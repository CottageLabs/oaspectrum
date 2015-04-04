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