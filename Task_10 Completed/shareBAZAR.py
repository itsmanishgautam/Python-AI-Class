import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import csv
import os

# Function to format date string
def format_date(date):
    return date.strftime("%Y-%m-%d")

# Step 1: Get the HTML page and extract the CSRF token
def get_csrf_token(session, url):
    response = session.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        token = soup.find('input', {'name': '_token'})['value']
        return token
    else:
        raise Exception("Failed to retrieve the CSRF token.")

# Step 2: Send the POST request using the extracted CSRF token
def get_share_data(session, url, headers, data):
    response = session.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to retrieve share data.")

# Step 3: Extract table headers and data from HTML
def extract_table_data(html):
    thead_pattern = r'<thead>(.*?)</thead>'
    tbody_pattern = r'<tbody>(.*?)</tbody>'
    
    thead_data = re.findall(thead_pattern, html, re.DOTALL)
    tbody_data = re.findall(tbody_pattern, html, re.DOTALL)
    
    head_data_all = []
    for data in thead_data:
        head_data = re.findall(r'<th.*?>(.*?)</th>', data, re.DOTALL)
        head_data_all.extend(head_data)
    
    matches_data_all = []
    for data in tbody_data:
        matches_data = re.findall(r'<td.*?>(.*?)</td>', data, re.DOTALL)
        matches_data_all.extend(matches_data)
    
    return head_data_all, matches_data_all

# Step 4: Parse table data into structured format
def parse_table_data(head_data_all, matches_data_all):
    num_columns = len(head_data_all)
    sublists = [matches_data_all[i:i + num_columns] for i in range(0, len(matches_data_all), num_columns)]
    
    company_names = []
    company_pattern = r'title="([^"]+)"'
    for sublist in sublists:
        for item in sublist:
            match = re.search(company_pattern, item)
            if match:
                company_names.append(match.group(1))
    
    def extract_symbol(html):
        name_match = re.search(r'>([^<]+)<', html)
        return name_match.group(1) if name_match else None
    
    data = []
    if sublists == [[' No Record Found.']]:
        return "No Record Found", data
    
    for i, sublist in enumerate(sublists):
        symbol = extract_symbol(sublist[1])
        entry = {head_data_all[0]: sublist[0], head_data_all[1]: symbol}
        entry.update(dict(zip(head_data_all[2:], sublist[2:])))
        entry['Company Name'] = company_names[i]
        data.append(entry)
    
    return head_data_all, data

# # Step 5: Write data to CSV file
# def write_to_csv(file_name, head_data_all, data):
#     os.makedirs(os.path.dirname(file_name), exist_ok=True)
#     with open(file_name, mode='w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=head_data_all + ['Company Name'])
#         writer.writeheader()
#         for row in data:
#             writer.writerow(row)

def main():
    # Define URLs and headers
    get_url = "https://www.sharesansar.com/today-share-price"
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

    # Get user input for date
    user_input = input("Enter the date in AD in format: YYYY-MM-DD: ")
    fixed_date = datetime.strptime(user_input, "%Y-%m-%d")

    # Initialize session and get CSRF token
    session = requests.Session()
    token = get_csrf_token(session, get_url)
    
    # Prepare data payload for the specific date
    data = {
        "_token": token,
        "sector": "all_sec",
        "date": format_date(fixed_date)
    }

    # Get share data
    response_html = get_share_data(session, post_url, headers, data)

    # Extract table headers and data
    head_data_all, matches_data_all = extract_table_data(response_html)
    
    # Parse table data into structured format
    head_data_all, data = parse_table_data(head_data_all, matches_data_all)

    # Handle "No Record Found" case
    # if head_data_all == "No Record Found":
    #     print("No Record Found")
    # else:
    #     # Write data to CSV file
    #     file_name = f"Task_10 Completed/csv/share_Bazar_{format_date(fixed_date)}.csv"
    #     write_to_csv(file_name, head_data_all, data)
    #     print(f"Data has been written to {file_name}")

if __name__ == "__main__":
    main()
