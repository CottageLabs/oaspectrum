from service import sheets, models
import codecs

def export_csv(path):

    with codecs.open(path, "wb", "utf-8") as writer:
        out = sheets.ScoreSheet(writer=writer)
        for score in models.Score.scroll():
            out.add_dataobj(score)
        out.save()


