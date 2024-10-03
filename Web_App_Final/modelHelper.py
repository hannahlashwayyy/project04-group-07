import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, sex, age, BMI, High_Blood_Pressure, High_Cholesterol, Cholesterol_Check, Heavy_Alcohol_Consumption, Stroke, Heart_Disease_or_Attack_History, General_Health, Physical_Health, Difficulty_Walking):

        # create dataframe of one row for inference
        df = pd.DataFrame()
        df["HighBP"] = [High_Blood_Pressure]
        df["HighChol"] = [High_Cholesterol]
        df["CholCheck"] = [Cholesterol_Check]
        df["BMI"] = [BMI]
        df["Stroke"] = [Stroke]
        df["HeartDiseaseorAttack"] = [Heart_Disease_or_Attack_History]
        df["HvyAlcoholConsump"] = [Heavy_Alcohol_Consumption]
        df["GenHlth"] = [General_Health]
        df["PhysHlth"] = [Physical_Health]
        df["DiffWalk"] = [Difficulty_Walking]
        df["Sex"] = [sex]
        df["Age"] = [age]

         #scaler
        scaler = pickle.load(open("diabetes_scaler_ada.h5", 'rb'))
        scaled_data = scaler.transform(df.loc[:, ["BMI", "PhysHlth"]])
        df_scaled = pd.DataFrame(scaled_data, columns=["BMI", "PhysHlth"])

        #replace
        df["BMI"] = df_scaled.BMI
        df["PhysHlth"] = df_scaled.PhysHlth

        # Re-arrange columns
        df = df.loc[:, ['HighBP', 'HighChol', 'CholCheck', 'Stroke',
       'HeartDiseaseorAttack', 'HvyAlcoholConsump', 'DiffWalk', 'Sex', 'BMI',
       'PhysHlth', 'GenHlth', 'Age']]

        # model
        model = pickle.load(open("diabetes_model_ada.h5", 'rb'))


        preds = model.predict_proba(df)
        return(preds[0][1])









