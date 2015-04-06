from service import sheets, models
from octopus.core import initialise

# ensure the index is initialised
initialise()

# load the data from a sheet
sheet = sheets.ScoreSheet("/home/richard/Dropbox/Projects/OASpectrum/test_scores.csv")

# attempt to parse everything to data objects
obs = [o for o in sheet.dataobjs(models.Score)]

# if successful, save everything
for o in obs:
    o.save()