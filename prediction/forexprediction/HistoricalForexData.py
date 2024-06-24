from datetime import datetime, timedelta
import requests
from currencyprediction.models import HistoricalForexData


def fetch_historical_forex_data_and_save(start_date, end_date):
    base_url = "https://www.nrb.org.np/api/forex/v1/"
    endpoint = "rates"
    url = f"{base_url}{endpoint}"

    current_date = start_date
    while current_date <= end_date:
        params = {
            "page": 1,
            "per_page": 1,
            "from": current_date.strftime("%Y-%m-%d"),
            "to": current_date.strftime("%Y-%m-%d"),
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            forex_data = response.json()
            payload = forex_data["data"]["payload"][0]
            rates = payload["rates"]
            for rate in rates:
                currency_code = rate["currency"]["iso3"]
                buy_rate = rate["buy"]
                sell_rate = rate["sell"]

                # Save data into HistoricalForexData model
                historical_entry, created = HistoricalForexData.objects.get_or_create(
                    date=payload["date"],
                    currency=currency_code,
                    defaults={"buy_rate": buy_rate, "sell_rate": sell_rate},
                )

                if not created:
                    # Update existing entry if needed
                    historical_entry.buy_rate = buy_rate
                    historical_entry.sell_rate = sell_rate
                    historical_entry.save()

        else:
            print(f"Failed to fetch data for {current_date.strftime('%Y-%m-%d')}")

        current_date += timedelta(days=1)
