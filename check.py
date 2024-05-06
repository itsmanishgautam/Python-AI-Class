import urllib.request
import bs4
from bs4 import BeautifulSoup
import csv

# User agent header
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# List to store URLs
urls = []

# Iterate over pages 1 to 13
for page_num in range(1, 14):
    url = f'https://www.jobsnepal.com/jobs?page={page_num}'
    urls.append(url)

# Initialize empty lists to store data
job_titles = []
companies = []
locations = []
categories = []

# Iterate over each URL
for url in urls:
    # Send a request with the user agent header
    request = urllib.request.Request(url, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    html_content = response.read().decode('utf-8')

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all job title elements
    title_elements = soup.find_all('h2', class_='job-title')
    for title_element in title_elements:
        job_titles.append(title_element.text.strip())

    # Find all company elements
    company_elements = soup.find_all('div', class_='company-logo')
    for company_element in company_elements:
        companies.append(company_element.a.get('title'))

    # Find all location elements
    location_elements = soup.find_all('i', class_='icon-location4')
    for location_element in location_elements:
        locations.append(location_element.find_next_sibling('div').text.strip())

    # Find all category elements
    category_elements = soup.find_all('div', class_='icon-price-tags')
    for category_element in category_elements:
        categories.append(category_element.find_next('div').text.strip())

# Create a list of tuples containing job data
data = list(zip(job_titles, companies, locations, categories))

# Define the CSV file path
csv_file = 'job_data.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Company', 'Location', 'Category'])  # Write header row
    writer.writerows(data)  # Write data rows

print(f'Data exported to {csv_file}')
