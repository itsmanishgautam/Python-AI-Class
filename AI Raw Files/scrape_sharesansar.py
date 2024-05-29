import re
import urllib.request
import urllib.parse
import datetime
import csv

# Function to fetch HTML content from a given URL with optional parameters
def fetch_html(url, params=None):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    if params:
        url += '?' + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={'User-Agent': user_agent})
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')

# Function to extract share prices from HTML content
def parse_share_prices(html_content, date):
    thead_pattern = r'<thead>(.*?)</thead>'
    thead_data = re.findall(thead_pattern, html_content, re.DOTALL)
    head_data_all = []
    for data in thead_data:
        head_data = re.findall(r'<th.*?>(.*?)</th>', data, re.DOTALL)
        head_data_all.extend(head_data)

    tbody_pattern = r'<tbody>(.*?)</tbody>'
    tbody_data = re.findall(tbody_pattern, html_content, re.DOTALL)
    matches_data_all = []
    for data in tbody_data:
        matches_data = re.findall(r'<td.*?>(.*?)</td>', data, re.DOTALL)
        matches_data_all.extend(matches_data)

    sublists = [matches_data_all[i:i+21] for i in range(0, len(matches_data_all), 21)]
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

    pattern = r'title="([^"]+)"[^>]*>([^<]+)<\/a>'
    matches = re.findall(pattern, ''.join(Symbol))

    names = []
    symbols_list = []

    for name, symbol in matches:
        names.append(name)
        symbols_list.append(symbol)

    return [(date, name, symbol, conf, open_, high, low, close, vwap, vol, prev_close, turnover, trans, diff, range_, diff_percent, range_percent, vwap_percent, days_120, days_180, weeks_high, weeks_low) for name, symbol, conf, open_, high, low, close, vwap, vol, prev_close, turnover, trans, diff, range_, diff_percent, range_percent, vwap_percent, days_120, days_180, weeks_high, weeks_low in zip(names, symbols_list, Conf, Open, High, Low, Close, VWAP, Vol, Prev_Close, Turnover, Trans, Diff, Range, Diff_Percent, Range_Percent, VWAP_Percent, Days_120, Days_180, Weeks_High, Weeks_Low)]

# Function to generate dates between two date ranges
def date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += datetime.timedelta(days=1)

# Main script to scrape data over the past 5 years and save to CSV
def main():
    start_date = datetime.date(2024, 5, 1)
    end_date = datetime.date(2024, 5, 3)
    csv_filename = "nepse.csv"
    
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Name', 'Symbol', 'Conf', 'Open', 'High', 'Low', 'Close', 'VWAP', 'Vol', 'Prev. Close', 'Turnover', 'Trans', 'Diff', 'Range', 'Diff %', 'Range %', 'VWAP %', '120 Days', '180 Days', '52 Weeks High', '52 Weeks Low'])

        for single_date in date_range(start_date, end_date):
            formatted_date = single_date.strftime('%Y-%m-%d')
            params = {'date': formatted_date}
            html_content = fetch_html('https://www.sharesansar.com/today-share-price', params)
            share_prices = parse_share_prices(html_content, formatted_date)
            for row in share_prices:
                writer.writerow(row)

    print("CSV file exported successfully.")

if __name__ == "__main__":
    main()
