from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load('model_lg.pkl')
scaler = joblib.load('scaler_lg.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Read inputs from form 
    age = float(request.form['age'])
    sex = float(request.form['sex'])
    cp = float(request.form['cp'])
    trestbps = float(request.form['trestbps'])
    chol = float(request.form['chol'])
    fbs = float(request.form['fbs'])
    restecg = float(request.form['restecg'])  
    thalach = float(request.form['thalach'])   
    exang = float(request.form['exang']) 
    oldpeak = float(request.form['oldpeak'])
    slope = float(request.form['slope'])
    ca = float(request.form['ca'])
    thal = float(request.form['thal'])

    # --- scale only continuous features ---
    continuous_features = np.array([[age, trestbps, chol, thalach, oldpeak]])
    scaled_continuous = scaler.transform(continuous_features)

    # --- reconstruct in exact training order ---
    final_features = np.array([[
        scaled_continuous[0][0],  # age
        sex,                      # sex
        cp,                       # cp
        scaled_continuous[0][1],  # trestbps
        scaled_continuous[0][2],  # chol
        fbs,                      # fbs
        restecg,                  # restecg
        scaled_continuous[0][3],  # thalach
        exang,                    # exang
        scaled_continuous[0][4],  # oldpeak
        slope,                    # slope
        ca,                       # ca
        thal                      # thal
    ]])

    # Predict
    prediction = model.predict(final_features)
    pred_value = int(prediction[0])  # class (0 or 1)
    
    # Prepare message
    if pred_value == 0:
        message = "No Heart Disease Detected ✅"
    else:
        message = "Heart Disease Detected ⚠️"

    return render_template(
        'index.html',
        prediction_text=message,
        prediction_value=pred_value
    )

if __name__ == '__main__':
    app.run(debug=True)

