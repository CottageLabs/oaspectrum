from service.models import Score

# function for filtering score results as they are pulled through the search api
def filter_score(score_data):
    score = Score(score_data)
    score.remove_admin_data()
    return score.data
