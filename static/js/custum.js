$( document ).ready(function() {

//    $(".btn-group button").click(function () {
//        $("#search-option").val($(this).val());
//    });

//    if (searchOption == '1') {
//        alert('searchOption == 1');
//        $(".btn-group").toggle();
//    }

    $("#query").focus();
});

function submitForm(form) {
    var active = $('.search-option[class*="active"]').val();
    $('#search-option').val(active);
    $('#search-form').submit();
}

