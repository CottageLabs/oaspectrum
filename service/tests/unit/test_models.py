from octopus.modules.es import testindex
from octopus.lib import dataobj
from service import models

class TestModels(testindex.ESTestCase):

    def setUp(self):
        super(TestModels, self).setUp()

    def tearDown(self):
        super(TestModels, self).tearDown()

    def test_01_model(self):
        fields_and_values = {
            "id" : "123456",
            "journal_name" : "Journal of THings",
            "journal_url" : "http://www.journal.com",
            "issn" : ("1234-5678", ["1234-5678"]),
            "eissn" : ("9876-5432", ["9876-5432"]),
            "publisher" : "A Pub",
            "reader_rights_score" : ("4", 4),
            "reader_rights_url" : "http://rr.url",
            "reader_rights_relevant_text" : "whatever",
            "reuse_rights_score" : ("8", 8),
            "reuse_rights_url" : "http://reuse.com",
            "reuse_rights_relevant_text" : "another",
            "copyrights_score" : ("9", 9),
            "copyrights_url" : "http://copyrights.com",
            "copyrights_relevant_text" : "copy",
            "author_posting_rights_score" : ("1", 1),
            "author_posting_rights_url" : "http://apr.com",
            "author_posting_rights_relevant_text" : "postit",
            "automatic_posting_rights_score" : ("2", 2),
            "automatic_posting_rights_url" : "http://auto.com",
            "automatic_posting_rights_relevant_text" : "automate!",
            "machine_readability_score" : ("3", 3),
            "machine_readability_url" : "http://mr.com",
            "machine_readability_relevant_text" : "readme",
            "apc" : ("GBP100", "GBP100"),
            "funder_policy_url" : "http://fp.url",
            "romeo_url" : "http://romeo.url",
            "total" : ("34", 34),
            "publisher_contact_date" : "2015-01-01T00:00:00Z",
            "score_locked_date" : "2014-01-01T00:00:00Z",
            "last_upload_date" : "2013-01-01T00:00:00Z",
            "last_upload_by" : "tester"
        }
        score = models.Score()
        dataobj.test_dataobj(score, fields_and_values)