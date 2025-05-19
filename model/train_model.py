import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load dataset
columns = [
    'id', 'name', 'brand', 'model', 'vehicle_age', 'km_driven', 'seller_type',
    'fuel_type', 'transmission_type', 'mileage', 'engine', 'max_power', 'seats', 'selling_price'
]

df = pd.read_csv('dataset.csv', names=columns, header=None)

# Data Cleaning
numeric_cols = ['vehicle_age', 'km_driven', 'mileage', 'engine', 'max_power', 'seats', 'selling_price']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Handle missing values
df.dropna(subset=numeric_cols, inplace=True)

# Encode categorical features
categorical_cols = ['fuel_type', 'transmission_type', 'seller_type', 'brand', 'model']
encoders = {col: LabelEncoder() for col in categorical_cols}

for col in categorical_cols:
    df[col] = df[col].fillna('Unknown')
    df[f'{col}_enc'] = encoders[col].fit_transform(df[col])

# Feature selection
features = [
    'vehicle_age', 'km_driven', 'mileage', 'engine', 'max_power', 'seats',
    'fuel_type_enc', 'transmission_type_enc', 'seller_type_enc', 'brand_enc', 'model_enc'
]
X = df[features]
y = df['selling_price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    min_samples_leaf=2,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print(f'MSE: {mean_squared_error(y_test, predictions):.2f}')
print(f'R² Score: {r2_score(y_test, predictions):.2f}')

# Save model and encoders
joblib.dump(model, 'car_price_model.pkl')
for col in categorical_cols:
    joblib.dump(encoders[col], f'{col}_encoder.pkl')

# Example prediction
sample = X_test.iloc[0:1]
print(f"\nSample Prediction: {model.predict(sample)[0]:,.2f} INR")
