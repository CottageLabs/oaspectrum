jQuery(document).ready(function($) {

    // when the update button is clicked, disable it and show the waiting gif
    $("#upload").click(function(event) {
        event.preventDefault();
        $("#upload").attr("disabled", "disabled")
                    .html("Uploading <img src='/static/images/white-transparent-loader.gif'>");
        $("#upload-form").submit();
    });

});

