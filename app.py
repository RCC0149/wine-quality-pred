from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)
model = joblib.load('wine_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form values (match feature order)
    features = [
        float(request.form['fixed_acidity']),
        float(request.form['volatile_acidity']),
        float(request.form['citric_acid']),
        float(request.form['residual_sugar']),
        float(request.form['chlorides']),
        float(request.form['free_sulfur_dioxide']),
        float(request.form['total_sulfur_dioxide']),
        float(request.form['density']),
        float(request.form['pH']),
        float(request.form['sulphates']),
        float(request.form['alcohol'])
    ]
    # Scale features
    final_features = scaler.transform(np.array([features]))
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text=f'Predicted Wine Quality (1-10): {prediction[0]}')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)