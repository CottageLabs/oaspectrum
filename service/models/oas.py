from service import dao
from octopus.lib import dataobj

class Score(dataobj.DataObj, dao.ScoreDAO):
    """
    {
        "id" : "<opaque id for score>",
        "created_date" : "<date record created>",
        "last_updated" : "<date record last updated>",

        "journal" : {
            "name" : "<name of journal>",
            "url" : "<url to journal home page>",
            "issn" : [<issn>],
            "eissn" : [<eissn>],
            "publisher" : "<publisher>"
        },

        "reader_rights" : {
            "score" : <integer score>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "reuse_rights" : {
            "score" : <integer score>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "copyrights" : {
            "score" : <integer score>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "author_posting_rights" : {
            "score" : <integer score>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "automatic_posting_rights" : {
            "score" : <integer score>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },
        "machine_readability" : {
            "score" : <integer score>,
            "url" : "<url>",
            "text" : "<relevant text>"
        },

        "apc" : "<apc price (as plain text)>",
        "funder_policy_url" : "<funder policy url>",
        "romeo_url" : "<sherpa romeo url>",

        "total" : <total score as integer>

        "admin" : {
            "publisher_contact_date" : "<publisher contact date>",
            "score_locked_date" : "<score locked date>",
            "last_upload_date" : "<when this record was last uploaded by csv>",
            "last_uploaded_by" : "<user who last uploaded this record>"
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
        self._set_single("journal.name", val, coerce=self._utf8_unicode())

    @property
    def journal_url(self):
        return self._get_single("journal.url", coerce=self._utf8_unicode())

    @journal_url.setter
    def journal_url(self, val):
        self._set_single("journal.url", val, coerce=self._utf8_unicode())

    @property
    def issn(self):
        return self._get_list("journal.issn", coerce=self._utf8_unicode())

    @issn.setter
    def issn(self, val):
        self._set_list("journal.issn", val, coerce=self._utf8_unicode())

    @property
    def eissn(self):
        return self._get_list("journal.eissn", coerce=self._utf8_unicode())

    @eissn.setter
    def eissn(self, val):
        self._set_list("journal.eissn", val, coerce=self._utf8_unicode())

    @property
    def publisher(self):
        return self._get_single("journal.publisher", coerce=self._utf8_unicode())

    @publisher.setter
    def publisher(self, val):
        self._set_single("journal.publisher", val, coerce=self._utf8_unicode())


    #######################################################
    ## Reader Rights

    @property
    def reader_rights_score(self):
        return self._get_single("reader_rights.score", coerce=self._int())

    @reader_rights_score.setter
    def reader_rights_score(self, val):
        self._set_single("reader_rights.score", val, coerce=self._int())

    @property
    def reader_rights_url(self):
        return self._get_single("reader_rights.url", coerce=self._utf8_unicode())

    @reader_rights_url.setter
    def reader_rights_url(self, val):
        self._set_single("reader_rights.url", val, coerce=self._utf8_unicode())

    @property
    def reader_rights_relevant_text(self):
        return self._get_single("reader_rights.text", coerce=self._utf8_unicode())

    @reader_rights_relevant_text.setter
    def reader_rights_relevant_text(self, val):
        self._set_single("reader_rights.text", val, coerce=self._utf8_unicode())


    #######################################################
    ## Reuse Rights

    @property
    def reuse_rights_score(self):
        return self._get_single("reuse_rights.score", coerce=self._int())

    @reuse_rights_score.setter
    def reuse_rights_score(self, val):
        self._set_single("reuse_rights.score", val, coerce=self._int())

    @property
    def reuse_rights_url(self):
        return self._get_single("reuse_rights.url", coerce=self._utf8_unicode())

    @reuse_rights_url.setter
    def reuse_rights_url(self, val):
        self._set_single("reuse_rights.url", val, coerce=self._utf8_unicode())

    @property
    def reuse_rights_relevant_text(self):
        return self._get_single("reuse_rights.text", coerce=self._utf8_unicode())

    @reuse_rights_relevant_text.setter
    def reuse_rights_relevant_text(self, val):
        self._set_single("reuse_rights.text", val, coerce=self._utf8_unicode())


    #######################################################
    ## Copyrights

    @property
    def copyrights_score(self):
        return self._get_single("copyrights.score", coerce=self._int())

    @copyrights_score.setter
    def copyrights_score(self, val):
        self._set_single("copyrights.score", val, coerce=self._int())

    @property
    def copyrights_url(self):
        return self._get_single("copyrights.url", coerce=self._utf8_unicode())

    @copyrights_url.setter
    def copyrights_url(self, val):
        self._set_single("copyrights.url", val, coerce=self._utf8_unicode())

    @property
    def copyrights_relevant_text(self):
        return self._get_single("copyrights.text", coerce=self._utf8_unicode())

    @copyrights_relevant_text.setter
    def copyrights_relevant_text(self, val):
        self._set_single("copyrights.text", val, coerce=self._utf8_unicode())


    #######################################################
    ## Author Posting Rights

    @property
    def author_posting_rights_score(self):
        return self._get_single("author_posting_rights.score", coerce=self._int())

    @author_posting_rights_score.setter
    def author_posting_rights_score(self, val):
        self._set_single("author_posting_rights.score", val, coerce=self._int())

    @property
    def author_posting_rights_url(self):
        return self._get_single("author_posting_rights.url", coerce=self._utf8_unicode())

    @author_posting_rights_url.setter
    def author_posting_rights_url(self, val):
        self._set_single("author_posting_rights.url", val, coerce=self._utf8_unicode())

    @property
    def author_posting_rights_relevant_text(self):
        return self._get_single("author_posting_rights.text", coerce=self._utf8_unicode())

    @author_posting_rights_relevant_text.setter
    def author_posting_rights_relevant_text(self, val):
        self._set_single("author_posting_rights.text", val, coerce=self._utf8_unicode())


    #######################################################
    ## Automatic Posting Rights

    @property
    def automatic_posting_rights_score(self):
        return self._get_single("automatic_posting_rights.score", coerce=self._int())

    @automatic_posting_rights_score.setter
    def automatic_posting_rights_score(self, val):
        self._set_single("automatic_posting_rights.score", val, coerce=self._int())

    @property
    def automatic_posting_rights_url(self):
        return self._get_single("automatic_posting_rights.url", coerce=self._utf8_unicode())

    @automatic_posting_rights_url.setter
    def automatic_posting_rights_url(self, val):
        self._set_single("automatic_posting_rights.url", val, coerce=self._utf8_unicode())

    @property
    def automatic_posting_rights_relevant_text(self):
        return self._get_single("automatic_posting_rights.text", coerce=self._utf8_unicode())

    @automatic_posting_rights_relevant_text.setter
    def automatic_posting_rights_relevant_text(self, val):
        self._set_single("automatic_posting_rights.text", val, coerce=self._utf8_unicode())


    #######################################################
    ## Machine Readability

    @property
    def machine_readability_score(self):
        return self._get_single("machine_readability.score", coerce=self._int())

    @machine_readability_score.setter
    def machine_readability_score(self, val):
        self._set_single("machine_readability.score", val, coerce=self._int())

    @property
    def machine_readability_url(self):
        return self._get_single("machine_readability.url", coerce=self._utf8_unicode())

    @machine_readability_url.setter
    def machine_readability_url(self, val):
        self._set_single("machine_readability.url", val, coerce=self._utf8_unicode())

    @property
    def machine_readability_relevant_text(self):
        return self._get_single("machine_readability.text", coerce=self._utf8_unicode())

    @machine_readability_relevant_text.setter
    def machine_readability_relevant_text(self, val):
        self._set_single("machine_readability.text", val, coerce=self._utf8_unicode())


    #######################################################
    ## Top Level Properties

    @property
    def apc(self):
        return self._get_single("apc", coerce=self._utf8_unicode())

    @apc.setter
    def apc(self, val):
        self._set_single("apc", val, coerce=self._utf8_unicode())

    @property
    def funder_policy_url(self):
        return self._get_single("funder_policy_url", coerce=self._utf8_unicode())

    @funder_policy_url.setter
    def funder_policy_url(self, val):
        self._set_single("funder_policy_url", val, coerce=self._utf8_unicode())

    @property
    def romeo_url(self):
        return self._get_single("romeo_url", coerce=self._utf8_unicode())

    @romeo_url.setter
    def romeo_url(self, val):
        self._set_single("romeo_url", val, coerce=self._utf8_unicode())

    @property
    def total(self):
        return self._get_single("total", coerce=self._int())

    @total.setter
    def total(self, val):
        self._set_single("total", val, coerce=self._int())


    #######################################################
    ## Admin Properties

    @property
    def publisher_contact_date(self):
        return self._get_single("admin.publisher_contact_date", coerce=self._date_str())

    @publisher_contact_date.setter
    def publisher_contact_date(self, val):
        self._set_single("admin.publisher_contact_date", val, coerce=self._date_str())

    @property
    def score_locked_date(self):
        return self._get_single("admin.score_locked_date", coerce=self._date_str())

    @score_locked_date.setter
    def score_locked_date(self, val):
        self._set_single("admin.score_locked_date", val, coerce=self._date_str())

    @property
    def last_upload_date(self):
        return self._get_single("admin.last_upload_date", coerce=self._date_str())

    @last_upload_date.setter
    def last_upload_date(self, val):
        self._set_single("admin.last_upload_date", val, coerce=self._date_str())

    @property
    def last_upload_by(self):
        return self._get_single("admin.last_upload_by", coerce=self._utf8_unicode())

    @last_upload_by.setter
    def last_upload_by(self, val):
        self._set_single("admin.last_upload_by", val, coerce=self._utf8_unicode())