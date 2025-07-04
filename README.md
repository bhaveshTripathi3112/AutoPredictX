# AutoPredictX

AutoPredictX is a web-based application for predicting the resale value of used cars in India using machine learning. It provides a user-friendly interface for car sellers or buyers to estimate the fair resale price based on key vehicle attributes.

## Features

- **Fast Resale Price Prediction:** Enter car features (brand, model, age, kilometers driven, etc.) and get an instant estimated resale value.
- **Modern Web Interface:** Simple form for input, real-time result display.
- **Machine Learning Model:** Utilizes a Random Forest Regressor trained on real car data.
- **Flexible Tech Stack:** Python (Flask) backend, scikit-learn model, and a responsive HTML/JS/CSS frontend.

## How It Works

1. The user fills out the form with car details (brand, model, age, km driven, seller/fuel/transmission type, mileage, engine, power, seats).
2. The frontend sends this data as JSON to the Flask backend.
3. The backend encodes features, runs the trained model, and returns the predicted price.
4. The UI displays the predicted resale value.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/bhaveshTripathi3112/AutoPredictX.git
cd AutoPredictX
```

### 2. Set Up the Backend

- Install requirements:

  ```bash
  cd backend
  pip install -r requirements.txt
  ```

- Make sure the trained model and all encoder `.pkl` files are in the `model/` directory (see below for training your own).

### 3. Set Up the Model (Optional: for retraining)

- Go to the `model/` directory:

  ```bash
  cd ../model
  pip install -r requirements.txt
  ```

- To retrain the model, place your dataset as `dataset.csv` and run:

  ```bash
  python train_model.py
  ```

- This will generate `car_price_model.pkl`, along with encoder files.

### 4. Run the Application

From the `backend` directory:

```bash
python app.py
```

By default, the app runs on `http://127.0.0.1:5000/`. Open this in your browser.

### 5. Usage

- Fill out the fields in the web form and click "Predict Price."
- The estimated resale value will appear below the form.

## Project Structure

```
AutoPredictX/
│
├── backend/
│   ├── app.py                # Flask backend serving model and API
│   └── requirements.txt
│
├── frontend/
│   ├── static/
│   │   ├── script.js         # Frontend JS logic
│   │   └── style.css         # Styling
│   └── templates/
│       └── index.html        # Main web page
│
├── model/
│   ├── train_model.py        # Model training script
│   ├── requirements.txt
│   └── (model and encoder .pkl files)
│
└── README.md                 # This file
```

## Dependencies

- Python 3.8+
- Flask, joblib, numpy, scikit-learn, pandas (see respective `requirements.txt` for full details)
- Frontend: HTML, CSS, JavaScript

## License

*Please specify your license here if applicable.*

## Author

[bhaveshTripathi3112](https://github.com/bhaveshTripathi3112)

---

*AutoPredictX makes car resale pricing transparent and accessible for everyone.*
