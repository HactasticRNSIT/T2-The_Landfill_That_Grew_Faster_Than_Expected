import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv("landfill_data.csv")

X = data[[
    "population",
    "waste_generated",
    "recycling_rate",
    "rainfall",
    "urban_growth"
]]

y = data["landfill_growth"]

model = LinearRegression()
model.fit(X, y)

def predict_growth(values):

    prediction = model.predict(np.array([values]))

    return round(prediction[0], 2)