import urllib.request
from bs4 import BeautifulSoup

urls = []

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

for page_num in range(1, 14):
    url = 'https://www.jobsnepal.com/jobs?page=1'


    request = urllib.request.Request(url, headers={'User-Agent': user_agent})

    response = urllib.request.urlopen(request)

    html_content = response.read().decode('utf-8')


    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <div class="col-md-8 px-0 top-content"> elements
    alldata = soup.find_all('div', class_='col-md-8 px-0 top-content')

    title = soup.find_all('h2', class_='job-title')

    job_title = [
        h2.text.strip() for h2 in title]

    print(job_title)

    data = soup.find_all('div', class_='card-inner')

    company = [a.find('a').get('title') for a in data]

    print(company)

    data = soup.find_all('div', class_=['icon-price-tags mr-2 text-success icon-sm', 'd-flex align-items-center pl-1 pr-1 py-1'])


    doubledata = [div.find('div').text.strip() for div in data]

    print(doubledata)

    locations = doubledata[::2]
    categories = doubledata[1::2]

    print("Locations:", locations)
    print("Categories:", categories)

data = list(zip(job_title, company,locations,categories))
import csv
csv_file = 'job_data10.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Title', 'Company', 'Location', 'Category'])
        writer.writerows(data) 

print(f'Data exported to {csv_file}')    


