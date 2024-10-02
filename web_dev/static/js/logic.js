$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
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
    var HvyAlcoholConsump = $("#HvyAlcoholConsump").val();
    var GenHlth = $("#GenHlth").val();
    var PhysHlth = $("#PhysHlth").val();
    var DiffWalk = $("#DiffWalk").val();
    var Sex = $("#Sex").val();
    var Age = $("#Age").val();


    // check if inputs are valid

    // create the payload
    var payload = {
        "HighBP": HighBP,
        "HighChol": HighChol,
        "CholCheck": CholCheck,
        "BMI": BMI,
        "Stroke": Stroke,
        "HeartDiseaseorAttack": HeartDiseaseorAttack,
        "HvyAlcoholConsump": HvyAlcoholConsump,
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
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            var prob = parseFloat(returnedData["prediction"]);

            //if (prob > 0.5) {
               // $("#output").text(`You Survived with probability ${prob}!`);
            //} else {
              //  $("#output").text(`You did not survive with probability ${prob}, sorry. :(`);
           // }

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}
