from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

FEATURE_ORDER = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

model = load_model("diabetes_model.keras")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    values = [data.get(feature, 0) for feature in FEATURE_ORDER]
    input_array = np.array(values).reshape(1, -1)

    pred = model.predict(input_array)[0]
    prob = model.predict_proba(input_array)[0].tolist() if hasattr(model, "predict_proba") else []

    return jsonify({
        "prediction": int(pred),
        "probability": prob
    })

if __name__ == "__main__":
    app.run(debug=True)

