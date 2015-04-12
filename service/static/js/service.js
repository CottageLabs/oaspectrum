jQuery(document).ready(function($) {

    $.extend(octopus, {
        page: {},
        service : {
            newScore : function(params) {
                var schema = {
                    id : {type : "single", path : "id", coerce: String },
                    created_date : {type : "single", path : "created_date", coerce: String},
                    last_updated : {type : "single", path : "last_updated", coerce: String},

                    journal_name : { type : "single", path : "journal.name", coerce : String},
                    journal_url : {type : "single", path : "journal.url", coerce : String},
                    issn : { type : "list", path : "journal.issn", coerce : String },
                    eissn : { type : "list", path : "journal.eissn", coerce: String },
                    publisher : { type: "single", path: "journal.publisher", coerce: String },

                    reader_rights_score : { type : "single", path : "reader_rights.score", coerce: parseInt},
                    reader_rights_url : { type: "single", path: "reader_rights_url", coerce: String },
                    reader_rights_relevant_text : { type: "single", path : "reader_rights.relevant_text", coerce: String },

                    reuse_rights_score : { type : "single", path : "reuse_rights.score", coerce: parseInt},
                    reuse_rights_url : { type: "single", path: "reuse_rights_url", coerce: String },
                    reuse_rights_relevant_text : { type: "single", path : "reuse_rights.relevant_text", coerce: String },

                    copyrights_score : { type : "single", path : "copyrights.score", coerce: parseInt},
                    copyrights_url : { type: "single", path: "copyrights_url", coerce: String },
                    copyrights_relevant_text : { type: "single", path : "copyrights.relevant_text", coerce: String },

                    author_posting_rights_score : { type : "single", path : "author_posting_rights.score", coerce: parseInt},
                    author_posting_rights_url : { type: "single", path: "author_posting_rights_url", coerce: String },
                    author_posting_rights_relevant_text : { type: "single", path : "author_posting_rights.relevant_text", coerce: String },

                    automatic_posting_rights_score : { type : "single", path : "reader_rights.score", coerce: parseInt},
                    automatic_posting_rights_url : { type: "single", path: "reader_rights_url", coerce: String },
                    automatic_posting_rights_relevant_text : { type: "single", path : "reader_rights.relevant_text", coerce: String },

                    machine_readability_score : { type : "single", path : "reader_rights.score", coerce: parseInt},
                    machine_readability_url : { type: "single", path: "reader_rights_url", coerce: String },
                    machine_readability_relevant_text : { type: "single", path : "reader_rights.relevant_text", coerce: String },

                    apc : { type: "single", path : "apc", coerce: String },
                    funder_policy_url : { type: "single", path : "funder_policy_url", coerce: String },
                    romeo_url : { type: "single", path : "romeo_url", coerce: String },
                    total : { type: "single", path : "total", coerce: parseInt },

                    publisher_contact_date : { type: "single", path : "admin.publisher_contact_date", coerce: String },
                    score_locked_date : { type: "single", path : "admin.score_locked_date", coerce: String },
                    last_upload_date : { type: "single", path : "admin.last_upload_date", coerce: String },
                    last_upload_by : { type: "single", path: "admin.last_upload_by", coerce: String }
                };

                var Score = function() {
                    this.data = {};
                    this.schema = {};
                    this.allow_off_schema = false;
                };

                var proto = $.extend(octopus.dataobj.DataObjPrototype, octopus.service.ScorePrototype);
                Score.prototype = proto;

                var dobj = new Score();
                dobj.schema = schema;
                if (params) {
                    if (params.raw) {
                        dobj.data = params.raw;
                    }
                }
                return dobj;
            },

            ScorePrototype : {

            }
        }
    });

});