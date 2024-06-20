from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import requests
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Function to fetch historical forex data from API
def fetch_historical_forex_data(start_date, end_date):
    base_url = "https://www.nrb.org.np/api/forex/v1/"
    endpoint = "rates"
    url = f"{base_url}{endpoint}"

    historical_data = []

    current_date = start_date
    while current_date <= end_date:
        params = {
            "page": 1,
            "per_page": 1,
            "from": current_date.strftime("%Y-%m-%d"),
            "to": current_date.strftime("%Y-%m-%d")
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            forex_data = response.json()
            payload = forex_data['data']['payload'][0]
            rates = payload['rates']
            for rate in rates:
                historical_data.append({
                    'date': payload['date'],
                    'currency': rate['currency']['iso3'],
                    'buy': rate['buy'],
                    'sell': rate['sell']
                })
        else:
            print(f"Failed to fetch data for {current_date.strftime('%Y-%m-%d')}")

        current_date += timedelta(days=1)

    return pd.DataFrame(historical_data)

# Function to predict future rates for a given currency
def predict_future_rates(historical_data, target_currency, prediction_date):
    target_data = historical_data[historical_data['currency'] == target_currency]

    if len(target_data) < 2:
        raise ValueError(f"Not enough historical data available for {target_currency}")

    X = np.arange(len(target_data)).reshape(-1, 1)
    y_buy = target_data['buy']
    y_sell = target_data['sell']

    model_buy = LinearRegression()
    model_buy.fit(X, y_buy)

    model_sell = LinearRegression()
    model_sell.fit(X, y_sell)

    # Predict future rates for the prediction_date
    days_since_start = (prediction_date - target_data['date'].min()).days
    future_buy_rate = model_buy.predict([[days_since_start]])[0]
    future_sell_rate = model_sell.predict([[days_since_start]])[0]

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.scatter(X, y_buy, color='blue', label='Actual Buy Rates')
    plt.plot(X, model_buy.predict(X), color='red', label='Predicted Buy Rates')
    plt.xlabel('Days')
    plt.ylabel('Buy Rate')
    plt.title(f'Linear Regression Prediction - Buy Rate ({target_currency})')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.scatter(X, y_sell, color='green', label='Actual Sell Rates')
    plt.plot(X, model_sell.predict(X), color='orange', label='Predicted Sell Rates')
    plt.xlabel('Days')
    plt.ylabel('Sell Rate')
    plt.title(f'Linear Regression Prediction - Sell Rate ({target_currency})')
    plt.legend()

    # Save plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    return future_buy_rate, future_sell_rate, plot_data

# View to handle the index page and form submission
def index(request):
    error_message = ""
    currency = None
    buy_rate = None
    sell_rate = None
    plot_data = None
    predicted_date = None

    if request.method == 'POST':
        currency = request.POST.get('currency', '')
        prediction_date_str = request.POST.get('prediction_date', '')

        try:
            prediction_date = datetime.strptime(prediction_date_str, "%Y-%m-%d")

            # Fetch historical data if not already fetched
            if 'historical_data' not in request.session:
                end_date = datetime.today()
                start_date = end_date - timedelta(days=30)
                historical_df = fetch_historical_forex_data(start_date, end_date)
                request.session['historical_data'] = historical_df.to_json() 
            else:
                historical_df = pd.read_json(request.session['historical_data'])

            if prediction_date < datetime.today():
                target_data = historical_df[(historical_df['date'] == prediction_date_str) & (historical_df['currency'] == currency)]
                if not target_data.empty:
                    buy_rate = round(target_data.iloc[0]['buy'], 2)
                    sell_rate = round(target_data.iloc[0]['sell'], 2)
                else:
                    error_message = f"No historical data available for {currency} on {prediction_date_str}"
            else:
                predicted_buy_rate, predicted_sell_rate, plot_data = predict_future_rates(historical_df, currency, prediction_date)
                buy_rate = round(predicted_buy_rate, 2)
                sell_rate = round(predicted_sell_rate, 2)
                predicted_date = prediction_date_str
        except ValueError as e:
            error_message = str(e)

    context = {
        'error_message': error_message,
        'currency': currency,
        'buy_rate': buy_rate,
        'sell_rate': sell_rate,
        'plot_data': plot_data,
        'predicted_date': predicted_date
    }
    return render(request, 'index.html', context)
