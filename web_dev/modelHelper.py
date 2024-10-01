import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(sex, age, BMI, High_Blood_Pressure, High_Cholesterol, Cholesterol_Check, Smoker, Stroke, Heart_Disease_or_Attack_History):
        # create dataframe of one row for inference
        df = pd.DataFrame()
        df["Sex"] = [sex]
        df["Age"] = [age]
        df["BMI"] = [BMI]
        df["High_BP"] = [High_Blood_Pressure]
        df["HighChol"] = [High_Cholesterol]
        df["CHolCheck"] = [Cholesterol_Check]
        df["Smoker"] = [Smoker]
        df["Stroke"] = [Stroke]
        df["HeartDiseaseorAttack"] = [Heart_Disease_or_Attack_History]
      
        

        # model
        model = pickle.load(open("INSERT_PIPELINE_H5_HERE", 'rb'))

        # columns in order
        df = df.loc[:, ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'Sex', 'Age']]

        preds = model.predict_proba(df)
        return(preds[0][1])
