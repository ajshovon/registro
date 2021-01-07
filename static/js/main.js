$(document).ready(function () {
    $("#add").click(function () {
        $("#add").toggle("fast");
        $("#search_button").toggle("fast");
    });
    $("#cancel_add").click(function () {
        $("#add").toggle("fast");
        $("#search_button").toggle("fast");
    });
    $("#cancel_add2").click(function () {
        $("#add").toggle("fast");
        $("#search_button").toggle("fast");
    });
    $("#search_button").click(function () {
        $("#add").toggle();
        $("#search_id").toggle();
        $("#search_button").toggle();
    });
    $("#cancel_search").click(function () {
        $("#search_id").toggle();
        $("#search_button").toggle();
        $("#add").toggle();   
    });

});