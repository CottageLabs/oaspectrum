from service import dao
from octopus.lib import dataobj
import math

class Score(dataobj.DataObj, dao.ScoreDAO):
    """
    {
        "id" : "<opaque id for score>",
        "created_date" : "<date record created>",
        "last_updated" : "<date record last updated>",

        "journal" : {
            "name" : "<name of journal *>",
            "url" : "<url to journal home page *>",
            "issn" : [<issn *>],
            "eissn" : [<eissn>],
            "publisher" : "<publisher>"
        },

        "reader_rights" : {
            "score" : <integer score *>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "reuse_rights" : {
            "score" : <integer score *>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "copyrights" : {
            "score" : <integer score *>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "author_posting_rights" : {
            "score" : <integer score *>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "automatic_posting_rights" : {
            "score" : <integer score *>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "machine_readability" : {
            "score" : <integer score *>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },

        "apc" : "<apc price (as plain text)>",
        "funder_policy_url" : "<funder policy url>",
        "romeo_url" : "<sherpa romeo url>",

        "total" : <total score as integer *>

        "admin" : {
            "publisher_contact_date" : "<publisher contact date>",
            "score_locked_date" : "<score locked date>",
            "last_upload_date" : "<when this record was last uploaded by csv *>",
            "last_uploaded_by" : "<user who last uploaded this record *>"
        }
    }
    """

    ####################################################################
    ## Journal information

    @property
    def journal_name(self):
        return self._get_single("journal.name", coerce=self._utf8_unicode())

    @journal_name.setter
    def journal_name(self, val):
        self._set_single("journal.name", val, coerce=self._utf8_unicode(), allow_none=False)

    @property
    def journal_url(self):
        return self._get_single("journal.url", coerce=self._utf8_unicode())

    @journal_url.setter
    def journal_url(self, val):
        self._set_single("journal.url", val, coerce=self._utf8_unicode(), allow_none=False)

    @property
    def issn(self):
        return self._get_list("journal.issn", coerce=self._utf8_unicode())

    @issn.setter
    def issn(self, val):
        self._set_list("journal.issn", val, coerce=self._utf8_unicode(), allow_none=False, ignore_none=True)

    @property
    def eissn(self):
        return self._get_list("journal.eissn", coerce=self._utf8_unicode())

    @eissn.setter
    def eissn(self, val):
        self._set_list("journal.eissn", val, coerce=self._utf8_unicode(), allow_none=False, ignore_none=True)

    @property
    def publisher(self):
        return self._get_single("journal.publisher", coerce=self._utf8_unicode())

    @publisher.setter
    def publisher(self, val):
        self._set_single("journal.publisher", val, coerce=self._utf8_unicode(), ignore_none=True)


    #######################################################
    ## Reader Rights

    @property
    def reader_rights_score(self):
        return self._get_single("reader_rights.score", coerce=self._int())

    @reader_rights_score.setter
    def reader_rights_score(self, val):
        self._set_single("reader_rights.score", val, coerce=self._int(), allow_none=False)

    @property
    def reader_rights_url(self):
        return self._get_single("reader_rights.url", coerce=self._utf8_unicode())

    @reader_rights_url.setter
    def reader_rights_url(self, val):
        self._set_single("reader_rights.url", val, coerce=self._utf8_unicode(), ignore_none=True)

    @property
    def reader_rights_relevant_text(self):
        return self._get_single("reader_rights.text", coerce=self._utf8_unicode())

    @reader_rights_relevant_text.setter
    def reader_rights_relevant_text(self, val):
        self._set_single("reader_rights.text", val, coerce=self._utf8_unicode(), ignore_none=True)


    #######################################################
    ## Reuse Rights

    @property
    def reuse_rights_score(self):
        return self._get_single("reuse_rights.score", coerce=self._int())

    @reuse_rights_score.setter
    def reuse_rights_score(self, val):
        self._set_single("reuse_rights.score", val, coerce=self._int(), allow_none=False)

    @property
    def reuse_rights_url(self):
        return self._get_single("reuse_rights.url", coerce=self._utf8_unicode())

    @reuse_rights_url.setter
    def reuse_rights_url(self, val):
        self._set_single("reuse_rights.url", val, coerce=self._utf8_unicode(), ignore_none=True)

    @property
    def reuse_rights_relevant_text(self):
        return self._get_single("reuse_rights.text", coerce=self._utf8_unicode())

    @reuse_rights_relevant_text.setter
    def reuse_rights_relevant_text(self, val):
        self._set_single("reuse_rights.text", val, coerce=self._utf8_unicode(), ignore_none=True)


    #######################################################
    ## Copyrights

    @property
    def copyrights_score(self):
        return self._get_single("copyrights.score", coerce=self._int())

    @copyrights_score.setter
    def copyrights_score(self, val):
        self._set_single("copyrights.score", val, coerce=self._int(), allow_none=False)

    @property
    def copyrights_url(self):
        return self._get_single("copyrights.url", coerce=self._utf8_unicode())

    @copyrights_url.setter
    def copyrights_url(self, val):
        self._set_single("copyrights.url", val, coerce=self._utf8_unicode(), ignore_none=True)

    @property
    def copyrights_relevant_text(self):
        return self._get_single("copyrights.text", coerce=self._utf8_unicode())

    @copyrights_relevant_text.setter
    def copyrights_relevant_text(self, val):
        self._set_single("copyrights.text", val, coerce=self._utf8_unicode(), ignore_none=True)


    #######################################################
    ## Author Posting Rights

    @property
    def author_posting_rights_score(self):
        return self._get_single("author_posting_rights.score", coerce=self._int())

    @author_posting_rights_score.setter
    def author_posting_rights_score(self, val):
        self._set_single("author_posting_rights.score", val, coerce=self._int(), allow_none=False)

    @property
    def author_posting_rights_url(self):
        return self._get_single("author_posting_rights.url", coerce=self._utf8_unicode())

    @author_posting_rights_url.setter
    def author_posting_rights_url(self, val):
        self._set_single("author_posting_rights.url", val, coerce=self._utf8_unicode(), ignore_none=True)

    @property
    def author_posting_rights_relevant_text(self):
        return self._get_single("author_posting_rights.text", coerce=self._utf8_unicode())

    @author_posting_rights_relevant_text.setter
    def author_posting_rights_relevant_text(self, val):
        self._set_single("author_posting_rights.text", val, coerce=self._utf8_unicode(), ignore_none=True)


    #######################################################
    ## Automatic Posting Rights

    @property
    def automatic_posting_rights_score(self):
        return self._get_single("automatic_posting_rights.score", coerce=self._int())

    @automatic_posting_rights_score.setter
    def automatic_posting_rights_score(self, val):
        self._set_single("automatic_posting_rights.score", val, coerce=self._int(), allow_none=False)

    @property
    def automatic_posting_rights_url(self):
        return self._get_single("automatic_posting_rights.url", coerce=self._utf8_unicode())

    @automatic_posting_rights_url.setter
    def automatic_posting_rights_url(self, val):
        self._set_single("automatic_posting_rights.url", val, coerce=self._utf8_unicode(), ignore_none=True)

    @property
    def automatic_posting_rights_relevant_text(self):
        return self._get_single("automatic_posting_rights.text", coerce=self._utf8_unicode())

    @automatic_posting_rights_relevant_text.setter
    def automatic_posting_rights_relevant_text(self, val):
        self._set_single("automatic_posting_rights.text", val, coerce=self._utf8_unicode(), ignore_none=True)


    #######################################################
    ## Machine Readability

    @property
    def machine_readability_score(self):
        return self._get_single("machine_readability.score", coerce=self._int())

    @machine_readability_score.setter
    def machine_readability_score(self, val):
        self._set_single("machine_readability.score", val, coerce=self._int(), allow_none=False)

    @property
    def machine_readability_url(self):
        return self._get_single("machine_readability.url", coerce=self._utf8_unicode())

    @machine_readability_url.setter
    def machine_readability_url(self, val):
        self._set_single("machine_readability.url", val, coerce=self._utf8_unicode(), ignore_none=True)

    @property
    def machine_readability_relevant_text(self):
        return self._get_single("machine_readability.text", coerce=self._utf8_unicode())

    @machine_readability_relevant_text.setter
    def machine_readability_relevant_text(self, val):
        self._set_single("machine_readability.text", val, coerce=self._utf8_unicode(), ignore_none=True)


    #######################################################
    ## Top Level Properties

    @property
    def apc(self):
        return self._get_single("apc", coerce=self._utf8_unicode())

    @apc.setter
    def apc(self, val):
        self._set_single("apc", val, coerce=self._utf8_unicode(), ignore_none=True)

    @property
    def funder_policy_url(self):
        return self._get_single("funder_policy_url", coerce=self._utf8_unicode())

    @funder_policy_url.setter
    def funder_policy_url(self, val):
        self._set_single("funder_policy_url", val, coerce=self._utf8_unicode(), ignore_none=True)

    @property
    def romeo_url(self):
        return self._get_single("romeo_url", coerce=self._utf8_unicode())

    @romeo_url.setter
    def romeo_url(self, val):
        self._set_single("romeo_url", val, coerce=self._utf8_unicode(), ignore_none=True)

    @property
    def total(self):
        return self._get_single("total", coerce=self._int())

    @total.setter
    def total(self, val):
        self._set_single("total", val, coerce=self._int(), allow_none=False)


    #######################################################
    ## Admin Properties

    @property
    def publisher_contact_date(self):
        return self._get_single("admin.publisher_contact_date", coerce=self._date_str())

    def format_publisher_contact_date(self, format="%e %b %Y"):
        return self._get_single("admin.publisher_contact_date", coerce=self._date_str(out_format=format))

    @publisher_contact_date.setter
    def publisher_contact_date(self, val):
        self._set_single("admin.publisher_contact_date", val, coerce=self._date_str(), ignore_none=True)

    @property
    def score_locked_date(self):
        return self._get_single("admin.score_locked_date", coerce=self._date_str())

    @score_locked_date.setter
    def score_locked_date(self, val):
        self._set_single("admin.score_locked_date", val, coerce=self._date_str(), ignore_none=True)

    @property
    def last_upload_date(self):
        return self._get_single("admin.last_upload_date", coerce=self._date_str())

    def format_last_upload_date(self, format="%e %b %Y"):
        return self._get_single("admin.last_upload_date", coerce=self._date_str(out_format=format))

    @last_upload_date.setter
    def last_upload_date(self, val):
        self._set_single("admin.last_upload_date", val, coerce=self._date_str(), allow_none=False)

    @property
    def last_upload_by(self):
        return self._get_single("admin.last_upload_by", coerce=self._utf8_unicode())

    @last_upload_by.setter
    def last_upload_by(self, val):
        self._set_single("admin.last_upload_by", val, coerce=self._utf8_unicode(), allow_none=False)


    ####################################################################
    ## Utility properties

    @property
    def score_id(self):
        eissns = self.eissn
        if len(eissns) > 0:
            return eissns[0]
        pissns = self.issn
        if len(pissns) > 0:
            return pissns[0]
        return self.id

    @property
    def nearest_ten(self):
        return (self.total / 10) * 10 # take advantage of how python treats integers

    def _band(self, score, bands):
        band = 1
        boundaries = bands.keys()
        boundaries.sort()
        for b in boundaries:
            if score >= b:
                band = bands[b]
            else:
                break
        return band

    @property
    def reader_rights_band(self):
        bands = {0 : 1, 5 : 2, 12 : 3, 16 : 4, 20 : 5}
        return self._band(self.reader_rights_score, bands)

    @property
    def reuse_rights_band(self):
        bands = {0 : 1, 4 : 2, 7 : 3, 14 : 4, 20 : 5}
        return self._band(self.reuse_rights_score, bands)

    @property
    def copyrights_band(self):
        bands = {0 : 1, 4 : 2, 10 : 4, 16 : 5}  # Note that there is no middle band here
        return self._band(self.copyrights_score, bands)

    @property
    def author_posting_rights_band(self):
        bands = {0 : 1, 4 : 2, 6 : 3, 10 : 4, 16 : 5}
        return self._band(self.author_posting_rights_score, bands)

    @property
    def automatic_posting_rights_band(self):
        bands = {0 : 1, 2 : 2, 4 : 3, 8 : 4, 12 : 5}
        return self._band(self.automatic_posting_rights_score, bands)

    @property
    def machine_readability_band(self):
        bands = {0 : 1, 4 : 2, 8 : 3, 12 : 4, 16 : 5}
        return self._band(self.machine_readability_score, bands)

    def remove_admin_data(self):
        self._delete("admin")


