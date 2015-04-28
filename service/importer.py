from octopus.lib import dataobj
from service import sheets, models
import re
from datetime import datetime
from flask.ext.login import current_user

ISSN_RX = "^[0-9]{4}-[0-9]{3}[X0-9]$"

class ImportException(Exception):
    pass

def import_csv(path):

    def _url_check(reference_issn, o, field, name):
        if o.get(field) is not None and not o.get(field).startswith("http"):
            raise ImportException("{n} for ISSN {x} is malformed: {y}".format(n=name, x=reference_issn, y=o.get(field)))

    def _score_check(reference_issn, o, field, name):
        if o.get(field) is None:
            raise ImportException("{n} for ISSN {x} is not set".format(n=name, x=reference_issn))
        coerce = dataobj.DataObj()._int()
        try:
            coerce(o.get(field))
        except ValueError:
            raise ImportException("{n} for ISSN {x} is not an integer: {y}".format(n=name, x=reference_issn, y=o.get(field)))

    def _is_delete(o):
        for key, value in o.iteritems():
            if key not in ["issn", "eissn"]:
                if value is not None and value != "":
                    return False
        return True

    # load the data from a sheet
    sheet = sheets.ScoreSheet(path)

    # attempt to parse everything to data objects, doing some validation
    # along the way
    scores = []
    deletes = []
    for o in sheet.objects():
        # check that at least one issn exists, and that both are formatted correctly
        if o.get("issn") is None and o.get("eissn") is None:
            raise ImportException("All records must have ISSNs")

        if o.get("issn") is not None and not re.match(ISSN_RX, o.get("issn")):
            raise ImportException("ISSN {x} is malformed; should be of the form NNNN-NNNN".format(x=o.get("issn")))

        if o.get("eissn") is not None and not re.match(ISSN_RX, o.get("eissn")):
            raise ImportException("E-ISSN {x} is malformed; should be of the form NNNN-NNNN".format(x=o.get("eissn")))

        issns = []
        if o.get("issn") is not None:
            issns.append(o.get("issn"))
        if o.get("eissn") is not None:
            issns.append(o.get("eissn"))

        # at this point we can determine if this is a delete, which is signified by all elements other than
        # the issn(s) being empty
        if _is_delete(o):
            deletes.append(issns)
            continue

        reference_issn = o.get("issn") if o.get("issn") is not None else o.get("eissn")

        # check that all the urls are empty or start with http
        _url_check(reference_issn, o, "reader_rights_url", "Reader Rights URL")
        _url_check(reference_issn, o, "reuse_rights_url", "Reuse Rights URL")
        _url_check(reference_issn, o, "copyrights_url", "Copyrights URL")
        _url_check(reference_issn, o, "author_posting_rights_url", "Author Posting Rights URL")
        _url_check(reference_issn, o, "automatic_posting_rights_url", "Automatic Posting Rights URL")
        _url_check(reference_issn, o, "machine_readability_url", "Machine Readability URL")

        # check that all the scores are integers (don't bother with range checking, this is a format check only)
        _score_check(reference_issn, o, "reader_rights_score", "Reader Rights Score")
        _score_check(reference_issn, o, "reuse_rights_score", "Reuse Rights Score")
        _score_check(reference_issn, o, "copyrights_score", "Copyrights Score")
        _score_check(reference_issn, o, "author_posting_rights_score", "Author Posting Rights Score")
        _score_check(reference_issn, o, "automatic_posting_rights_score", "Automatic Posting Rights Score")
        _score_check(reference_issn, o, "machine_readability_score", "Machine Readability Score")

        # if we get to here, we are good to import the object by creating the model and then saving it

        # first we want to see if this is one we already have
        existing = models.Score.pull_by_issn(issns)

        # to ensure we don't accidentally carry over unwanted data, we'll make a new one from scratch
        score = models.Score()

        # now, populate it with the new data
        try:
            score.populate(o)
        except dataobj.DataSchemaException as e:
            raise ImportException(reference_issn + ": " + e.message)

        # now carry over any relevant old data
        if existing is not None:
            score.id = existing.id
            score.created_date = existing.created_date

        # now add the provenance metadata
        score.last_upload_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        if not current_user.is_anonymous():
            score.last_upload_by = current_user.email
        else:
            score.last_upload_by = "anonymous"

        scores.append(score)

    # delete any issns that are scheduled for deletion
    for issns in deletes:
        models.Score.delete_by_issns(issns)

    # finally, once they all parse, save them
    for score in scores:
        score.save()
