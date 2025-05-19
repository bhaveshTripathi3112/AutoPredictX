import os
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Set up Flask app
app = Flask(
    __name__,
    template_folder='../frontend/templates',
    static_folder='../frontend/static'
)

# Load model and encoders
MODEL_DIR = '../model'
model = joblib.load(os.path.join(MODEL_DIR, 'car_price_model.pkl'))
brand_encoder = joblib.load(os.path.join(MODEL_DIR, 'brand_encoder.pkl'))
model_encoder = joblib.load(os.path.join(MODEL_DIR, 'model_encoder.pkl'))
seller_encoder = joblib.load(os.path.join(MODEL_DIR, 'seller_type_encoder.pkl'))
fuel_encoder = joblib.load(os.path.join(MODEL_DIR, 'fuel_type_encoder.pkl'))
transmission_encoder = joblib.load(os.path.join(MODEL_DIR, 'transmission_type_encoder.pkl'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        # Extract and encode features
        brand = brand_encoder.transform([data['brand']])[0]
        model_name = model_encoder.transform([data['model']])[0]
        vehicle_age = float(data['vehicle_age'])
        km_driven = float(data['km_driven'])
        seller_type = seller_encoder.transform([data['seller_type']])[0]
        fuel_type = fuel_encoder.transform([data['fuel_type']])[0]
        transmission = transmission_encoder.transform([data['transmission_type']])[0]
        mileage = float(data['mileage'])
        engine = float(data['engine'])
        max_power = float(data['max_power'])
        seats = float(data['seats'])

        # Arrange features as per training
        features = np.array([[vehicle_age, km_driven, mileage, engine, max_power, seats,
                              fuel_type, transmission, seller_type, brand, model_name]])
        pred = model.predict(features)[0]
        return jsonify({'prediction': int(pred)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
