from octopus.lib import clcsv

class ScoreSheet(clcsv.SheetWrapper):

    HEADERS = {
        "Journal Name" : "journal_name",
        "Journal URL" : "journal_url",
        "Reader Rights Score" : "reader_rights_score",
        "Reader Rights URL" : "reader_rights_url",
        "Reader Rights Relevant Text" : "reader_rights_relevant_text",
        "Reuse Rights Score" : "reuse_rights_score",
        "Reuse Rights URL" : "reuse_rights_url",
        "Reuse Rights Relevant Text" : "reuse_rights_relevant_text",
        "Copyrights Score" : "copyrights_score",
        "Copyrights URL" : "copyrights_url",
        "Copyrights Relevant Text" : "copyrights_relevant_text",
        "Author Posting Rights Score" : "author_posting_rights_score",
        "Author Posting Rights URL" : "author_posting_rights_url",
        "Author Posting Rights Relevant Text" : "author_posting_rights_relevant_text",
        "Automatic Posting Score" : "automatic_posting_score",
        "Automatic Posting Rights URL" : "automatic_posting_url",
        "Automatic Posting Rights Relevant Text" : "automatic_posting_relevant_text",
        "Machine Readability Score" : "machine_readability_score",
        "Machine Readability URL" : "machine_readability_url",
        "Machine Readability Relevant Text"  : "machine_readability_relevant_text",
        "APC Price" : "apc_price",
        "Funder Policy URL" : "funder_policy_url",
        "SHERPA/RoMEO URL" : "romeo_url",
        "Journal ISSN" : "issn",
        "Total Score" : "total",
        "Publisher" : "publisher",
        "Publisher Contact Date" : "publisher_contact_date",
        "Score Locked Date" : "score_locked_date"
    }

    EMPTY_STRING_AS_NONE = True
