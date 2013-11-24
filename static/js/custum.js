$( document ).ready(function() {
    var radiobtn = null;
    if ($("#option-arg").val() == 'exactWord') {
        console.log('option: exactWord');
        radiobtn = document.getElementById("radio1");
        radiobtn.checked = true;
    } else if ($("#option-arg").val() == 'startsWith') {
        console.log('option: startsWith');
        radiobtn = document.getElementById("radio2");
        radiobtn.checked = true;
    } else if ($("#option-arg").val() == 'contains') {
        console.log('option: contains');
        radiobtn = document.getElementById("radio3");
        radiobtn.checked = true;
    }
    $("tr:odd").addClass("odd");
    $("#query").focus();
});

function submitForm(form) {
    $('#search-form').submit();
}
