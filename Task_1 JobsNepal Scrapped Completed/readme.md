# Job Scraping Project

## Overview
This project aims to scrape job listings from the Jobs Nepal website using both BeautifulSoup (for HTML parsing) and regex (for pattern matching in HTML content). It retrieves job titles, company names, locations, and categories from multiple pages of job listings.

## Files
- `jobs_scraping_bs4.py`: Python script using BeautifulSoup for scraping.
- `jobs_scraping_regex.py`: Python script using regex for scraping.
- `csv/Job_data_Soup2.csv`: CSV file containing job data exported using BeautifulSoup.
- `csv/jobs_nepal_regex_scrap.csv`: CSV file containing job data exported using regex.

## Dependencies
- Python 3.x
- Libraries: urllib, BeautifulSoup (for BeautifulSoup scraping)
- Libraries: urllib, re (for regex scraping)

## How to Use
1. Clone the repository or download the files.
2. Ensure Python and required libraries are installed.
3. Run `jobs_scraping_bs4.py` or `jobs_scraping_regex.py` to perform scraping.
4. CSV files (`Job_data_Soup2.csv`, `jobs_nepal_regex_scrap.csv`) will be generated with scraped data.
5. Explore the CSV files for the scraped job listings.

## Notes
- Adjust the range in the for loop (`for page_num in range(1, 15)`) in the scraping scripts to scrape more or fewer pages.
- Ensure proper internet connection and handling of HTTP requests.
- The user-agent header (`User-Agent`) is included to avoid being blocked by the website.

## Programmer
Manish Gautam

## Mentor, Brain
Dixanta Bahadur Shrestha
