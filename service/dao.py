from octopus.modules.es import dao
from octopus.core import app

class ScoreDAO(dao.ESDAO):
    __type__ = 'score'
