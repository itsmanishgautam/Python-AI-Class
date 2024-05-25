import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

# Load and preprocess data
data = pd.read_csv('construction_data.csv')
data.fillna(method='ffill', inplace=True)

# Feature selection
features = ['material_cost', 'labor_rate', 'project_size', 'location']
X = data[features]
y = data['total_cost']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Save the model
import joblib
joblib.dump(model, 'cost_prediction_model.pkl')

# Dashboard Integration (Pseudo-code)
# Assuming we have a Flask app for the dashboard
from flask import Flask, request, jsonify

app = Flask(__name__)
model = joblib.load('cost_prediction_model.pkl')

@app.route('/predict_cost', methods=['POST'])
def predict_cost():
    input_data = request.json
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return jsonify({'predicted_cost': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
