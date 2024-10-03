from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper

#create Flask instance
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper() 

# Route to render index.html template 
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/tableau_hannah")
def tableau_hannah():
    # Return template and data
    return render_template("tableau_hannah.html")

@app.route("/tableau_thripura")
def tableau_thripura():
    # Return template and data
    return render_template("tableau_thripura.html")

@app.route("/works_cited")
def works_cited():
    # Return template and data
    return render_template("works_cited.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    try:
        # Access the raw JSON payload
        content = request.json
        print("Received JSON:", content)

        # Define the required keys
        required_keys = ["Sex", "age", "BMI", "HighBP", "HighChol", "CholCheck",
                 "HeavyAlcoholConsump",  # Match this with the incoming key
                 "Stroke", "HeartDiseaseorAttack", "GenHlth",
                 "PhysHlth", "DiffWalk"]

        # Validate the presence of all required keys in the incoming JSON payload
        for key in required_keys:
            if key not in content:
                return jsonify({"error": f"Missing key: {key}"}), 400

        # parse
        sex = content["Sex"]
        age = float(content["age"])
        BMI = float(content["BMI"])
        High_Blood_Pressure = int(content["HighBP"])
        High_Cholesterol = int(content["HighChol"])
        Cholesterol_Check = int(content["CholCheck"])
        Heavy_Alcohol_Consumption = int(content["HeavyAlcoholConsump"])
        Stroke = int(content["Stroke"])
        Heart_Disease_or_Attack_History = int(content["HeartDiseaseorAttack"])
        General_Health = int(content["GenHlth"])
        Physical_Health = int(content["PhysHlth"])
        Difficulty_Walking = int(content["DiffWalk"])

        # Call the model helper function to make predictions
        preds = modelHelper.makePredictions(sex, age, BMI, High_Blood_Pressure, High_Cholesterol,
                                            Cholesterol_Check, Heavy_Alcohol_Consumption, Stroke,
                                            Heart_Disease_or_Attack_History, General_Health,
                                            Physical_Health, Difficulty_Walking)

        # Return the prediction result as JSON
        return jsonify({"ok": True, "prediction": str(preds)})

    except Exception as e:
        # Log any errors for debugging
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)