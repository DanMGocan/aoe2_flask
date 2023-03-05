$(function () {
    let availableTags = [
        "unit_1",
        "unit_2",
        "unit_3",
        "unit_4",
        "unit_5"
    ];

    $("#unit_name").autocomplete({
        source: availableTags
    });
});