/**
 * Created by brunopiaggio on 4/17/20.
 */

function color(red, green, blue) {
    $.ajax({
        method: "POST",
        url: "/command",
        contentType: "application/json",
        data: JSON.stringify({
            action: "color",
            red: red,
            green: green,
            blue: blue }),
        statusCode: {
            403: function () {
                window.location = "/login"
            }
        }
    });
}


function effect(effect_name) {
    $.ajax({
        method: "POST",
        url: "/command",
        contentType: "application/json",
        data: JSON.stringify({
            action: "effect",
            name: effect_name }),
        statusCode: {
            403: function () {
                window.location = "/login"
            }
        }
    });
}