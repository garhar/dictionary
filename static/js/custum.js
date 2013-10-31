$( document ).ready(function() {

    if ($("#search-option").val() == 1) {
        $("#exactWord").removeClass('active');
        $("#startsWith").addClass('active');
    } else if ($("#search-option").val() == 2) {
        $("#exactWord").removeClass('active');
        $("#containsString").addClass('active');
    }

    $(".btn-toolbar button").click(function () {
        $("#search-option").val($(this).val());
    });
    $("#query").focus();
});

function submitForm(form) {
    $('#search-form').submit();
}

//var clip = new ZeroClipboard( document.getElementById("copy-button"), {
//    moviePath: "/static/flash/ZeroClipboard.swf"
//} );
//
//clip.on( "load", function(client) {
//    alert( "movie is loaded" );
//
//    client.on( "complete", function(client, args) {
//        alert('test');
//        this.style.display = "none";
//        alert("Copied text to clipboard: " + args.text );
//    } );
//} );
//
//function setupClipboard(element, counter) {
//    alert('test clip...');
//}