from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from datetime import datetime
import pandas as pd


def predict_future_rates(historical_data, target_currency, prediction_date_str):
    # Convert prediction_date_str to datetime object if it's not already
    if isinstance(prediction_date_str, str):
        prediction_date = datetime.strptime(prediction_date_str, "%Y-%m-%d")
    else:
        prediction_date = prediction_date_str

    target_data = historical_data[historical_data["currency"] == target_currency]

    if len(target_data) < 2:
        raise ValueError(f"Not enough historical data available for {target_currency}")

    X = np.arange(len(target_data)).reshape(-1, 1)
    y_buy = target_data["buy"]
    y_sell = target_data["sell"]

    model_buy = LinearRegression()
    model_buy.fit(X, y_buy)

    model_sell = LinearRegression()
    model_sell.fit(X, y_sell)

    # Predict future rates for the prediction_date
    days_since_start = (
        prediction_date - pd.to_datetime(target_data["date"]).min()
    ).days
    future_buy_rate = model_buy.predict([[days_since_start]])[0]
    future_sell_rate = model_sell.predict([[days_since_start]])[0]

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.scatter(X, y_buy, color="blue", label="Actual Buy Rates")
    plt.plot(X, model_buy.predict(X), color="red", label="Predicted Buy Rates")
    plt.xlabel("Days")
    plt.ylabel("Buy Rate")
    plt.title(f"Linear Regression Prediction - Buy Rate ({target_currency})")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.scatter(X, y_sell, color="green", label="Actual Sell Rates")
    plt.plot(X, model_sell.predict(X), color="orange", label="Predicted Sell Rates")
    plt.xlabel("Days")
    plt.ylabel("Sell Rate")
    plt.title(f"Linear Regression Prediction - Sell Rate ({target_currency})")
    plt.legend()

    # Save plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
    plt.close()

    return future_buy_rate, future_sell_rate, plot_data
