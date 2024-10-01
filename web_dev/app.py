from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper

#create Flask instance
app = Flask(__name__)
app.config[] = 0

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

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau2.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    sex = content["Sex"]
    age = float(content["age"])
    BMI = float(content["BMI"])
    High_Blood_Pressure = content["HighBP"]
    High_Cholesterol = content["HighChol"]
    Cholesterol_Check = content["CholCheck"]
    Heavy_Alcohol_Consumption = content["HeavyAlcoholComsup"]
    Stroke = content["Stroke"]
    Heart_Disease_or_Attack_History = content["HeartDiseaseorAttack"]
    General_Health = content["GenHlth"]
    Physical_Health = ["PhysHlth"]

    


    preds = modelHelper.makePredictions(sex, age, BMI, High_Blood_Pressure, High_Cholesterol, Cholesterol_Check, Heavy_Alcohol_Consumption, Stroke, Heart_Disease_or_Attack_History, General_Health, Physical_Health)
    return(jsonify({"ok": True, "prediction": str(preds)}))


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
