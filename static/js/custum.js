$( document ).ready(function() {
    if ($("#search-option").val() == 'exactWord') {
        console.log('exactWord');
        radiobtn = document.getElementById("radio1");
        radiobtn.checked = true;
    } else if ($("#search-option").val() == 'startsWith') {
        console.log('startsWith');
        radiobtn = document.getElementById("radio2");
        radiobtn.checked = true;
    } else if ($("#search-option").val() == 'contains') {
        console.log('contains');
        radiobtn = document.getElementById("radio3");
        radiobtn.checked = true;
    }
    $("tr:odd").addClass("odd");
    $("#query").focus();
});

function submitForm(form) {
    $('#search-form').submit();
}
