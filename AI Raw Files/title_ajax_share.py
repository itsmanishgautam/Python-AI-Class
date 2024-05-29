import urllib.request
import re

def extract_ajax_data(url):
    # Simulate a browser request (replace with actual headers if needed)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    try:
        # Make the request
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read().decode('utf-8')

        # Example regular expression to extract relevant data (adjust based on website structure)
        pattern = r'\{(.*?)\}'  # Captures data within curly braces
        matches = re.findall(pattern, data)

        if matches:
            return matches[0]  # Assuming the first match is the desired data
        else:
            print("No data found using the provided regular expression.")
    except Exception as e:
        print(f"Error occurred: {e}")

# Replace with the actual AJAX endpoint URL
ajax_url = "https://www.sharesansar.com/ajaxtodayshareprice"

extracted_data = extract_ajax_data(ajax_url)

if extracted_data:
    print("Extracted data:", extracted_data)
else:
    print("Data extraction unsuccessful.")
