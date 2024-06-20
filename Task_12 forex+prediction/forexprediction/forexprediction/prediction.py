from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import numpy as np
from .api import fetch_historical_forex_data

def predict_future_rates(historical_data, target_currency):
    # Filter data for the target currency
    target_data = historical_data[historical_data['currency'] == target_currency]

    if len(target_data) < 2:
        raise ValueError(f"Not enough historical data available for {target_currency}")

    # Prepare features (dates as integers for simplicity)
    X = np.arange(len(target_data)).reshape(-1, 1)
    y_buy = target_data['buy']
    y_sell = target_data['sell']

    # Create and train the models for buy and sell rates
    model_buy = LinearRegression()
    model_buy.fit(X, y_buy)

    model_sell = LinearRegression()
    model_sell.fit(X, y_sell)

    # Predict future rates (e.g., next day)
    next_index = len(target_data)
    future_buy_rate = model_buy.predict([[next_index]])[0]
    future_sell_rate = model_sell.predict([[next_index]])[0]

    return future_buy_rate, future_sell_rate

if __name__ == "__main__":
    try:
        # Fetch historical data for the last 30 days
        end_date = datetime.today()
        start_date = end_date - timedelta(days=30)
        historical_df = fetch_historical_forex_data(start_date, end_date)
        while True:
            # Get user input for target currency
            target_currency = input("Enter the target currency (ISO3 code, e.g., USD): ")

            try:
                predicted_buy_rate, predicted_sell_rate = predict_future_rates(historical_df, target_currency)
                next_day = end_date + timedelta(days=1)
                print(f"Predicted future buy rate for {target_currency} on {next_day.strftime('%Y-%m-%d')} is: {predicted_buy_rate}")
                print(f"Predicted future sell rate for {target_currency} on {next_day.strftime('%Y-%m-%d')} is: {predicted_sell_rate}")
            except ValueError as e:
                print(e)

            # Optionally wait before fetching data again (adjust as needed)
            import time
            time.sleep(5)  # Wait for 1 minute before fetching data again

    except KeyboardInterrupt:
        print("Prediction stopped by user.")
