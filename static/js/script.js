/*
    jQuery for MaterializeCSS initialization
*/
$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    $("#alert-close").click(function () {
    $("#form-alert").hide("fade");
    });

    // Auto close flash messages
    $(function() { setTimeout(function() { 
    $("#form-alert").hide(1000) }, 2000); });
  

    // Stop form icons from changing color when inputs are clicked
    $("input").on("click", function () {
        $("i").css("color", "black");
    });
    
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        // Create variable for green underline (valid selection)
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        // Create variable for red underline (not valid selection)
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        // If the validate property is required then show required message on DOM
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        // Apply event handler to add our valid seletion class to change border css style to green
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                // If user exits the select without a valid slection apply our not valid
                // selection class to change border css style to red
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});