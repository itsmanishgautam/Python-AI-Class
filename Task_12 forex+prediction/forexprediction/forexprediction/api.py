import requests
from datetime import datetime, timedelta
import pandas as pd

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
