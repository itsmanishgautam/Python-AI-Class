

import requests

def get_forex_rates(date):
    base_url = "https://www.nrb.org.np/api/forex/v1/"
    endpoint = "rates"
    url = f"{base_url}{endpoint}"

    # Prepare parameters
    params = {
        "page": 1,
        "per_page": 1,
        "from": date,
        "to": date
    }

    # Make request
    response = requests.get(url, params=params)

    # Check for successful response
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error
        print("Error:", response.status_code)
        return None

# Accept user input for the date
date = input("Enter the date (YYYY-MM-DD): ")

forex_data = get_forex_rates(date)
if forex_data:
    # Process the data as needed
    print(forex_data)
else:
    print("Failed to fetch FOREX data.")



# import csv

# # Extract FOREX rates data
# payload = forex_data['data']['payload'][0]
# date = payload['date']
# rates = payload['rates']

# # Define CSV file name
# csv_filename = f"forex_rates_{date}.csv"

# # Write FOREX rates data to CSV file
# with open(csv_filename, mode='w', newline='') as file:
#     writer = csv.writer(file)
    
#     # Write header
#     writer.writerow(['Currency', 'Unit', 'Name', 'ISO3', 'Buy', 'Sell'])
    
#     # Write data rows
#     for rate in rates:
#         currency = rate['currency']
#         writer.writerow([currency['iso3'], currency['unit'], currency['name'], currency['iso3'], rate['buy'], rate['sell']])

# print(f"FOREX rates data has been exported to {csv_filename}.")

