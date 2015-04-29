from service import sheets, models
import codecs
from octopus.modules.cache.models import CacheGenerator

class CSVCache(CacheGenerator):
    def generate(self, path):
        export_csv(path)

def export_csv(path):
    with codecs.open(path, "wb", "utf-8") as writer:
        out = sheets.ScoreSheet(writer=writer)
        for score in models.Score.scroll():
            out.add_dataobj(score)
        out.save()


