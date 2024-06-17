# README.md

### Overview
This repository contains scripts for retrieving FOREX rates from the Nepal Rastra Bank API and scraping share price data from Sharesansar. The scripts demonstrate web scraping, data extraction, and CSV file creation using Python.

---

### 1. **FOREX Rates Retrieval Script**

#### Description
This script retrieves foreign exchange rates for a specified date from the Nepal Rastra Bank API.

#### Features
- **API Request**: Sends GET requests to the Nepal Rastra Bank API to fetch FOREX rates.
- **Date Input**: Accepts a date input in the format `YYYY-MM-DD` from the user.
- **Error Handling**: Checks for successful responses and handles errors appropriately.

#### Usage
1. Run the script.
2. Enter the date in the format `YYYY-MM-DD` when prompted.
3. The script will display the retrieved FOREX data or an error message if the request fails.

---

### 2. **Share Price Data Scraping Script**

#### Description
This script scrapes share price data from Sharesansar for a specified date.

#### Features
- **CSRF Token Handling**: Retrieves and uses the CSRF token required for making POST requests to the Sharesansar website.
- **HTML Parsing**: Uses BeautifulSoup to parse HTML and extract share price data.
- **Data Structuring**: Organizes extracted data into a structured format.
- **CSV Export**: Saves the structured data into a CSV file.

#### Usage
1. Run the script.
2. Enter the date in the format `YYYY-MM-DD` when prompted.
3. The script will display the extracted data or a message if no records are found.

---

### Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup4` library
- `datetime` library
- `re` library
- `csv` library

---

### Installation

1. Clone this repository.
2. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Run the desired script using Python:
   ```bash
   python forex_rates.py
   ```
   or
   ```bash
   python share_price_scraper.py
   ```

---

### Learning Outcomes

- **FOREX Rates Retrieval Script**: Improved skills in API requests, JSON handling, and error management.
- **Share Price Data Scraping Script**: Enhanced web scraping techniques, HTML parsing with BeautifulSoup, and data structuring for CSV export.

---

### Programmer
Manish Gautam

### Mentor
Dixanta Bahadur Shrestha
CIBT, Kumaripati
