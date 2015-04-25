# overrides for the webapp deployment
DEBUG = True
PORT = 5022
SSL = False
THREADED = True

MAIL_FROM_ADDRESS = "none@example.com"
MAIL_SUBJECT_PREFIX = "OA Spectrum: "

# override these in local.cfg
MAIL_SERVER = None
MAIL_PORT = None
MAIL_USERNAME = None
MAIL_PASSWORD = None

# Overrides for the account module
SECRET_KEY = "oaspectrum"   # for dev, replace this in the deployment

ACCOUNT_RESET_EMAIL_SUBJECT = "Password reset"



# important overrides for the ES module

# elasticsearch back-end connection settings
ELASTIC_SEARCH_HOST = "http://localhost:9200"
ELASTIC_SEARCH_INDEX = "oas"
ELASTIC_SEARCH_VERSION = "1.4.2"

# Classes from which to retrieve ES mappings to be used in this application
ELASTIC_SEARCH_MAPPINGS = [
    "service.dao.ScoreDAO",
    "octopus.modules.account.dao.BasicAccountDAO"
]

QUERY_ROUTE = {
    "query" : {                                 # the URL route at which it is mounted
        "score" : {                             # the URL name for the index type being queried
            "auth" : False,                     # whether the route requires authentication
            "role" : None,                      # if authenticated, what role is required to access the query endpoint
            "filters" : [],            # names of the standard filters to apply to the query
            "dao" : "service.dao.ScoreDAO"       # classpath for DAO which accesses the underlying ES index
        }
    }
}

CLIENTJS_QUERY_ENDPOINT = "/query/score"

