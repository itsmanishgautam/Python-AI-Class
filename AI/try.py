import urllib.request
import re

url = 'https://www.jobsnepal.com/jobs?page=1'
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
# Fetch the webpage's HTML content
html_content = response.read().decode('utf-8')
print(html_content)


# <div class="col-md-8 px-0 top-content">
# </div>

# Find the start and end index of the content within the specified <div> tag
start_index = html_content.find('<div class="col-md-8 px-0 top-content">')
end_index = html_content.find('</div>', start_index)

# Extract the content within the specified <div> tag
content_html = html_content[start_index:end_index + len('</div>')]

# Print or further process the content HTML
print(content_html)