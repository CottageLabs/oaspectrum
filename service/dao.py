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