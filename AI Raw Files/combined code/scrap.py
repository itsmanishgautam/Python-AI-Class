# %%
import urllib.request
from bs4 import BeautifulSoup

job_titles = []
datacompany = []
doubledata = []

# User-Agent string to avoid being blocked
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

for page_num in range(1, 14):
    url = f'https://www.jobsnepal.com/jobs?page={page_num}'

    request = urllib.request.Request(url, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    html_content = response.read().decode('utf-8')

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <div class="col-md-8 px-0 top-content"> elements
    alldata = soup.find_all('div', class_='col-md-8 px-0 top-content')

    title = soup.find_all('h2', class_='job-title')

    # Extract job titles from the current page
    job_titles.extend([h2.text.strip() for h2 in title])


    # Find all <div class="card-inner"> elements
    datacompany_elements = soup.find_all('div', class_='card-inner')

    for element in datacompany_elements:
        company_name = element.find('a').get('title') if element.find('a') else None
        if company_name:
            datacompany.append(company_name.strip())



    datadouble_data = soup.find_all('div', class_=['icon-price-tags mr-2 text-success icon-sm', 'd-flex align-items-center pl-1 pr-1 py-1'])


    # doubledata = [div.find('div').text.strip() for div in data]


    # Find all <div> elements with the specified classes
    data_elements = soup.find_all('div', class_=['icon-price-tags mr-2 text-success icon-sm', 'd-flex align-items-center pl-1 pr-1 py-1'])

    # Extract information from the elements and append to doubledata
    for element in data_elements:
        bothdata = element.find('div')
        if bothdata:
            data = bothdata.text.strip()
            doubledata.append(data) 

    
locations = doubledata[::2]
categories = doubledata[1::2]
    

print("Job Titles:", job_titles)
print("Company:", datacompany)
print("Locations:", locations)
print("Categories:", categories)


# %% [markdown]
# Export to csv

# %%
# Create a list of tuples containing job titles and companies
data = list(zip(job_titles, datacompany,locations,categories))
import csv

# Define the CSV file path
csv_file = 'csv/Job_data_Soup2.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Company', 'Location', 'Category'])  # Write header row
    writer.writerows(data)  # Write data rows

print(f'Data exported to {csv_file}')


# %%
import re
import urllib.request

job_titles = []
datacompany = []
locations = []
categories = []

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

for page_num in range(1, 15):
    url = f'https://www.jobsnepal.com/jobs?page={page_num}'

    request = urllib.request.Request(url, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    html_content = response.read().decode('utf-8')


    titlepattern = r'<h2 class="job-title" title="(.*?)">'
    matchtitle = re.findall(titlepattern, html_content)
    job_titles.extend(matchtitle)


    companypattern = r'<div class="card-inner">.*?<a[^>]+title="(.*?)"'
    matchcompany = re.findall(companypattern, html_content, re.DOTALL)
    datacompany.extend(matchcompany)


    locationpattern = r'<div class="d-flex align-items-center pl-1 pr-1 py-1">\s*<i class="icon-location4 mr-2 text-success">\s*</i>\s*<div>\s*(.*?)\s*</div>'
    matchlocation = re.findall(locationpattern, html_content)
    locations.extend(matchlocation)


    categoriespattern = r'<div class="d-flex align-items-center pl-1 pr-1 py-1">\s*<i class="icon-price-tags mr-2 text-success icon-sm">\s*</i>\s*<div>\s*(.*?)\s*</div>'
    matchcategory = re.findall(categoriespattern, html_content)
    categories.extend(matchcategory)



print("Job Titles:", job_titles)
print("Company:", datacompany)
print("Locations:", locations)
print("Categories:", categories)


# %%
totaljob_title = len(job_titles)
print(totaljob_title)

# %% [markdown]
# Export To CSV

# %%
# Create a list of tuples containing job titles and companies
data = list(zip(job_titles, datacompany,locations,categories))
import csv

# Define the CSV file path
csv_file = 'csv/jobs_nepal_regex_scrap.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Company', 'Location', 'Category'])  # Write header row
    writer.writerows(data)  # Write data rows

print(f'Data exported to {csv_file}')


# %%
import re
import urllib.request

# %%
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# %%
url ='https://bankbyaj.com/deposite'
request = urllib.request.Request(url, headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html_content = response.read().decode('utf-8')

# %%
# print(html_content)

# %%
bank_name_pattern = r'<h3[^>]*>[^<]*<\/h3><span[^>]*>([^<]*)<\/span>'
Bank_name=re.findall(bank_name_pattern,html_content)
print(Bank_name)

# %%
print(len(Bank_name))

# %%
# Account_Intrest_Pattern = r'<h3[^>]*>(\d+\.\d+%?)<\/h3>'
Account_Intrest_Pattern = r'<td _ngcontent-sc20=""><h3 _ngcontent-sc20="">(.*?)</h3></td><td _ngcontent-sc20=""><h3 _ngcontent-sc20="">(.*?)</h3></td>'
Account_Data = re.findall(Account_Intrest_Pattern, html_content)
print(Account_Data)

Savings_Deposit =[item[0] for item in Account_Data]
Fixed_Deposit = [item[1] for item in Account_Data]

print("Savings Deposit Rates:", Savings_Deposit)
print("Fixed Deposit Rates:", Fixed_Deposit)

# %%
# Create a list of tuples containing job titles and companies
data = list(zip(Bank_name,Savings_Deposit,Fixed_Deposit))
import csv

# Define the CSV file path
csv_file = 'csv/bank_interest.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Bankn Name','Savings Rate','Fixed Rate'])  # Write header row
    writer.writerows(data)  # Write data rows

print(f'Data exported to {csv_file}')

# %% [markdown]
# ASK QUESTION
# 

# %%
# import csv
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# # Load CSV data into a dictionary
# bank_data = {}
# with open('csv/bank_interest.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         bank_data[row['Bank_Name']] = {'Savings_Rate': row['Savings_Rate'], 'Fixed_Rate': row['Fixed_Rate']}

# # Function to extract bank name from user input
# def extract_bank_name(user_input):
#     tokens = word_tokenize(user_input)
#     stop_words = set(stopwords.words('english'))
#     filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
#     for token in filtered_tokens:
#         if token in bank_data:
#             return token
#     return None

# # Function to get interest rate based on user question
# def get_interest_rate(user_question):
#     bank_name = extract_bank_name(user_question)
#     if bank_name:
#         if 'savings' in user_question.lower():
#             return bank_data[bank_name]['Savings_Rate']
#         elif 'fixed deposit' in user_question.lower():
#             return bank_data[bank_name]['Fixed_Rate']
#     return None

# # Example user questions
# user_questions = input("Enter Question: ")

# # Generate bot answers
# for question in user_questions.split(";"):
#     interest_rate = get_interest_rate(question)
#     if interest_rate:
#         print(f"**User Question:** {question}")
#         print(f"**Bot Answer:** The {'savings' if 'savings' in question.lower() else 'fixed deposit'} interest rate at {extract_bank_name(question)} is {interest_rate}.")
#         print()
#     else:
#         print(f"**User Question:** {question}")
#         print("**Bot Answer:** Sorry, I couldn't find the information for your query.")
#         print()


# %%
import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load CSV data into a dictionary
bank_data = {}
with open('csv/bank_interest.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        bank_name = row['Bank_Name']
        tokens = word_tokenize(bank_name)  # Tokenize bank name
        bank_data[tuple(tokens)] = {
            'Bank_Name': tokens,  # Add bank name token
            'Savings_Rate': row['Savings_Rate'],
            'Fixed_Rate': row['Fixed_Rate']
        }

print(bank_data)

# %%
user_input = input("Enter your query (less KEYWORD): ")  # Example: "Nepal Bank"

# Tokenize user input
user_tokens = word_tokenize(user_input)

# Convert tokens to lowercase
user_tokens_lower = [token.lower() for token in user_tokens]

print(user_tokens_lower)

# %%
# user_tokens = [ 'Banijya']

# # bank_data = {
# #     ('Nepal', 'Bank', 'Ltd', '.'): {'Bank_Name': ['Nepal', 'Bank', 'Ltd', '.'], 'Savings_Rate': '5.65%', 'Fixed_Rate': '6.75%'},
# #     ('Rastriya', 'Banijya', 'Bank'): {'Bank_Name': ['Rastriya', 'Banijya', 'Bank'], 'Savings_Rate': '4.65%', 'Fixed_Rate': '6.40%'}
# # }

# Function to get bank data based on user input tokens
def get_bank_data(user_tokens_lower):
    max_matches = 0
    best_match = None
    
    for key in bank_data.keys():
        key_lower = [k.lower() for k in key]
        matches = sum(token in key_lower for token in user_tokens_lower)
        
        if matches > max_matches:
            max_matches = matches
            best_match = bank_data[key]
    
    return best_match

# Get bank data based on user input tokens
bank_info = get_bank_data(user_tokens)

# Reply with bank data if available
if bank_info:
    print("**Bot Response:** Here is the information for your query:")
    for key, value in bank_info.items():
        if key == 'Bank_Name':
            print(f"{key}: {' '.join(value)}")
        else:
            print(f"{key}: {value}")
else:
    print("**Bot Response:** Sorry, I couldn't find any relevant information.")






# %%
import re
import urllib.request

# %%
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# %%
url = 'https://www.hamropatro.com/gold'
request = urllib.request.Request(url, headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html_content = response.read().decode('utf-8')

# %%
# print(html_content)

# %%
pattern = r'<li onClick=".*?">(.*?)<\/li>\s*<li onClick=".*?">\s*Nrs.\s*(.*?)<\/li>'
matches = re.findall(pattern, html_content)

Item_Name =[item[0] for item in matches]
Rupees = [item[1] for item in matches]

print("Item_Name:",Item_Name)
print("Rupees:",Rupees)


# %%
# Create a list of tuples containing job titles and companies
data = list(zip(Item_Name,Rupees))
import csv

# Define the CSV file path
csv_file = 'csv/Gold_Silver_Cost.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Item Name','Rupees'])  # Write header row
    writer.writerows(data)  # Write data rows

print(f'Data exported to {csv_file}')


# %%
import re
import urllib.request

# %%
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# %%
url = 'https://namastesindhupalchowk.com/blog/district-of-nepal'
request = urllib.request.Request(url, headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html_content = response.read().decode('utf-8')

# %%
# Extracting data within <tbody> tags from both tables
tbody_data = re.findall(r'<tbody>\s*(.*?)\s*<\/tbody>', html_content, re.DOTALL)

matches_data_all = []

# Iterate over each element of tbody_data and extract data within <td> tags
for data in tbody_data:
    matches_data = re.findall(r'<td>(.*?)<\/td>', data)
    matches_data_all.extend(matches_data)

print("All_Data:", matches_data_all)



# %%
value_to_find = 'Taplejung'

# Find position
position = matches_data_all.index(value_to_find)

print(f"The position of '{value_to_find}' in the list is {position}.")

# %%
index = 42  # Assuming you want to split at index 5 (Python indexing starts from 0)

# Separate the list
list_before_index = matches_data_all[:index]
list_after_index = matches_data_all[index:]

# Print the separated lists
print("List before index:", list_before_index)
print("List after index:", list_after_index)

# %%
value_to_find = '242157'

# Find position
position = list_after_index.index(value_to_find)

print(f"The position of '{value_to_find}' in the list is {position}.")



# %%
index = 385  # Assuming you want to split at index 5 (Python indexing starts from 0)

# Separate the list
Final_List = list_after_index[:index]
list_after_index = list_after_index[index:]

# Print the separated lists
print("Final_List:", Final_List)
print("List after index:", list_after_index)

# %%
# Separate the list into sublists of five elements each
sublists = [Final_List[i:i+5] for i in range(0, len(Final_List), 5)]

# Extract data into separate lists
S_No = [item[0] for item in sublists]
District = [item[1] for item in sublists]
Headquarter = [item[2] for item in sublists]
Total_Area = [item[3] for item in sublists]
Population = [item[4] for item in sublists]

# Print the separated lists
print("S.No:", S_No)
print("District:", District)
print("Headquarter:", Headquarter)
print("Total_Area:", Total_Area)
print("Population:", Population)

# %%
# Create a list of tuples containing job titles and companies
data = list(zip(District,Headquarter,Total_Area,Population))
import csv

# Define the CSV file path
csv_file = 'csv/nepal_data.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['District','Headquarter','Total Area','Population'])  # Write header row
    writer.writerows(data)  # Write data rows

print(f'Data exported to {csv_file}')


# %%
import re
import urllib.request

# %%
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# %%
url = 'https://www.sharesansar.com/today-share-price'
request = urllib.request.Request(url, headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html_content = response.read().decode('utf-8')

# %% [markdown]
# Head Data Extract

# %%
# Extracting data within <thead> tags from both tables
thead_pattern = r'<thead>(.*?)</thead>'
thead_data = re.findall(thead_pattern, html_content, re.DOTALL)              

head_data_all = []

# Iterate over each element of thead_data and extract data within <th> tags
for data in thead_data:
    head_data = re.findall(r'<th.*?>(.*?)</th>', data, re.DOTALL)
    head_data_all.extend(head_data)

# print("T_Head:", head_data_all)

# %%
# print(len(head_data_all))

# %% [markdown]
# Body Extract

# %%
# Extracting data within <tbody> tags
tbody_pattern = r'<tbody>(.*?)</tbody>'
tbody_data = re.findall(tbody_pattern, html_content, re.DOTALL)              

matches_data_all = []

# Iterate over each element of tbody_data and extract data within <td> tags
for data in tbody_data:
    matches_data = re.findall(r'<td.*?>(.*?)</td>', data, re.DOTALL)
    matches_data_all.extend(matches_data)

# print("tbody_text", matches_data_all)

# %%

# Separate the list into sublists of 21 elements each
sublists = [matches_data_all[i:i+21] for i in range(0, len(matches_data_all), 21)]

# Extract data into separate lists
S_No = [item[0] for item in sublists]
Symbol = [item[1] for item in sublists]

Conf = [item[2] for item in sublists]
Open = [item[3] for item in sublists]
High = [item[4] for item in sublists]
Low = [item[5] for item in sublists]
Close = [item[6] for item in sublists]
VWAP = [item[7] for item in sublists]
Vol = [item[8] for item in sublists]
Prev_Close = [item[9] for item in sublists]
Turnover = [item[10] for item in sublists]
Trans = [item[11] for item in sublists]
Diff = [item[12] for item in sublists]
Range = [item[13] for item in sublists]
Diff_Percent = [item[14] for item in sublists]
Range_Percent = [item[15] for item in sublists]
VWAP_Percent = [item[16] for item in sublists]
Days_120 = [item[17] for item in sublists]
Days_180 = [item[18] for item in sublists]
Weeks_High = [item[19] for item in sublists]
Weeks_Low = [item[20] for item in sublists]

# Print the separated lists
# print("S.No:", S_No)
# print("Symbol:", Symbol)
# print("Conf:", Conf)
# print("Open:", Open)
# print("High:", High)
# print("Low:", Low)
# print("Close:", Close)
# print("VWAP:", VWAP)
# print("Vol:", Vol)
# print("Prev. Close:", Prev_Close)
# print("Turnover:", Turnover)
# print("Trans:", Trans)
# print("Diff:", Diff)
# print("Range:", Range)
# print("Diff %:", Diff_Percent)
# print("Range %:", Range_Percent)
# print("VWAP %:", VWAP_Percent)
# print("120 Days:", Days_120)
# print("180 Days:", Days_180)
# print("52 Weeks High:", Weeks_High)
# print("52 Weeks Low:", Weeks_Low)


# %% [markdown]
# Symbol editing

# %%
pattern = r'title="([^"]+)"[^>]*>([^<]+)<\/a>'

matches = re.findall(pattern, ''.join(Symbol))

names = []
symbols_list = []

for name, symbol in matches:
    names.append(name)
    symbols_list.append(symbol)

# print("Names:", names)
# print("Symbols:", symbols_list)

# %%
import csv

# Define the file name
csv_filename = "csv/nepse_data.csv"

# Combine the separated lists into rows
rows = zip( names ,symbols_list, Conf, Open, High, Low, Close, VWAP, Vol, Prev_Close, Turnover, Trans, Diff, Range, Diff_Percent, Range_Percent, VWAP_Percent, Days_120, Days_180, Weeks_High, Weeks_Low)

# Write the rows to a CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header
    writer.writerow([ 'Name','Symbol', 'Conf', 'Open', 'High', 'Low', 'Close', 'VWAP', 'Vol', 'Prev. Close', 'Turnover', 'Trans', 'Diff', 'Range', 'Diff %', 'Range %', 'VWAP %', '120 Days', '180 Days', '52 Weeks High', '52 Weeks Low'])
    
    # Write the rows
    for row in rows:
        writer.writerow(row)

print("CSV file exported successfully.")



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


# %%
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer

# %%
import pandas as pd
training_data = pd.read_csv('first_twitter_training.csv')

# %%
training_data = training_data.drop(training_data.columns[0], axis=1)

# %%
df = training_data.drop(training_data.columns[0], axis=1)

# %%
labels = df.iloc[:, 0].values
string_data = df.iloc[:, 1].values

# %%


# %%
import numpy as np
labels = np.array([
    1 if label.lower() == 'positive' 
    else -1 if label.lower() == 'negative' 
    else 0 if label.lower() == 'neutral' 
    else 2 if label.lower() == 'irrelevant' 

    else label
    for label in labels
])


# %%
print(labels[:100])


# %%
# Create a DataFrame from the extracted data
data_to_export = pd.DataFrame({'Labels': labels, 'StringData': string_data})

# Specify the file path where you want to save the CSV file
file_path = 'label_only_numeric_exported_data.csv'

# Export the DataFrame to a CSV file
data_to_export.to_csv(file_path, index=False)

print("Data exported to CSV successfully.")

# %%
print(string_data[:10])




# %%
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# %%
dataset = pd.read_csv('label_only_numeric_exported_data.csv')
sentences = dataset['StringData'].astype(str).tolist()
labels = dataset['Labels'].tolist()

labels = np.array(labels)

labels = dataset['Labels'].apply(lambda x: 1 if x > 0 else 0).tolist()
labels = np.array(labels)

# %%
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)
padded_data = pad_sequences(sequences, padding='post', truncating='post')

# %%
vocab_size = len(word_index) + 1
embedding_dim = 16
max_length = padded_data.shape[1]

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# %%
model.fit(padded_data, labels, epochs=10, validation_split=0.2)

loss, accuracy = model.evaluate(padded_data, labels)
print(f"Loss: {loss}, Accuracy: {accuracy}")

# %%
def predict_user_input(user_sentences):
    user_sequences = tokenizer.texts_to_sequences(user_sentences)
    user_padded = pad_sequences(user_sequences, padding='post', truncating='post', maxlen=max_length)
    predictions = model.predict(user_padded)
    predicted_labels = [1 if p > 0.5 else 0 for p in predictions]
    return predicted_labels

# %%
user_input = input("Enter a sentence: ")
user_sentences = [user_input]  # Ensure user input is a list of strings
predicted_labels = predict_user_input(user_sentences)
print(f"Predicted Labels: {predicted_labels}")


import random
import matplotlib.pyplot as plt

# Generate random dataset
random.seed(0)
X = [[random.uniform(0, 2)] for _ in range(100)]
y = [[4 + 3 * x[0] + random.gauss(0, 1)] for x in X]

train_ratio = 0.8
train_size = int(len(X) * train_ratio)
X_train = X[:train_size]
y_train = y[:train_size]
X_test = X[train_size:]
y_test = y[train_size:]

# Add bias term to training and testing data
def add_bias_term(X):
    return [[1] + x for x in X]

X_train_b = add_bias_term(X_train)
X_test_b = add_bias_term(X_test)

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def matmul(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in transpose(B)] for A_row in A]

def inverse_2x2(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]

X_train_b_T = transpose(X_train_b)
X_train_b_T_X_train_b = matmul(X_train_b_T, X_train_b)
X_train_b_T_X_train_b_inv = inverse_2x2(X_train_b_T_X_train_b)
X_train_b_T_y_train = matmul(X_train_b_T, y_train)
theta_best = matmul(X_train_b_T_X_train_b_inv, X_train_b_T_y_train)

print(f"Coefficient: {theta_best[1][0]}")
print(f"Intercept: {theta_best[0][0]}")

y_test_pred = matmul(X_test_b, theta_best)

mse = sum((y_test[i][0] - y_test_pred[i][0]) ** 2 for i in range(len(y_test))) / len(y_test)
print(f"Mean squared error: {mse}")

plt.plot([x[1] for x in X_train_b], [y[0] for y in y_train], "b.", label="Training data")
plt.plot([x[1] for x in X_test_b], [y[0] for y in y_test], "g.", label="Test data")
plt.plot([x[1] for x in X_test_b], [y[0] for y in y_test_pred], "r-", linewidth=2, label="Predicted line")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Linear Regression from Scratch")
plt.show()
import random
import csv

def generate_fake_courses(num_records):
    courses = ['Java', 'Python', 'PHP', 'C#']  # List of available courses

    with open('Task_2/csv/Courses.csv', 'w', newline='') as csvfile:
        fieldnames = ['Course']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_records):
            writer.writerow({'Course': random.choice(courses)})  # Choose a random course from the list

if __name__ == "__main__":
    num_records = 100000
    generate_fake_courses(num_records)
from faker import Faker
import csv
import random
import pandas as pd

fake = Faker()

def generate_fake_data(num_records):
    with open('Task_2/csv/fake_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Contact', 'Country', 'CountryCode']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow({
                'Name': fake.name(),
                'Contact': fake.phone_number(),
                'Country': fake.country(),
                'CountryCode': fake.country_code()
            })


def merge_csv(df1,df2):
    merged_df = pd.concat([df1, df2], axis=1)
    merged_df.to_csv("Task_2/csv/merged_Courses_output.csv", index=False)



def split_csv(input_file):
    output_files = ['Task_2/csv/splitoutput1.csv', 'Task_2/csv/splitoutput2.csv', 'Task_2/csv/splitoutput3.csv']

    writers = {}
    for file_name in output_files:
        writers[file_name] = csv.DictWriter(open(file_name, 'w', newline=''), fieldnames=['Country', 'Name', 'Contact', 'CountryCode', 'Course'])
        writers[file_name].writeheader()

    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            output_file = random.choice(output_files)
            writers[output_file].writerow(row)



if __name__ == "__main__":
    num_records = 100000
    generate_fake_data(num_records)

    df1 = pd.read_csv("Task_2/csv/fake_data.csv")
    df2 = pd.read_csv("Task_2/csv/Courses.csv")
    merge_csv(df1,df2)

    input_file = 'Task_2/csv/merged_Courses_output.csv'
    split_csv(input_file)
    print("Fake data generated and CSV file split completed.")

import pandas as pd

def merge_csv_complex(df3, df4, output_file):
    merged_df = pd.merge(df4, df3, on=['Currency_Code'])
    merged_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    df3 = pd.read_csv("Task_2/csv/forex.csv")
    df4 = pd.read_csv("Task_2/csv/Country_and_CurrencyCode.csv")
    output_file = 'Task_2/csv/CountryAdd_onCurrency_output.csv'
    merge_csv_complex(df3, df4, output_file)

import pandas as pd

def merge_csv_complex(out1, out2, out3, mergedcsv1, output_file1, output_file2, output_file3):

    # Convert "Country" column to lowercase for case-insensitive matching
    mergedcsv1['Country'] = mergedcsv1['Country'].str.lower()
    out1['Country'] = out1['Country'].str.lower()
    out2['Country'] = out2['Country'].str.lower()
    out3['Country'] = out3['Country'].str.lower()

    # Perform the merge
    merged_df1 = pd.merge(out1, mergedcsv1, on=['Country'])
    merged_df2 = pd.merge(out2, mergedcsv1, on=['Country'])
    merged_df3 = pd.merge(out3, mergedcsv1, on=['Country'])
    
    # Write the merged DataFrames to CSV files
    merged_df1.to_csv(output_file1, index=False)
    merged_df2.to_csv(output_file2, index=False)
    merged_df3.to_csv(output_file3, index=False)

if __name__ == "__main__":
    mergedcsv = pd.read_csv("Task_2/csv/CountryAdd_onCurrency_output.csv")
    # Reorder columns
    df = mergedcsv[['Country', 'Currency_Code', 'Currency_x', 'Currency_y', 'Units', 'Buy', 'Sell']]
    # Write back to CSV
    df.to_csv('Task_2/csv/CountryRearrange.csv', index=False)

    mergedcsv1 = pd.read_csv('Task_2/csv/CountryRearrange.csv')
    out1 = pd.read_csv("Task_2/csv/splitoutput1.csv")
    out2 = pd.read_csv("Task_2/csv/splitoutput2.csv")
    out3 = pd.read_csv("Task_2/csv/splitoutput3.csv")

    output_file1 = 'Task_2/csv/finaldata1.csv'
    output_file2 = 'Task_2/csv/finaldata2.csv'
    output_file3 = 'Task_2/csv/finaldata3.csv'

    merge_csv_complex(out1, out2, out3, mergedcsv1, output_file1, output_file2, output_file3)






# %%
import urllib.request
import re

# %%
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# %%
url ='https://www.nrb.org.np/forex/'
request = urllib.request.Request(url, headers={'User-Agent': user_agent})
response = urllib.request.urlopen(request)
html_content = response.read().decode('utf-8')

# %%
# print(html_content)

# %%
# Define the regex pattern to match everything between <tbody> and </tbody> tags
tbody_pattern = r'<tbody>(.*?)</tbody>'

# %%
# Use re.findall to find all matches of the pattern in the HTML content
body_matches = re.findall(tbody_pattern, html_content, re.DOTALL)

# %%
print(body_matches)

# %%
# Define the regex pattern
currency_pattern = r'<div class="flag flag--..."></div>\s*<div class="ml-2 text-uppercase">(.*?)\s*<span\s*class="text-capitalize">\(([^)]+)\)</span>'

# Find all matches in the HTML
currency_matches = re.findall(currency_pattern, html_content) 

# %%
print(currency_matches)

# %%
currency_code = [item[0] for item in currency_matches]
currency_code = [code.upper() for code in currency_code]
currency = [item[1] for item in currency_matches]

# %%
print(currency_code)
print(currency)

# %%
print(len(currency_matches))

# %%
data_pattern = r'<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>'
# Find all matches in the HTML
data_matches = re.findall(data_pattern, html_content) 

# %%
print(data_matches)

# %%
units = [item[0] for item in data_matches]
buy = [item[1] for item in data_matches]
sell = [item[2] for item in data_matches]


# %%
print(units)
print(buy)
print(sell)

# %%
print(len(data_matches))

# %%
# Create a list of tuples containing job titles and companies
data = list(zip(currency_code,currency,units,buy,sell))
import csv

# Define the CSV file path
csv_file = 'csv/forex.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Currency_Code','Currency','Units','Buy','Sell'])  # Write header row
    writer.writerows(data)  # Write data rows

print(f'Data exported to {csv_file}')


import os
import json
import Levenshtein
import random

with open('Task_4 Completed/data.json', 'r') as file:
    data = json.load(file)

def calculate_similarity(input_str, query):
    distance = Levenshtein.distance(input_str.lower(), query.lower())
    similarity = 1 - (distance / max(len(input_str), len(query)))
    return similarity

def generate_response(user_input, query_counts):
    if os.path.exists("Task_4 Completed/query_counts.json"):
        with open("Task_4 Completed/query_counts.json", "r") as file:
            query_counts = json.load(file)

    irritated_responses = [response for intent in data['intents'] if intent['tag'] == 'irritated_responses' for response in intent['responses']]

    similar_queries = [query for query in query_counts.keys() if calculate_similarity(user_input, query) > 0.7]  # Adjust similarity threshold as needed

    if similar_queries:
        query = max(similar_queries, key=lambda x: query_counts[x])
        query_counts[query] += 1
        response = random.choice(irritated_responses)
    elif any(user_input in intent['patterns'] for intent in data['intents']):
        for intent in data['intents']:
            for pattern in intent['patterns']:
                if user_input in pattern:
                    response = random.choice(intent['responses'])
                    break
    else:
        response = "I'm sorry, I don't understand that."
    
    query_counts[user_input.strip().lower()] = query_counts.get(user_input.strip().lower(), 0) + 1

    with open("Task_4 Completed/query_counts.json", "w") as file:
        json.dump(query_counts, file)

    return response


# Chatbot loop
print("Welcome to the Chatbot!")
query_counts = {}

while True:
    user_input = input("You: ").lower()
    if user_input in ['quit', 'bye', 'goodbye']:
        break 
    else:
        response = generate_response(user_input, query_counts)
        print("Bot:", response)

if os.path.exists("Task_4 Completed/query_counts.json"):
    os.remove("Task_4 Completed/query_counts.json")


import csv
import pandas as pd

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        elif self.head.data[2] > data[2]: 
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data[2] < data[2]: 
                current = current.next
            new_node.next = current.next
            current.next = new_node

def add_more_relations():
    return input("Would you like to add more relations? (yes/no): ").lower() == "yes"

def sort_into_linked_list(df):
    linked_list = SortedLinkedList()
    if df is not None:
        for index, row in df.iterrows():
            relation = row["Relation"].lower()
            category = row["Category"].lower()
            age = row["Age"]
            linked_list.insert((relation, category, age))
    return linked_list

def display_linked_list(linked_list):
    current = linked_list.head
    while current:
        print("Relation:", current.data[0])
        print("Category:", current.data[1])
        print("Age:", current.data[2])
        print("-------------------")
        current = current.next

def export_to_csv(linked_list, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Relation", "Category", "Age"])
        current = linked_list.head
        while current:
            writer.writerow(current.data)
            current = current.next
    print("Data exported to", filename)

def main():
    try:
        existing_filename = "Task_5/relation.csv"
        try:
            existing_df = pd.read_csv(existing_filename)
        except FileNotFoundError:
            existing_df = pd.DataFrame(columns=["Relation", "Category", "Age"])

        new_data = []
        while add_more_relations():
            relation = input("Enter the relation: ").lower()
            category = input("Enter the category (Senior/Junior): ").lower()
            age = int(input("Enter the age: "))
            new_data.append({"Relation": relation, "Category": category, "Age": age})

        new_df = pd.DataFrame(new_data)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)

        linked_list = sort_into_linked_list(combined_df)
        print("Data sorted into a sorted linked list:")
        display_linked_list(linked_list)

        sorted_filename = "Task_5/sorted_relations.csv"
        export_to_csv(linked_list, sorted_filename)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
import pandas as pd
import spacy

df = pd.read_csv("Task_5 Completed/sorted_relations.csv")
nlp = spacy.load("en_core_web_sm")

def match_user_input(user_input, df):
    doc_user_input = nlp(user_input)
    
    for index, row in df.iterrows():
        doc_relation = nlp(row['Relation'])
        
        for token_user_input in doc_user_input:
            if any(token_user_input.text == token_relation.text for token_relation in doc_relation):
                return row
    
    return None

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    matched_row = match_user_input(user_input, df)
    
    if matched_row is not None:
        if matched_row['Relation'] == matched_row.iloc[0] and matched_row.iloc[1] == 'senior':
            reply = f"Namaste {matched_row['Relation']}, I am a bot."
        elif matched_row['Relation'] == matched_row.iloc[0] and matched_row.iloc[1] == 'junior':
            reply = f"Hello {matched_row['Relation']}, I am a bot."
    else:
        reply = "Sorry, You are not in my database."

    print("Bot:", reply)


import csv
import pandas as pd

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        elif self.head.data[2] > data[2]: 
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data[2] < data[2]: 
                current = current.next
            new_node.next = current.next
            current.next = new_node

def add_more_relations():
    return input("Would you like to add more relations? (yes/no): ").lower() == "yes"

def sort_into_linked_list(df):
    linked_list = SortedLinkedList()
    if df is not None:
        for index, row in df.iterrows():
            relation = row["Relation"].lower()
            category = row["Category"].lower()
            age = row["Age"]
            linked_list.insert((relation, category, age))
    return linked_list

def display_linked_list(linked_list):
    current = linked_list.head
    while current:
        print("Relation:", current.data[0])
        print("Category:", current.data[1])
        print("Age:", current.data[2])
        print("\n")
        current = current.next

def export_to_csv(linked_list, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Relation", "Category", "Age"])
        current = linked_list.head
        while current:
            writer.writerow(current.data)
            current = current.next
    print("Data exported to", filename)

def main():
    try:
        existing_filename = "Task_5/relation.csv"
        try:
            existing_df = pd.read_csv(existing_filename)
        except FileNotFoundError:
            existing_df = pd.DataFrame(columns=["Relation", "Category", "Age"])

        # user_age = int(input("Enter the user age: "))
        user_age = 22
        new_data = []
        while add_more_relations():
            relation = input("Enter the relation: ").lower()
            age = int(input("Enter the age: "))

            category = "senior" if age > user_age else "junior"

            new_data.append({"Relation": relation, "Category": category, "Age": age})

        new_df = pd.DataFrame(new_data)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)

        linked_list = sort_into_linked_list(combined_df)
        print("Data sorted into a sorted linked list:")
        display_linked_list(linked_list)

        sorted_filename = "Task_5/sorted_relations.csv"
        export_to_csv(linked_list, sorted_filename)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

# %%
import re

keywords_set = {
    'sum': ['sum', 'add', 'plus', 'total','append', 'increase', 'increment', 'augment', 'totalize', 'tally'],
    'difference': ['difference', 'subtract', 'minus', 'less', 'decrease', 'reduce', 'deduct', 'take away', 'diminish', 'subtract from'],
    'product': ['product', 'multiply', 'times', 'timesed', 'multiplied by', 'twice', 'double', 'triple', 'quadruple', 'product of'],
    'division': ['division', 'divide', 'over', 'divided by', 'fraction', 'split', 'partition', 'share', 'cut', 'divided into'],
    'power': ['power', 'raised to the power of', 'to the exponent of', 'squared', 'cubed', 'to the nth power', 'to the power', 'exponentiate'],
    # 'addition': ['add', 'plus', 'append']
}

operations_set = {
    'sum': '+',
    'difference': '-',
    'product': '*',
    'division': '/',
    'power': '**',
    # 'addition': '+'
}


# %%

def extract_keyword(input_text):
    for operation, synonyms in keywords_set.items():
        if any(word in input_text for word in synonyms):
            return operation
    return None

def extract_numbers(input_text):
    number_pattern = r'\d+'
    numbers = re.findall(number_pattern, input_text)
    return numbers

# %%


input_text = input("Enter Text: ")
operation = extract_keyword(input_text)

if operation:
    operation_symbol = operations_set.get(operation)
    if operation_symbol:
        numbers = extract_numbers(input_text)
        print(f"Operation: {operation}\nOperation Symbol: {operation_symbol}\nNumbers: {numbers}")
    else:
        print("No operation symbol defined for:", operation)
else:
    print("No operation keyword found in the text.")


# %%
num1 = int(numbers[0])
num2 = int(numbers[1])


if operation in operations_set:
    operator = operations_set[operation]
    expression = f"{num1} {operator} {num2}"
    result = eval(expression)
    print(f"The {operation} of {num1} and {num2} is {result}")
else:
    print("Unsupported operation")



import csv

# Define the CSV filename
csv_filename = "Task_8 Completed/csv/product_data.csv"
tokenized_product_data = []
original_product_data = []

# Function to tokenize a string value
def tokenize(value):
    return value.strip().lower().split()

# Read and tokenize the CSV file
with open(csv_filename, mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Read the header
    for row in reader:
        original_product_data.append(row)  # Keep the original row for better output later
        tokenized_row = []
        for value in row:
            tokenized_row.extend(tokenize(value))
        tokenized_product_data.append(tokenized_row)

# Print the tokenized data for verification (optional)
# for row in tokenized_product_data:
#     print(row)

def format_reply(matched_rows):
    if not matched_rows:
        return "Sorry, no matching products found in the database."
    
    reply = "Matching products found:\n"
    for row in matched_rows:
        reply += ', '.join(row) + '\n'
    return reply

while True:
    keyword = input("Enter the sentence (or 'exit' to quit): ")

    if keyword.lower() == "exit":
        print("Exiting the program...")
        break

    input_tokens = tokenize(keyword)
    # print(f"Tokenized input: {input_tokens}")

    matching_rows = [
        original_product_data[idx] for idx, row in enumerate(tokenized_product_data)
        if any(token in row for token in input_tokens)
    ]
    
    reply = format_reply(matching_rows)
    print(reply)
import csv

def get_product_data():
    product_name = input("Enter the product name: ")
    cost = float(input("Enter the cost of the product: "))
    category = input("Enter the category of the product: ")
    color = input("Enter the color of the product: ")
    container = input("Enter the container type: ")

    product_data = {
        "Product Name": product_name,
        "Cost": cost,
        "Category": category,
        "Color": color,
        "Container":container
    }

    return product_data

csv_filename = "Task_8/csv/product_data.csv"

while True:
    product_data = get_product_data()

    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=product_data.keys())

        writer.writeheader()

        writer.writerow(product_data)

    choice = input("Do you want to enter data for another product? (yes/no): ")
    if choice.lower() != 'yes':
        break

print(f"Product data exported to {csv_filename}")
import math
import random
# from collections import deque


def bot_select_from_outer_layer(matrix):
    outer_layer = []

    outer_layer.extend(matrix[0])
    outer_layer.extend(matrix[-1])
    outer_layer.extend(matrix[i][0] for i in range(1, len(matrix) - 1))
    outer_layer.extend(matrix[i][-1] for i in range(1, len(matrix) - 1))
    return random.choice(outer_layer)

def choose_random_number_in_matrix(matrix):
    flat_matrix = [number for sublist in matrix for number in sublist]
    return random.choice(flat_matrix)


# Example usage:
num = int(input("Enter a number:"))

row = int(math.sqrt(num))
column = math.ceil(num / row)
print("Row: ",row)
print("Column: ",column)


matrix = [[random.randint(1, 100) for _ in range(column)] for _ in range(row)]

print("Matrix:")
for r in matrix:
    print(r)

bot_number = bot_select_from_outer_layer(matrix)
print("Selected number from outer layer:", bot_number)

number_to_find = choose_random_number_in_matrix(matrix)
print("Destination Number:", number_to_find)







def find_path(matrix, bot_number, number_to_find):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    visited = [[False] * num_cols for _ in range(num_rows)]
    visited_count = 0

    # Find the starting position of the bot_number
    start_row, start_col = None, None
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == bot_number:
                start_row, start_col = row, col
                break
        if start_row is not None:
            break

    if start_row is None:
        print("Bot number not found in the matrix.")
        return None
    
    current_row, current_col = start_row, start_col
    path = [matrix[current_row][current_col]]

    while matrix[current_row][current_col] != number_to_find:
        visited[current_row][current_col] = True
        visited_count += 1

        adjacent = find_adjacent(matrix, current_row, current_col)
        min_distance = float('inf')
        next_row, next_col = None, None

        for r, c in adjacent:
            if not visited[r][c]:
                distance = abs(matrix[r][c] - number_to_find)
                if distance < min_distance:
                    min_distance = distance
                    next_row, next_col = r, c
        
        if next_row is None or next_col is None:
            print("Number {} not found in the matrix reachable from bot number {}.".format(number_to_find, bot_number))
            return None
        
        current_row, current_col = next_row, next_col
        path.append(matrix[current_row][current_col])

    return path

def find_adjacent(matrix, row, col):
    adjacent = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Check adjacent elements to the left, right, up, down, and diagonals
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            adjacent.append((new_row, new_col))
    
    return adjacent

path = find_path(matrix, bot_number, number_to_find)
if path:
    print("Path found:", path)
else:
    print("No path found to the destination number.")
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

# %%
import NRB_Forex
import re
from datetime import datetime

def fetch_forex_data(date):
    forex_data = NRB_Forex.get_forex_rates(date)
    if forex_data:
        return forex_data
    else:
        print("Failed to fetch FOREX data for", date)
        return None

# Todays Date
today_date = datetime.now().strftime("%Y-%m-%d")
today_forex_data = fetch_forex_data(today_date)
print("Today's FOREX data:", today_forex_data)

# Past Date
past_date_input = input("Enter the date (YYYY-MM-DD) for past FOREX data: ")
past_dates_extracted = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', past_date_input)
if past_dates_extracted:
    past_date = past_dates_extracted[0]
    past_forex_data = fetch_forex_data(past_date)
    print("Past FOREX data:", past_forex_data)
else:
    print("Invalid date format. Please enter date in YYYY-MM-DD format.")


# %%
import re

# Convert the forex data dictionaries to strings

today_forex_str = str(today_forex_data)
past_forex_str = str(past_forex_data)


# Regex pattern to extract currency ISO code, name, and unit
pattern = r"'iso3':\s*'(\w+)'.*?'name':\s*'([^']*)'.*?'unit':\s*([^,}]+)"


# Find currency ISO code, name, and unit in today's forex data
pattern_data_today = re.findall(pattern, today_forex_str)

# Find currency ISO code, name, and unit in past forex data
pattern_data_past = re.findall(pattern, past_forex_str)


def extract_currency_data(forex_data, currency_iso):
    currency_data = None
    for payload in forex_data['data']['payload']:
        for rate in payload['rates']:
            if rate['currency']['iso3'] == currency_iso:
                currency_data = rate
                break
        if currency_data:
            break
    return currency_data


currencies_data = [currency[0] for currency in pattern_data_past]

user_input = input("Which Currency?")

user_input_tokens = user_input.split()
upper_user_input_tokens = [token.upper() for token in user_input_tokens]

currency = list(set(upper_user_input_tokens) & set(currencies_data))

if currency:
    today_currency_data = extract_currency_data(today_forex_data, currency[0])
    past_currency_data = extract_currency_data(past_forex_data, currency[0])
    
    if today_currency_data and past_currency_data:
        print(f"{currency[0]} ({pattern_data_today[currencies_data.index(currency[0])][1]}) Data:")
        print("Today's:")
        print("Buy:", today_currency_data['buy'])
        print("Sell:", today_currency_data['sell'])
        print("Unit:", pattern_data_today[currencies_data.index(currency[0])][2])
        print("Past:")
        print("Buy:", past_currency_data['buy'])
        print("Sell:", past_currency_data['sell'])
        print("Unit:", pattern_data_past[currencies_data.index(currency[0])][2])
    else:
        print(f"{currency[0]} data not found.")
else:
    print("Currency not found in the available data.")


# %%
def calculate_unit_price(buy, sell, unit):
    unit_buy = float(buy) / unit
    unit_sell = float(sell) / unit
    return unit_buy, unit_sell

currency = list(set(upper_user_input_tokens) & set(currencies_data))

if currency:
    today_currency_data = extract_currency_data(today_forex_data, currency[0])
    past_currency_data = extract_currency_data(past_forex_data, currency[0])
    
    if today_currency_data and past_currency_data:
        today_unit = int(pattern_data_today[currencies_data.index(currency[0])][2])
        past_unit = int(pattern_data_past[currencies_data.index(currency[0])][2])

        today_unit_buy, today_unit_sell = calculate_unit_price(today_currency_data['buy'], today_currency_data['sell'], today_unit)
        past_unit_buy, past_unit_sell = calculate_unit_price(past_currency_data['buy'], past_currency_data['sell'], past_unit)

        user_input_amount = 200

        today_user_buy = user_input_amount * today_unit_buy
        today_user_sell = user_input_amount * today_unit_sell
        past_user_buy = user_input_amount * past_unit_buy
        past_user_sell = user_input_amount * past_unit_sell

        print("Today's Data:")
        print(f"Today Rate {currency[0]} (BUY) for {user_input_amount}:", today_user_buy)
        print(f"Today Rate {currency[0]} (Sell) for {user_input_amount}:", today_user_sell)

        print("\nPast Data:")
        print(f"Past Rate (BUY) for {user_input_amount} :", past_user_buy)
        print(f"Past Rate (Sell) for {user_input_amount} :", past_user_sell)
    else:
        print(f"{currency[0]} data not found.")
else:
    print("Currency not found in the available data.")


# %%
# Plotting
import matplotlib.pyplot as plt
labels = ['Today Buy', 'Today Sell', 'Past Buy', 'Past Sell']
values = [today_user_buy, today_user_sell, past_user_buy, past_user_sell]

plt.bar(labels, values, color=['blue', 'orange', 'green', 'red'])
plt.xlabel('Rates')
plt.ylabel('Amount')
plt.title(f'{currency[0]} Currency Rates')
plt.show()

# %%
# Calculate percentage increase or decrease for buying
buy_increase = ((today_user_buy - past_user_buy) / past_user_buy) * 100
buy_decrease = ((past_user_buy - today_user_buy) / past_user_buy) * 100

# Calculate percentage increase or decrease for selling
sell_increase = ((today_user_sell - past_user_sell) / past_user_sell) * 100
sell_decrease = ((past_user_sell - today_user_sell) / past_user_sell) * 100

# Display results
print("\nPercentage Change:")
if today_user_buy > past_user_buy:
    print(f"Buy rate increased by: {buy_increase:.2f}%")
else:
    print(f"Buy rate decreased by: {buy_decrease:.2f}%")

if today_user_sell > past_user_sell:
    print(f"Sell rate increased by: {sell_increase:.2f}%")
else:
    print(f"Sell rate decreased by: {sell_decrease:.2f}%")


# %%

# Plotting
plt.figure(figsize=(10, 5))

# Plotting buying rates
plt.subplot(1, 2, 1)
plt.bar(['Today Buy', 'Past Buy'], [today_user_buy, past_user_buy], color=['blue', 'orange'])
plt.xlabel('Rates')
plt.ylabel('Amount')
plt.title('Buying Rates')

# Plotting selling rates
plt.subplot(1, 2, 2)
plt.bar(['Today Sell', 'Past Sell'], [today_user_sell, past_user_sell], color=['green', 'red'])
plt.xlabel('Rates')
plt.ylabel('Amount')
plt.title('Selling Rates')

plt.tight_layout()
plt.show()

# Plotting percentage change
plt.figure(figsize=(5, 5))
labels = ['Buy Increase', 'Buy Decrease', 'Sell Increase', 'Sell Decrease']
values = [buy_increase, buy_decrease, sell_increase, sell_decrease]
plt.bar(labels, values, color=['blue', 'orange', 'green', 'red'])
plt.xlabel('Rates')
plt.ylabel('Percentage Change')
plt.title('Percentage Change in Buying and Selling Rates')
plt.show()


import re
import json
import os

# Define the file path for the brain.json file
BRAIN_FILE_PATH = "Task_11 NLP ML/brain.json"

# Load the bot's brain from the JSON file
def load_brain():
    if os.path.exists(BRAIN_FILE_PATH):
        with open(BRAIN_FILE_PATH, "r") as file:
            return json.load(file)
    else:
        print("AI: Brain data not found. Please provide initial brain data in 'brain.json'.")
        return {}

def save_brain(brain):
    with open(BRAIN_FILE_PATH, "w") as file:
        json.dump(brain, file, indent=4)
        print("AI: Brain has been updated and saved.")

# Extract numbers and operation based on known terms in the brain
def extract_numbers_and_operation(statement, brain):
    numbers = list(map(float, re.findall(r'\b\d+(?:\.\d+)?\b', statement)))
    operation = None

    for term, operation_name in brain.items():
        if term in statement:
            operation = operation_name
            break

    return numbers, operation

def perform_calculation(numbers, operation):
    if operation == "addition":
        result = sum(numbers)
    elif operation == "subtraction":
        result = numbers[0] - sum(numbers[1:])
    elif operation == "multiplication":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "division":
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
        except ZeroDivisionError:
            result = "Error: Division by zero."
    else:
        result = None

    return result

def ai_bot():
    brain = load_brain()
    print("Loaded brain:", brain)
    if not brain:
        return

    print("Hello! I can help you with basic arithmetic calculations.")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ['exit', 'quit']:
            print("AI: Goodbye!")
            break

        numbers, operation = extract_numbers_and_operation(user_input, brain)

        if not numbers:
            print("AI: I didn't find any numbers in your statement. Please provide numbers for the calculation.")
            continue

        if not operation:
            print("AI: I am confused, tell me which calculation you would like to perform (e.g., addition, subtraction, multiplication, division).")
            clarification = input("You: ").strip().lower()

            if clarification:
                print(f"AI: Could you explain what '{clarification}' means (e.g., addition, subtraction, multiplication, division)?")
                definition = input("You: ").strip().lower()
                
                brain[clarification] = definition
                save_brain(brain)
                print(f"AI: I have learned that '{clarification}' means '{definition}'. I will remember this for future calculations.")
                # Re-extract numbers and operation after learning new term
                numbers, operation = extract_numbers_and_operation(user_input, brain)

        result = perform_calculation(numbers, operation)

        if result is not None:
            print(f"AI: The result of the {operation} is: {result}")
        else:
            print("AI: I am still confused. Could you please clarify your request?")

# Run the AI bot
ai_bot()
  


Week 	Tasks
Week 1:	•	Set up development environment for backend projects.
•	Installed necessary tools such as Python, IDE (Vs Code), Django framework, and libraries.
•	Completed tutorials on Python basics and data manipulation.
•	Attended orientation sessions and familiarized myself with team members and project goals.
Week 2:	•	Learned about Web scraping, read/write files.
•	Work on a task to scrap data from Jobs Nepal website to gain some useful sights.
•	Implemented User-Agent header for HTTP requests to prevent website blocking.
•	Scrapped data using Beautiful Soup, later for more efficient extraction used regex and urllib to extract multiple pages data. 
•	Data is extracted and submitted in CSV format to my mentor.
Week 3:	•	Learned about Faker, file read/write/split.
•	Scrapped country data’s, forex data, currencies data, merged with faker data.
•	Further perform demographic analysis, contact management, skill assessment, and financial operations.
Week 4:	•	Scrapped historical/current gold and silver prices, Nepal location data, bank interest rates, and NEPSE data for investment analysis.
•	Analyzed and predicted potential returns on investments using the collected data.
•	Used regression model to forecast future earnings based on trends in gold, silver, bank interest rates.
Week 5:	•	Implemented chatbot functionalities using SpaCy and Levenshtein distance.
•	Matched user input with stored relations and generated responses based on matching criteria.
•	Managed query counts and provided appropriate responses based on user interactions.
Week 6:	•	Collect and review data on demolition activities at Gaushala Chowk.
•	Identify stakeholders, evaluate impact on traffic, community, and regulatory compliance, also forecast investment opportunities in real estate, infrastructure, and legal services.
•	Present findings and strategic recommendations based on analysis.
•	Created a Program that map x employees to y tech companies' where only z vacancies are available based on skills and time-availability preferences.
Week 7:	•	Understanding how to create and manipulate matrices and random number generation.
•	Develop a pathfinding algorithm to navigate from a starting number to a destination number within the matrix, using adjacency checks and heuristic methods.
Week 8:	•	Mastering web scraping techniques for both static tables and dynamic AJAX data.
•	Listing all banks and importing yearly turnover data, interest rates, commodities prices (gold, silver, copper, brass, oil, wheat, rice), Forex rates, and share prices for the past 5 years.
•	Scraping temporal data from various websites using regular expressions.
Week 10:	•	Learned and implemented regex to extract patterns and keywords from text, mapping them to operations.
•	Performed arithmetic operations based on extracted keywords and numbers.
•	Preprocessed text data, built, and trained a text classification model using TensorFlow.
•	Created a function to predict labels for new user inputs.
•	Loaded and manipulated data using Pandas, transforming labels for classification. 
Week 11:	•	Assigned a task to supply forex API in cashflow management app.
•	Analyzed NRB forex API documentation, parameters, request, responses to develop api.py and successfully tested and verified the working of the API.
•	Coordinated with colleagues of Frontend to integrate the API.
•	Supply various data like bank interest, share bazar, commodities etc previously scrapped to frontend interns for cashflow webapp development.
Week 12:	•	Tasked with developing a Django backend, creating an API, and subsequently integrating it with React.js for the NG Investment project.
•	Develop a Django backend, integrated with forex API, bank interest/loan rates, creating business houses, analyzing business houses income, expenses, ROI, etc.


Analysis task
# Learning Reinforcement

## Concept Overview

Learning Reinforcement is a process where initial mistakes are allowed during the learning phase to train entities not to repeat them. However, once learning transitions to reinforcement, strict adherence to established rules is mandatory unless critical tasks occur. It's an ongoing process to teach entities to follow rules and reward them based on their performance. The aim is to train entities to execute tasks effectively.

## Key Principles

1. **Mistake Tolerance During Learning**: Mistakes are part of the learning process and are acceptable during the initial stages but rules are to be followed at all times.
   
2. **Strict Rule Commitment During Reinforcement**: Once in the reinforcement phase, rules must be followed.

3. **Pre-broadcasted Rules**: The rules must be communicated to all relevant parties who can influence the entity's path to achievement.

## Process

### Objective Achievement

An entity (individual, organization, thread, etc.) aims to achieve certain objectives by following established rules and regulations. During this journey, the entity may face obstacles or may proceed without interference.

### Handling Obstacles

When an obstacle is encountered, there are two possible responses:
1. **Enforce Rules on the Obstacle**: 
   - Make the obstructing entity aware of the rules.
   - Encourage them to change their direction by understanding and adhering to the rules.
2. **Change Own Direction**:
   - The entity may change its own direction only under critical conditions where reinforcing the rules on the obstruction is not viable.

## Solution
To prevent obstacles, the best approach is to perform tasks simultaneously rather than concurrently. This method decreases the chance of bottlenecks and interruptions, thereby lowering costs. Pre-communicating rules ensures all parties are informed and accountable, creating a proactive environment that aims to prevent disruptions and maintain smooth operations.

## Examples

### Example 1: Balen Shah, Mayor of Kathmandu, Nepal
Balen Shah enforces rules on those who obstruct progress. He educates the obstructing parties about the rules and regulations, helping them understand why their actions are obstructive and encouraging compliance.
He enforces rules on those who obstruct. Anyone blocking the path is encouraged to understand and follow regulations through relearning or reassessment. This is crucial for societal improvement, maintaining discipline, and ensuring everyone adheres to established rules.
"As he said, 'We cannot give notices to all 2.5 lakh houses,' 'Do I have to carry your house map with me?'" He emphasizes the importance of being aware of one's surroundings, understanding administrative rules and regulations, self-learning and operating within those boundaries. Failure to comply may result in termination or consequences.

### Example 2: Trainee
Trainee implementing the concepts of learning reinforcement to gain knowledge during learning hour and implementing them practically in project or work environments.

### Example 3: Dog Training
Teaching a dog to sit illustrates reinforcement learning: Initially, it explores different responses to the command "sit". When it sits correctly, immediate rewards reinforce this behavior. Over time, the dog learns to consistently sit upon command to receive rewards, demonstrating effective learning through reinforcement.

another analysis 
Here's a list of the key data extracted from the article:

1. **Event**: Demolition of houses and shops built by encroaching on the roadside.
2. **Location**: Gaushala Chowk, Kathmandu.
3. **Date of Event**: May 19, 2024.
4. **Authority Involved**: Kathmandu Metropolitan City Office.
5. **Campaign Led By**: Mayor Balen Shah.
6. **Number of Bulldozers Used**: Four. 4
7. **Impact on Traffic**: Traffic disruption caused.
8. **Police Chief**: Rajunath Pandey.
9. **Initial Demolition**: Six houses on the first day.
10. **Notice Period Given**: 35 days.
11. **Public Announcements Duration**: 15 days.
12. **Historical Context**: Encroachment issue dates back to 2035.
13. **Number of Additional Structures to be Demolished**: 32 temporary towers and shutters.

# KMC Skill Fair 2024

## Overview
The KMC Skill Fair 2024 is an initiative by the Kathmandu Metropolitan City (KMC) aimed at providing vocational training to over 2,000 individuals to enhance employment opportunities. The fair, launched on May 1, 2024, coincides with International Workers' Day and offers free training in various high-demand professions. 

## Objectives
- Provide free vocational training to 2,081 individuals.
- Address the gap between the demand and supply of skilled manpower.
- Transition individuals from the informal sector to the formal economy.
- Connect education with skills, skills with labor, and labor with production.
- Increase employment and self-employment opportunities.
- Enhance professional levels and income for employed individuals without skills.

## Training Details
### Training Areas
1. **Automobiles**: Auto Electric, Auto Air Conditioning, Motorcycle and Scooter Repair (EV), Electrical Car Repair (EV).
2. **Construction Sector**: Carpentry, Tile and Marble Fitting, Electrician, Plumbing.
3. **Hospitality and Management**: Barista, Food and Cook, Waiter, Bartending, Waiter/Waitress.
4. **Information Technology**: Digital Marketing, Graphics Designing, Computer Hardware and Networking, CCTV Camera Installation.
5. **Mechanical**: Welding, Refrigerator and AC Technicians.
6. **Art and Culture**: Art and Culture training.
7. **Garments**: Tailoring and Fashion Designing.
8. **Beautician**: Nail Art, Makeup Art, Eyelash Art, Hair Cutting and Styling, Salon Training.
9. **Designing**: Sign Making.
10. **Priesthood**: Priestly and Astrology Training.

### Key Data
- **Total Applicants**: Over 10,000
- **Initial Trainees**: 2,081 individuals
- **Extended Training**: Over the next three years for remaining applicants
- **Cyber Security Training**: 4,000 people

## Collaboration
The fair is organized in collaboration with various organizations, including:
- Higher Institutions and Secondary Schools' Association Nepal (HISSAN)
- Confederation of Nepalese Industries (CNI)
- Nepal Training and Employment Trade Federation of Nepal (FP-TEN)
- Glocal
- Sipradi Trading
- CCTV Station
- Smart Home

## Key Dates
- **Fair Start Date**: May 1, 2024
- **Training Schedule Provided By**: May 10, 2024

## Eligibility
- **Age**: Participants must be between 18 and 58 years old.

## Application Process
- **Online**: Fill out the form on the official KMC website.
- **In-Person**: Forms can also be filled at ward offices and Tundikhel on the opening day.

## Final Event
A job fair will be organized on the final day of the training where employers will set up stalls. Trained individuals will have the opportunity to connect with prospective employers, showcasing their skills and qualifications.





Week 	Tasks
Week 1:	•	Set up development environment for backend projects.
•	Installed necessary tools such as Python, IDE (Vs Code), Django framework, and libraries.
•	Completed tutorials on Python basics and data manipulation.
•	Attended orientation sessions and familiarized myself with team members and project goals.
Week 2:	•	Learned about Web scraping, read/write files.
•	Work on a task to scrap data from Jobs Nepal website to gain some useful sights.
•	Implemented User-Agent header for HTTP requests to prevent website blocking.
•	Scrapped data using Beautiful Soup, later for more efficient extraction used regex and urllib to extract multiple pages data. 
•	Data is extracted and submitted in CSV format to my mentor.
Week 3:	•	Learned about Faker, file read/write/split.
•	Scrapped country data’s, forex data, currencies data, merged with faker data.
•	Further perform demographic analysis, contact management, skill assessment, and financial operations.
Week 4:	•	Scrapped historical/current gold and silver prices, Nepal location data, bank interest rates, and NEPSE data for investment analysis.
•	Analyzed and predicted potential returns on investments using the collected data.
•	Used regression model to forecast future earnings based on trends in gold, silver, bank interest rates.
Week 5:	•	Implemented chatbot functionalities using SpaCy and Levenshtein distance.
•	Matched user input with stored relations and generated responses based on matching criteria.
•	Managed query counts and provided appropriate responses based on user interactions.
Week 6:	•	Collect and review data on demolition activities at Gaushala Chowk.
•	Identify stakeholders, evaluate impact on traffic, community, and regulatory compliance, also forecast investment opportunities in real estate, infrastructure, and legal services.
•	Present findings and strategic recommendations based on analysis.
•	Created a Program that map x employees to y tech companies' where only z vacancies are available based on skills and time-availability preferences.
Week 7:	•	Understanding how to create and manipulate matrices and random number generation.
•	Develop a pathfinding algorithm to navigate from a starting number to a destination number within the matrix, using adjacency checks and heuristic methods.
Week 8:	•	Mastering web scraping techniques for both static tables and dynamic AJAX data.
•	Listing all banks and importing yearly turnover data, interest rates, commodities prices (gold, silver, copper, brass, oil, wheat, rice), Forex rates, and share prices for the past 5 years.
•	Scraping temporal data from various websites using regular expressions.
Week 10:	•	Learned and implemented regex to extract patterns and keywords from text, mapping them to operations.
•	Performed arithmetic operations based on extracted keywords and numbers.
•	Preprocessed text data, built, and trained a text classification model using TensorFlow.
•	Created a function to predict labels for new user inputs.
•	Loaded and manipulated data using Pandas, transforming labels for classification. 
Week 11:	•	Assigned a task to supply forex API in cashflow management app.
•	Analyzed NRB forex API documentation, parameters, request, responses to develop api.py and successfully tested and verified the working of the API.
•	Coordinated with colleagues of Frontend to integrate the API.
•	Supply various data like bank interest, share bazar, commodities etc previously scrapped to frontend interns for cashflow webapp development.
Week 12:	•	Tasked with developing a Django backend, creating an API, and subsequently integrating it with React.js for the NG Investment project.
•	Develop a Django backend, integrated with forex API, bank interest/loan rates, creating business houses, analyzing business houses income, expenses, ROI, etc.




























Data Collection and Preprocessing:
•	Utilized Python libraries such as regex, Beautiful Soup and urllib for web scraping.
•	Cleaned and preprocessed data using File I/O, Pandas and NumPy.
•	Handled missing data, outliers, and applied feature scaling where necessary.
Natural Language Processing (NLP) Tasks:
Data Handling and Preprocessing:
•	Processed and prepared textual data using Python and Pandas.
•	Applied tokenization and sequence padding with TensorFlow's NLP libraries.
Model Development and Training:
•	Developed neural network models with TensorFlow and Keras.
•	Trained models for binary classification tasks, evaluating with accuracy and loss metrics.
Algorithm Implementation and Integration:
•	Implemented arithmetic algorithms using Python's regex (re module).
•	Integrated algorithms into an AI bot for interactive usage.
File Management and Documentation:
•	Managed JSON files for data storage.
•	Documented code comprehensively with structured comments for clarity.



•	Web scraping
•	Analysis gausala analysis, learning reinforcement, kmc training programs.
•	Regression to prediction
•	Nlp
•	Classification, clustering, prediction
•	Extensive use of regular expression : for scraping, number extraction for arithmentic calculations.
•	Algorithm development 
•	Scraping temporal data ranging from 5 years,  nepse, forex etc.
•	Team up with frontend developers to supply all data available.

