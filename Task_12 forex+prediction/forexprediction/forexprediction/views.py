from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from .api import fetch_historical_forex_data
from .prediction import predict_future_rates

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
