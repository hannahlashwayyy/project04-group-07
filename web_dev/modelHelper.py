import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(sex, age, BMI, High_Blood_Pressure, High_Cholesterol, Cholesterol_Check, Heavy_Alcohol_Consumption, Stroke, Heart_Disease_or_Attack_History, General_Health, Physical_Health):
        # create dataframe of one row for inference
        df = pd.DataFrame()
        df["Sex"] = [sex]
        df["Age"] = [age]
        df["BMI"] = [BMI]
        df["High_BP"] = [High_Blood_Pressure]
        df["HighChol"] = [High_Cholesterol]
        df["CHolCheck"] = [Cholesterol_Check]
        df["HvyAlcoholConsump"] = [Heavy_Alcohol_Consumption]
        df["Stroke"] = [Stroke]
        df["HeartDiseaseorAttack"] = [Heart_Disease_or_Attack_History]
        df["GenHlth"] = [General_Health]
        df["HeartDiseaseorAttack"] = [Heart_Disease_or_Attack_History]
        df["PhysHlth"] = [Physical_Health]
      
        

        # model
        model = pickle.load(open("INSERT_PIPELINE_H5_HERE", 'rb'))

        # columns in order
        df = df.loc[:, ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'Sex', 'Age']]

        preds = model.predict_proba(df)
        return(preds[0][1])
