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
    $("tr:odd").addClass("odd");
    $("#query").focus();

});

function submitForm(form) {
    $('#search-form').submit();
}
