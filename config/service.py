import os

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

ACCOUNT_ENABLE = True
ACCOUNT_RESET_EMAIL_SUBJECT = "Password reset"
ACCOUNT_LIST_USERS = True


# important overrides for the ES module

# elasticsearch back-end connection settings
ELASTIC_SEARCH_HOST = "http://localhost:9200"
ELASTIC_SEARCH_INDEX = "oas"
ELASTIC_SEARCH_VERSION = "1.4.2"

# Classes from which to retrieve ES mappings to be used in this application
ELASTIC_SEARCH_MAPPINGS = [
    "service.dao.ScoreDAO",
    "octopus.modules.account.dao.BasicAccountDAO",
    "octopus.modules.cache.dao.CachedFileDAO"
]

QUERY_ROUTE = {
    "query" : {
        "score" : {
            "auth" : False,
            "role" : None,
            "filters" : [],
            "dao" : "service.dao.ScoreDAO"
        }
    },
    "account_query" : {
        "account" : {
            "auth" : True,
            "role" : "list-users",
            "filters" : [
                "octopus.modules.account.dao.query_filter"
            ],
            "dao" : "octopus.modules.account.dao.BasicAccountDAO"
        }
    }
}

CLIENTJS_QUERY_ENDPOINT = "/query/score"

CRUD = {
    "score" : {
        "model" : "service.models.ScoreCrud",
        "create" : {
            "enable" : False
        },
        "retrieve" : {
            "enable" : True
        },
        "update" : {
            "enable" : False
        },
        "delete" : {
            "enable" : False
        }
    }
}

SEARCH_DAO = "service.dao.ScoreDAO"

SEARCH_RESULT_FILTER = "service.search.filter_score"

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "upload")

CACHE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "cache")

CACHE_GENERATORS = {
    "csv" : {
        "class" : "service.exporter.CSVCache",
        "timeout" : 1800
    }
}