from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("backend/loan_model.pkl")


@app.get("/")
def home():
    return {"message": "Loan Prediction API Running ✅"}


@app.post("/predict")
def predict(data: dict):

    # Convert incoming JSON → feature array
    features = np.array(list(data.values())).reshape(1, -1)

    prediction = model.predict(features)

    return {
        "prediction": int(prediction[0])
    }