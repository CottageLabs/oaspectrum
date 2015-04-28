from octopus.modules.es import dao
from octopus.core import app

class ScoreDAO(dao.ESDAO):
    __type__ = 'score'

    @classmethod
    def pull_by_issn(cls, issn):
        q = ISSNQuery(issn)
        obs = cls.object_query(q.query())
        if len(obs) > 0:
            return obs[0]

    @classmethod
    def delete_by_issns(cls, issns):
        if not isinstance(issns, list):
            issns = [issns]
        q = ISSNSQuery(issns)
        cls.delete_by_query(q.query())

class ISSNSQuery(object):
    def __init__(self, issns):
        self.issns = issns

    def query(self):
        return {
            "query" : {
                "bool" : {
                    "should" : [
                        {"terms" : {"journal.issn.exact" : self.issns}},
                        {"terms" : {"journal.eissn.exact" : self.issns}}
                    ]
                }
            }
        }

class ISSNQuery(object):
    def __init__(self, issn):
        self.issn = issn

    def query(self):
        return {
            "query" : {
                "bool" : {
                    "should" : [
                        {"term" : {"journal.issn.exact" : self.issn}},
                        {"term" : {"journal.eissn.exact" : self.issn}}
                    ]
                }
            }
        }