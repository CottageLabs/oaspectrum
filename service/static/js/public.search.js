jQuery(document).ready(function($) {

    /****************************************************************
     * Application Facetview Theme
     *****************************
     */

    ///////////////////////////////////////////////////////////////////
    // overrides on the default facetview options

    function customFacetview(options) {
        /*****************************************
         * overrides must provide the following classes and ids
         *
         * id: facetview - main div in which the facetview functionality goes
         * id: facetview_filters - div where the facet filters will be displayed
         * id: facetview_rightcol - the main window for result display (doesn't have to be on the right)
         * class: facetview_search_options_container - where the search bar and main controls will go
         * id : facetview_selectedfilters - where we summarise the filters which have been selected
         * class: facetview_metadata - where we want paging to go
         * id: facetview_results - the table id for where the results actually go
         * id: facetview_searching - where the loading notification can go
         *
         * Should respect the following configs
         *
         * options.debug - is this a debug enabled facetview.  If so, put a debug textarea somewhere
         */

        // the facet view object to be appended to the page
        var thefacetview = '<div id="facetview"><div class="row">';

        // if there are facets, give them span3 to exist, otherwise, take up all the space
        var showfacets = false;
        for (var i = 0; i < options.facets.length; i++) {
            var f = options.facets[i];
            if (!f.hidden) {
                showfacets = true;
                break;
            }
        }
        if (showfacets) {
            thefacetview += '<div class="col-md-9" id="facetview_rightcol">';
        } else {
            thefacetview += '<div class="col-md-12" id="facetview_rightcol">';
        }

        // make space for the search options container at the top
        thefacetview += '<div class="facetview_search_options_container"></div>';

        // make space for the selected filters
        thefacetview += '<div><div class="row"><div class="col-md-12"><div class="btn-toolbar" id="facetview_selectedfilters" style="display:none"></div></div></div></div>';

        // make space at the top for the pager
        thefacetview += '<div class="facetview_metadata" style="margin-top:5px;"></div>';

        // insert loading notification
        thefacetview += '<div class="facetview_searching" style="display:none"></div>';

        // insert the div within which the results actually will go
        thefacetview += '<div id="facetview_results" dir="auto"></div>';

        // make space at the bottom for the pager
        thefacetview += '<div class="facetview_metadata"></div>';

        // debug window near the bottom
        if (options.debug) {
            thefacetview += '<div class="facetview_debug" style="display:none"><textarea style="width: 95%; height: 300px"></textarea></div>'
        }

        // close off all the main container
        thefacetview += '</div>';

        // if we are rendering facets, put that division in
        if (showfacets) {
            thefacetview += '<div class="col-md-3"><div id="facetview_filters"></div></div>';
        }

        // close off the outer containers
        thefacetview += '</div></div>';

        return thefacetview
    }

    function customSearchOptions(options) {
        /*****************************************
         * overrides must provide the following classes and ids
         *
         * class: facetview_startagain - reset the search parameters
         * class: facetview_pagesize - size of each result page
         * class: facetview_order - ordering direction of results
         * class: facetview_orderby - list of fields which can be ordered by
         * class: facetview_searchfield - list of fields which can be searched on
         * class: facetview_freetext - input field for freetext search
         * class: facetview_force_search - button which triggers a search on the current page status
         *
         * should (not must) respect the following configs
         *
         * options.search_sortby - list of sort fields and directions
         * options.searchbox_fieldselect - list of fields search can be focussed on
         * options.sharesave_link - whether to provide a copy of a link which can be saved
         * options.search_button - whether to provide a button to force a search
         */

        var searchopts = '<div class="row"> \
            <div class="col-md-5">';

        if (options.search_sortby.length > 0) {
            searchopts += '' +
                '<form class="form-inline"> \
                    <div class="form-group"> \
                        <div class="input-group"> \
                            <span class="input-group-btn"> \
                                <button class="btn btn-default facetview_order btn-sm" title="Current order descending. Click to change to ascending" href="desc"> \
                                    sort <span class="glyphicon glyphicon-arrow-down"></span> by \
                                </button> \
                            </span> \
                            <select class="facetview_orderby form-control input-sm"> \
                                <option value="">Relevance</option>';

            for (var each = 0; each < options.search_sortby.length; each++) {
                var obj = options.search_sortby[each];
                var sortoption = '';
                if ($.type(obj['field']) == 'array') {
                    sortoption = sortoption + '[';
                    sortoption = sortoption + "'" + obj['field'].join("','") + "'";
                    sortoption = sortoption + ']';
                } else {
                    sortoption = obj['field'];
                }
                searchopts += '<option value="' + sortoption + '">' + obj['display'] + '</option>';
            }

            searchopts += ' </select> \
                        </div> \
                    </div> \
                </form>';
        } else {
            searchopts += "&nbsp;"
        }

        searchopts += '' +
            '</div>';  // closes the left hand part of the search options

        // select box for fields to search on
        var field_select = "";
        if ( options.searchbox_fieldselect.length > 0 ) {
            field_select += '<select class="facetview_searchfield form-control input-sm" style="width: 120px">';
            field_select += '<option value="">search all</option>';

            for (var each = 0; each < options.searchbox_fieldselect.length; each++) {
                var obj = options.searchbox_fieldselect[each];
                field_select += '<option value="' + obj['field'] + '">' + obj['display'] + '</option>';
            }
            field_select += '</select>';
        }

        searchopts += '' +
            '<div class="col-md-7"> \
                <form class="form-inline pull-right"> \
                    <div class="form-group"> \
                        <div class="input-group"> \
                            <span class="input-group-btn"> \
                                <button class="btn btn-danger facetview_startagain btn-sm" title="Clear all search parameters and start again"> \
                                    <span class="glyphicon glyphicon-remove"></span> \
                                </button> \
                            </span> ' + field_select + '\
                            <input type="text" class="facetview_freetext form-control input-sm" name="q" value="" placeholder="Search" style="width: 200px" /> \
                            <span class="input-group-btn"> \
                                <button class="btn btn-info facetview_force_search btn-sm"> \
                                    <span class="glyphicon glyphicon-white glyphicon-search"></span> \
                                </button> \
                            </span> \
                        </div> \
                    </div> \
                </form> \
            </div> \
        </div>';

        return searchopts;
    }

    function customPager(options) {
        /*****************************************
         * overrides must provide the following classes and ids
         *
         * class: facetview_decrement - anchor to move the page back
         * class: facetview_increment - anchor to move the page forward
         * class: facetview_inactive_link - for links which should not have any effect (helpful for styling bootstrap lists without adding click features)
         *
         * should (not must) respect the config
         *
         * options.from - record number results start from (may be a string)
         * options.page_size - number of results per page
         * options.data.found - the total number of records in the search result set
         */

        // ensure our starting points are integers, then we can do maths on them
        var from = parseInt(options.from);
        var size = parseInt(options.page_size);

        // calculate the human readable values we want
        var to = from + size;
        from = from + 1; // zero indexed
        if (options.data.found < to) { to = options.data.found }
        var total = options.data.found;
        total = total.toLocaleString();

        var backlink = '<a alt="previous" title="Previous results page" class="facetview_decrement pull-right" style="color:#333; cursor: pointer; font-size: 16px"><span class="glyphicon glyphicon-arrow-left"></span></a>';
        if (from < size) {
            backlink = '<a class="facetview_decrement facetview_inactive_link" style="color:#333">&nbsp;</a>'
        }

        var nextlink = '<a alt="next" title="Next results page" class="facetview_increment pull-left" style="color:#333; cursor: pointer; font-size: 16px"><span class="glyphicon glyphicon-arrow-right"></span></a>';
        if (options.data.found <= to) {
            nextlink = '<a class="facetview_increment facetview_inactive_link" style="color:#333">&nbsp;</a>'
        }

        var meta = '<div class="row" style="font-size: 16px">';
        meta += '<div class="col-md-1">' + backlink + '</div>';
        meta += '<div class="col-md-10 text-center"><p style="font-weight: bold; text-align: center">' + from + ' &ndash; ' + to + ' of ' + total + '</p></div>';
        meta += '<div class="col-md-1">' + nextlink + '</div>';

        return meta
    }

    function scoreView(options, record) {
        var score = octopus.service.newScore({raw: record});

        // outer container for display
        var result = "";

        result += "<div class='score-result'>";
        result += "<div class='row'>";

        // left-hand container for metadata
        result += "<div class='col-md-9'>";

        // journal name
        // FIXME: requires link to full score page
        result += "<strong style='font-size: 150%'>" + score.get_field("journal_name") + "</strong><br>";

        // issns
        var issns = score.get_field("issn");
        var eissns = score.get_field("eissn");

        if (issns.length > 0 || eissns.length > 0) {
            result += "ISSN ";
            if (issns.length > 0) {
                result += issns.join(", ") + " (Print)";
            }
            if (eissns.length > 0) {
                if (issns.length > 0) {
                    result += "; "
                }
                result += eissns.join(", ") + "(Online)";
            }
            result += "<br>";
        }

        // publisher
        result += "<em>" + score.get_field("publisher") + "</em><br>";

        // close the left-hand container
        result += "</div>";

        // right-of-middle container for score information
        result += "<div class='col-md-1'>";

        // the total score as a big highlight number
        // round the score down to the nearest 10
        var nearest_ten = Math.floor(score.get_field("total") / 10) * 10;
        result += '<strong class="score-above-' + nearest_ten + '" style="font-size: 300%">' + score.get_field("total") + '</strong><br>';

        // close the right-of-middle container
        result += "</div>";

        // right-hand container for links out
        result += "<div class='col-md-2'>";

        result += '<a href="/score/' + score.score_id() + '" class="btn btn-info pull-right" style="margin-top: 15px"><span class="glyphicon glyphicon-stats"></span> Full Score</a>';

        // close right-hand container
        result += "</div>";

        // close the outer container
        result += "</div></div>";
        return result;
    }


    function customRangeFacet(facet, options) {
        /*****************************************
         * overrides must provide the following classes and ids
         *
         * id: facetview_filter_<safe filtername> - table for the specific filter
         *
         * each anchor must also have href="<filtername>"
         */

        var filterTmpl = '<div id="facetview_filter_{{FILTER_NAME}}" class="facetview_filters" data-href="{{FILTER_EXACT}}"> \
            <div class="row"> \
                <div class="col-md-12"> \
                    <strong>{{FILTER_DISPLAY}}</strong> \
                </div> \
            </div>\
         </div>';

        // full template for the facet - we'll then go on and do some find and replace
        /*
        var filterTmpl = '<table id="facetview_filter_{{FILTER_NAME}}" class="facetview_filters table table-bordered table-condensed table-striped" data-href="{{FILTER_EXACT}}"> \
            <tr><td><a class="facetview_filtershow" title="filter by {{FILTER_DISPLAY}}" \
            style="color:#333; font-weight:bold;" href="{{FILTER_EXACT}}"><i class="glyphicon glyphicon-plus"></i> {{FILTER_DISPLAY}} \
            </a> \
            </td></tr> \
            </table>';
        */

        // put the name of the field into FILTER_NAME and FILTER_EXACT
        filterTmpl = filterTmpl.replace(/{{FILTER_NAME}}/g, safeId(facet['field'])).replace(/{{FILTER_EXACT}}/g, facet['field']);

        // set the display name of the facet in FILTER_DISPLAY
        if ('display' in facet) {
            filterTmpl = filterTmpl.replace(/{{FILTER_DISPLAY}}/g, facet['display']);
        } else {
            filterTmpl = filterTmpl.replace(/{{FILTER_DISPLAY}}/g, facet['field']);
        }

        return filterTmpl
    }

    function customRangeFacetValues(options, facet) {
        /*****************************************
         * overrides must provide the following classes and ids
         *
         * class: facetview_filtervalue - wrapper element for any value included in the list
         * class: facetview_filterselected - for any anchors around selected filters
         * class: facetview_clear - for any link which should remove a filter (must also provide data-field and data-value)
         * class: facetview_filterchoice - tags the anchor wrapped around the name of the (unselected) field
         *
         * should (not must) respect the following config
         *
         * options.selected_filters_in_facet - whether to show selected filters in the facet pull-down (if that's your idiom)
         * options.render_facet_result - function which renders the individual facets
         */

        function getValueForRange(range, values) {
            for (var i=0; i < values.length; i=i+1) {
                var value = values[i];

                // the "to"s match if they both value and range have a "to" and they are the same, or if neither have a "to"
                var match_to = (value.to && range.to && value.to === range.to) || (!value.to && !range.to);

                // the "from"s match if they both value and range have a "from" and they are the same, or if neither have a "from"
                var match_from = (value.from && range.from && value.from === range.from) || (!value.from && !range.from);

                if (match_to && match_from) {
                    return value
                }
            }
        }

        function getRangeForValue(value, facet) {
            for (var i=0; i < facet.range.length; i=i+1) {
                var range = facet.range[i];

                // the "to"s match if they both value and range have a "to" and they are the same, or if neither have a "to"
                var match_to = (value.to && range.to && value.to === range.to.toString()) || (!value.to && !range.to);

                // the "from"s match if they both value and range have a "from" and they are the same, or if neither have a "from"
                var match_from = (value.from && range.from && value.from === range.from.toString()) || (!value.from && !range.from);

                if (match_to && match_from) {
                    return range
                }
            }
        }

        var selected_range = options.active_filters[facet.field];
        var frag = "";

        // render the active filter if there is one
        if (options.selected_filters_in_facet && selected_range) {
            var range = getRangeForValue(selected_range, facet);
            already_selected = true;

            var data_to = range.to ? " data-to='" + range.to + "' " : "";
            var data_from = range.from ? " data-from='" + range.from + "' " : "";

            var remove = '<a class="facetview_filterselected facetview_clear" data-field="' + facet.field + '" ' + data_to + data_from + ' href="#"><i class="glyphicon glyphicon-black glyphicon-remove" style="margin-top:1px;"></i></a>';

            var sf = '<div class="row facetview_filtervalue"> \
                <div class="col-md-12"> \
                    <em style="padding-left: 10px">' + range.display + '</em> ' + remove + ' \
                </div> \
            </div>';

            /*
            var sf = '<tr class="facetview_filtervalue" style="display:none;"><td>';
            sf += "<strong>" + range.display + "</strong> ";
            sf += '<a class="facetview_filterselected facetview_clear" data-field="' + facet.field + '" ' + data_to + data_from + ' href="#"><i class="glyphicon glyphicon-black glyphicon-remove" style="margin-top:1px;"></i></a>';
            sf += "</td></tr>";
            */

            frag += sf;

            // if a range is already selected, we don't render any more
            return frag
        }

        // then render the remaining selectable facets if necessary
        for (var i=0; i < facet["range"].length; i=i+1) {
            var r = facet["range"][i];
            var f = getValueForRange(r, facet["values"]);
            if (f) {
                if (f.count === 0 && facet.hide_empty_range) {
                    continue
                }
                var append = options.render_range_facet_result(options, facet, f, r);
                frag += append
            }
        }

        return frag
    }

    function customRangeFacetResult(options, facet, result, range) {
        /*****************************************
         * overrides must provide the following classes and ids
         *
         * class: facetview_filtervalue - tags the top level element as being a facet result
         * class: facetview_filterchoice - tags the anchor wrapped around the name of the field
         */
        var data_to = range.to ? " data-to='" + range.to + "' " : "";
        var data_from = range.from ? " data-from='" + range.from + "' " : "";

        var link = '<a style="padding-left: 10px" class="facetview_filterchoice' +
                    '" data-field="' + facet['field'] + '" ' + data_to + data_from + ' href="#"><span class="facetview_filterchoice_text" dir="auto">' + range.display + '</span>' +
                    '<span class="facetview_filterchoice_count" dir="ltr"> (' + result.count + ')</span></a>';

        var append = '<div class="row facetview_filtervalue"> \
            <div class="col-md-12"> \
                ' + link + ' \
            </div> \
        </div>';

        /*
        var append = '<tr class="facetview_filtervalue" style="display:none;"><td><a class="facetview_filterchoice' +
                    '" data-field="' + facet['field'] + '" ' + data_to + data_from + ' href="#"><span class="facetview_filterchoice_text" dir="auto">' + range.display + '</span>' +
                    '<span class="facetview_filterchoice_count" dir="ltr"> (' + result.count + ')</span></a></td></tr>';
        */

        return append
    }

    function customNotFound() {
        /*****************************************
         * overrides must provide the following classes and ids
         *
         * class: facetview_not_found - the id of the top level element containing the not found message
         */
        return '<div class="row">' +
            '<div class="col-md-12">' +
            '<div class="facetview_not_found">Sorry, no journal scores matched your search.  Try modifying your search text, or removing some of your filters.</div>' +
            '</div></div>';
    }


    // set the UI to present the given ordering
    function customSortOrderToggle(options, context, order) {
        if (order === 'asc') {
            $('.facetview_order', context).html('sort <i class="glyphicon glyphicon-arrow-up"></i> by');
            $('.facetview_order', context).attr('href','asc');
            $('.facetview_order', context).attr('title','Current order ascending. Click to change to descending');
        } else {
            $('.facetview_order', context).html('sort <i class="glyphicon glyphicon-arrow-down"></i> by');
            $('.facetview_order', context).attr('href','desc');
            $('.facetview_order', context).attr('title','Current order descending. Click to change to ascending');
        }
    }

    var facets = [];
    // facets.push({'field': 'journal.publisher.exact', 'display': 'Publisher'});
    facets.push({
        field: "total",
        display: "Total Score",
        type: "range",
        open: true,
        hide_inactive: true,
        range : [
            {"from" : 23, "display" : "Trying"},
            {"from" : 47, "display" : "Good"},
            {"from" : 70, "display" : "Very Good"},
            {"from" : 100, "display" : "Amazing"}
        ]
    });
    facets.push({
        field: "reader_rights.score",
        display: "Reader Rights Score",
        type: "range",
        open: true,
        hide_inactive: true,
        range : [
            {"from" : 5, "display" : "Trying"},
            {"from" : 12, "display" : "Good"},
            {"from" : 16, "display" : "Very Good"},
            {"from" : 20, "display" : "Amazing"}
        ]
    });
    facets.push({
        field: "reuse_rights.score",
        display: "Reuse Rights Score",
        type: "range",
        open: true,
        hide_inactive: true,
        range : [
            {"from" : 4, "display" : "Trying"},
            {"from" : 7, "display" : "Good"},
            {"from" : 14, "display" : "Very Good"},
            {"from" : 20, "display" : "Amazing"}
        ]
    });
    facets.push({
        field: "copyrights.score",
        display: "Copyrights Score",
        type: "range",
        open: true,
        hide_inactive: true,
        range : [
            // {"from" : 4, "display" : "Trying"},
            {"from" : 4, "display" : "Good"},
            {"from" : 10, "display" : "Very Good"},
            {"from" : 16, "display" : "Amazing"}
        ]
    });
    facets.push({
        field: "author_posting_rights.score",
        display: "Author Posting Rights Score",
        type: "range",
        open: true,
        hide_inactive: true,
        range : [
            {"from" : 4, "display" : "Trying"},
            {"from" : 6, "display" : "Good"},
            {"from" : 10, "display" : "Very Good"},
            {"from" : 16, "display" : "Amazing"}
        ]
    });
    facets.push({
        field: "automatic_posting_rights.score",
        display: "Automatic Posting Rights Score",
        type: "range",
        open: true,
        hide_inactive: true,
        range : [
            {"from" : 2, "display" : "Trying"},
            {"from" : 4, "display" : "Good"},
            {"from" : 8, "display" : "Very Good"},
            {"from" : 12, "display" : "Amazing"}
        ]
    });
    facets.push({
        field: "machine_readability.score",
        display: "Machine Readability Score",
        type: "range",
        open: true,
        hide_inactive: true,
        range : [
            {"from" : 4, "display" : "Trying"},
            {"from" : 8, "display" : "Good"},
            {"from" : 12, "display" : "Very Good"},
            {"from" : 16, "display" : "Amazing"}
        ]
    });

    $('#publicsearch').facetview({
        // basic settings
        debug: false,
        sharesave_link: false,

        // custom renderers
        render_the_facetview: customFacetview,
        render_search_options: customSearchOptions,
        render_results_metadata: customPager,
        render_result_record : scoreView,
        render_range_facet : customRangeFacet,
        render_range_facet_values : customRangeFacetValues,
        render_range_facet_result : customRangeFacetResult,
        render_not_found: customNotFound,

        // custom behaviour plugins
        behaviour_results_ordering : customSortOrderToggle,

        // search configuration
        search_url : octopus.config.query_endpoint,
        page_size : 10,
        facets : facets,
        search_sortby : [
            {"display" : "Total Score", "field" : "total"},
            {'display':'Journal Name','field':'journal.name.exact'},
            {'display':'Publisher','field':'journal.publisher.exact'},
            {"display" : "Reader Rights Score", "field" : "reader_rights.score"},
            {"display" : "Reuse Rights Score", "field" : "reader_rights.score"},
            {"display" : "Copyrights Score", "field" : "reader_rights.score"},
            {"display" : "Author Posting Rights Score", "field" : "reader_rights.score"},
            {"display" : "Automatic Posting Rights Score", "field" : "reader_rights.score"},
            {"display" : "Machine Readability Score", "field" : "reader_rights.score"}
        ],
        searchbox_fieldselect : [
            {'display':'Publisher','field':'journal.publisher'},
            {'display':'Journal Name','field':'journal.name'},
            {"display" : "ISSN", "field" : "ISSN"}
        ],
        sort : [ {"total" : {"order" : "desc"}} ]
    });

});
