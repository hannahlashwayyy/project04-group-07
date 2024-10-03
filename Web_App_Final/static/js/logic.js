$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        console.log("Button Clicked")
        makePredictions();
    });
});




// call Flask API endpoint
function makePredictions() {
    var HighBP = $("#HighBP").val();
    var HighChol = $("#HighChol").val();
    var CholCheck = $("#CholCheck").val();
    var BMI = $("#BMI").val();
    var Stroke = $("#Stroke").val();
    var HeartDiseaseorAttack = $("#HeartDiseaseorAttack").val();
    var HeavyAlcoholConsump = $("#HeavyAlcoholConsump").val();
    var GenHlth = $("#GenHlth").val();
    var PhysHlth = $("#PhysHlth").val();
    var DiffWalk = $("#DiffWalk").val();
    var Sex = $("#Sex").val();
    var Age = $("#age").val();


    // check if inputs are valid

    // create the payload
    var payload = {
        "HighBP": HighBP,
        "HighChol": HighChol,
        "CholCheck": CholCheck,
        "BMI": BMI,
        "Stroke": Stroke,
        "HeartDiseaseorAttack": HeartDiseaseorAttack,
        "HeavyAlcoholConsump": HeavyAlcoholConsump,
        "GenHlth": GenHlth,
        "PhysHlth": PhysHlth,
        "DiffWalk": DiffWalk,
        "Sex": Sex,
        "age": Age
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(payload),  // Send the payload directly as raw JSON
        success: function(returnedData) {
            console.log(returnedData);

            $("#output").text(`Your predicted risk for diabetes is ${Math.round(100 * parseFloat(returnedData["prediction"]), 2)}%`);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });
}