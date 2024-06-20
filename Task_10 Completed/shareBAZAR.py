
# %%
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Step 1: Get the HTML page and extract the CSRF token
session = requests.Session()
get_url = "https://www.sharesansar.com/today-share-price"
response = session.get(get_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML to find the CSRF token
    soup = BeautifulSoup(response.text, 'html.parser')
    token = soup.find('input', {'name': '_token'})['value']
else:
    print("Failed to retrieve the CSRF token.")
    exit()

# Step 2: Send the POST request using the extracted CSRF token
post_url = "https://www.sharesansar.com/ajaxtodayshareprice"
headers = {
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "DNT": "1",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "*/*",
    "Referer": "https://www.sharesansar.com/today-share-price",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-platform": "\"Android\""
}



# # Function to format date string
def format_date(date):
    return date.strftime("%Y-%m-%d")

# # Define the fixed date
user_input = input("Enter the date in AD in format: 2024-05-29: ")

fixed_date = datetime.strptime(user_input, "%Y-%m-%d")

# # Prepare the data payload for the specific date

data = {
    "_token": token,
    "sector": "all_sec",
    "date": format_date(fixed_date)
}


# # Make the POST request
response = requests.post(post_url, headers=headers, data=data)

# # Check the response status
# if response.status_code == 200:
#     response_html = response.text
#     print("Response for", data['date'], ":")
#     # print(response_html)
# else:
#     print("Request failed for", format_date(fixed_date), "with status code:", response.status_code)

response = session.post(post_url, headers=headers, data=data)
response_html = response.text
print(response_html)


# %%
# Extracting data within <thead> tags from both tables
import re
thead_pattern = r'<thead>(.*?)</thead>'
thead_data = re.findall(thead_pattern, response_html, re.DOTALL)              

head_data_all = []

# Iterate over each element of thead_data and extract data within <th> tags
for data in thead_data:
    head_data = re.findall(r'<th.*?>(.*?)</th>', data, re.DOTALL)
    head_data_all.extend(head_data)

print("T_Head:", head_data_all)

# %%
# Extracting data within <tbody> tags
import re
tbody_pattern = r'<tbody>(.*?)</tbody>'
tbody_data = re.findall(tbody_pattern, response_html, re.DOTALL)              

matches_data_all = []

# Iterate over each element of tbody_data and extract data within <td> tags
for data in tbody_data:
    matches_data = re.findall(r'<td.*?>(.*?)</td>', data, re.DOTALL)
    matches_data_all.extend(matches_data)

print("TBody:", matches_data_all)

# %%
num_columns = len(head_data_all)
print(len(head_data_all))

# Split the data into sublists for each row
sublists = [matches_data_all[i:i+num_columns] for i in range(0, len(matches_data_all), num_columns)]
print(sublists)



# %%
# List to store company names
company_names = []

# Regular expression pattern to match the title attribute
company_pattern = r'title="([^"]+)"'

# Loop through each sublist and extract company names
for sublist in sublists:
    for item in sublist:
        match = re.search(company_pattern, item)
        if match:
            company_names.append(match.group(1))

print(company_names)

# %%
import re
import csv
from datetime import datetime



# List to store company names
company_names = []

# Regular expression pattern to match the title attribute
company_pattern = r'title="([^"]+)"'

# Loop through each sublist and extract company names
for sublist in sublists:
    for item in sublist:
        match = re.search(company_pattern, item)
        if match:
            company_names.append(match.group(1))

# Function to extract symbol from HTML anchor tag
def extract_symbol(html):
    name_match = re.search(r'>([^<]+)<', html)
    symbol = name_match.group(1) if name_match else None
    return symbol


# Convert sublists to list of dictionaries
data = []

if sublists == [[' No Record Found.']]:
    print("No Record Found")
else:
    for i, sublist in enumerate(sublists):
        symbol = extract_symbol(sublist[1])
        entry = {head_data_all[0]: sublist[0], head_data_all[1]: symbol}
        entry.update(dict(zip(head_data_all[2:], sublist[2:])))
        entry['Company Name'] = company_names[i]
        data.append(entry)


    file_name = f"csv/share_Bazar_{format_date(fixed_date)}.csv"

    # Write data to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=head_data_all + ['Company Name'])
        # Write header
        writer.writeheader()
        print(head_data_all)
        # Write rows
        for row in data:
            writer.writerow(row)
            print(row)

    print(f"Data has been written to {file_name}")




# %%
# # Define the file name
# import csv
# file_name = f"data_{format_date(fixed_date)}.csv"

# # Write data to CSV
# with open(file_name, mode='w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=head_data_all + ['URL', 'Company Name', 'Title'])
#     # Write header
#     writer.writeheader()
#     # Write rows
#     for row in data:
#         writer.writerow(row)

# print(f"Data has been written to {file_name}")


