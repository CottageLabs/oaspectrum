# WARNING Automatic deployment

Be careful when committing to the master branch, as this particular application is automatically deployed to production without human review! Forks are OK of course, it's just CottageLabs/oaspectrum .

# Open Access Spectrum 

Application which provides the management and UI for the Open Access Spectrum service

## Installation

Clone the project:

    git clone https://github.com/CottageLabs/oaspectrum.git

get all the submodules

    cd myapp
    git submodule init
    git submodule update

This will initialise and clone the esprit and magnificent octopus libraries

Then get the submodules for Magnificent Octopus

    cd myapp/magnificent-octopus
    git submodule init
    git submodule update

Create your virtualenv and activate it

    virtualenv /path/to/venv
    source /path/tovenv/bin/activate

Install esprit and magnificent octopus (in that order)

    cd myapp/esprit
    pip install -e .
    
    cd myapp/magnificent-octopus
    pip install -e .
    
Create your local config

    cd myapp
    touch local.cfg

Then you can override any config values that you need to

To start your application, you'll also need to install it into the virtualenv just this first time

    cd myapp
    pip install -e .

Then, start your app with

    python service/web.py

If you want to specify your own root config file, you can use

    APP_CONFIG=path/to/rootcfg.py python service/web.py


## Data Model

\* - required field

```json
{
    "id" : "<opaque id for score>",
    "created_date" : "<date record created>",
    "last_updated" : "<date record last updated>",
    
    "journal" : {
        "name" : "<name of journal *>",
        "url" : "<url to journal home page *>",
        "issn" : [<issn *>],
        "eissn" : [<eissn>],
        "publisher" : "<publisher>"
    },
    
    "reader_rights" : {
        "score" : <integer score *>,
        "url" : "<url *>",
        "text" : "<relevant text *>"
    },
    "reuse_rights" : {
        "score" : <integer score *>,
        "url" : "<url *>",
        "text" : "<relevant text *>"
    },
    "copyrights" : {
        "score" : <integer score *>,
        "url" : "<url *>",
        "text" : "<relevant text *>"
    },
    "author_posting_rights" : {
        "score" : <integer score *>,
        "url" : "<url *>",
        "text" : "<relevant text *>"
    },
    "automatic_posting_rights" : {
        "score" : <integer score *>,
        "url" : "<url *>",
        "text" : "<relevant text *>"
    },
    "machine_readability" : {
        "score" : <integer score *>,
        "url" : "<url *>",
        "text" : "<relevant text *>"
    },
    
    "apc" : "<apc price (as plain text)>",
    "funder_policy_url" : "<funder policy url>",
    "romeo_url" : "<sherpa romeo url>",
    
    "total" : <total score as integer *>
    
    "admin" : {
        "publisher_contact_date" : "<publisher contact date>",
        "score_locked_date" : "<score locked date>",
        "last_upload_date" : "<when this record was last uploaded by csv *>",
        "last_uploaded_by" : "<user who last uploaded this record *>"
    }
}
```

# API

## Search API

To search OA Spectrum, go to:

    /api/search

The search API takes 3 query parameters:

* q - the query string, which can be formatted as per the [Lucene Query Syntax](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html).  Required.
* page - the page number of results to return. Optional, defaults to 1.
* pageSize - the number of results to return in a single page (max size 100). Optional, defaults to 10.

For example:

    GET /api/search?q=Pharmaceutica&page=2&pageSize=10

This will return a JSON document of the following form:

```json
{
    "query": "Pharmaceutica",
    "page": 2,
    "pageSize": 10,
    "total": 33,
    "timestamp": "2015-0429T10:43:18Z",
    "results": [],
}
```

The results array will contain a list, ordered by relevance to your query, of objects which conform to the data model
described above (without the admin data).

To query a specific field using the Lucene syntax, you can use the paths to the fields you want to query on from the data model.

For example, to query by ISSN:

    GET /api/search?q=journal.issn:1234-5678+OR+journal.eissn:1234-5678&page=2&pageSize=10

You may also use the "exact" keyword to force a field to match exactly the string you are passing in, rather than the
default tokenised matching.

The same ISSN query would be:

    GET /api/search?q=journal.issn.exact:1234-5678+OR+journal.eissn.exact:1234-5678&page=2&pageSize=10

## Retrieve API

Each document in the search results will provide you with an id, and the document represented by this ID can be
pulled on its own from the Retrieve API:

    GET /api/score/<id>

This will return a JSON document for only that record, formatted as described above.