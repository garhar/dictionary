$( document ).ready(function() {

    var radioMode = null;
    if ($("#mode-arg").val() == 'terms') {
        console.log('mode: terms');
        radioMode = document.getElementById("mode1");
        radioMode.checked = true;
    } else if ($("#mode-arg").val() == 'abbr') {
        console.log('mode: abbr');
        radioMode = document.getElementById("mode2");
        radioMode.checked = true;
    }

    var radioOption = null;
    if ($("#option-arg").val() == 'EXACT') {
        console.log('option: exactWord');
        radioOption = document.getElementById("option1");
        radioOption.checked = true;
    } else if ($("#option-arg").val() == 'STARTS_WITH') {
        console.log('option: startsWith');
        radioOption = document.getElementById("option2");
        radioOption.checked = true;
    } else if ($("#option-arg").val() == 'CONTAINS') {
        console.log('option: contains');
        radioOption = document.getElementById("option3");
        radioOption.checked = true;
    }
    $("tr:odd").addClass("odd");
    $("#query").focus();
});

function submitForm(form) {
    $('#search-form').submit();
}
