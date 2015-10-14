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
ACCOUNT_DEFAULT_ROLES = ["admin"]   # all system users are admins

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

DATE_FORMATS = [
    # the US formats
    "%m/%d/%Y",
    "%m/%d/%y",
    # other formats
    "%Y-%m-%dT%H:%M:%SZ",   # e.g. 2014-09-23T11:30:45Z
    "%Y-%m-%d",             # e.g. 2014-09-23
    "%d/%m/%y",             # e.g. 29/02/80
    "%d/%m/%Y",             # e.g. 29/02/1980
    "%d-%m-%Y",             # e.g. 01-01-2015
    "%Y.%m.%d",             # e.g. 2014.09.12
    "%d.%m.%Y",             # e.g. 12.9.2014
    "%d.%m.%y",             # e.g. 12.9.14
    "%d %B %Y",             # e.g. 21 June 2014
    "%d-%b-%Y",             # e.g. 31-Jul-13
    "%d-%b-%y",             # e.g. 31-Jul-2013
    "%b-%y",                # e.g. Aug-13
    "%B %Y",                # e.g. February 2014
    "%Y"                    # e.g. 1978
]