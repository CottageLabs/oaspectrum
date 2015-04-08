jQuery(document).ready(function($) {

    /****************************************************************
     * Application Facetview Theme
     *****************************
     */

    function discoveryRecordView(options, record) {
        var result = options.resultwrap_start;
        result += "<div class='row-fluid' style='margin-top: 10px; margin-bottom: 10px'>";
        result += "<div class='span12'>";
        result += "<strong style='font-size: 150%'>" + record["id"] + "</strong><br>";
        result += "</div></div>";
        result += options.resultwrap_end;
        return result;
    }

    var facets = [];
    facets.push({'field': 'journal.publisher.exact', 'display': 'Publisher'});
    facets.push({
        field: "reader_rights.score",
        display: "Reader Rights Score",
        type: "range",
        range : [
            {"from" : 0, "to" : 5, "display" : "< 5"},
            {"from" : 5, "to" : 10, "display" : "5 - 10"},
            {"from" : 10, "to" : 15, "display" : "10 - 15"},
            {"from" : 15, "display" : "15 - 20"}
        ]
    });

    $('#publicsearch').facetview({
        debug: true,
        search_url : octopus.config.query_endpoint,
        page_size : 10,
        facets : facets,
        search_sortby : [
            {'display':'Journal Name','field':'journal.name.exact'},
            {'display':'Publisher','field':'journal.publisher.exact'}
        ],
        searchbox_fieldselect : [
            {'display':'Journal Name','field':'journal.name'},
            {"display" : "ISSN", "field" : "ISSN"}
        ],
        render_result_record : discoveryRecordView,
        sharesave_link: false
    });

});
