import csv
from faker import Faker

# Create a Faker object
fake = Faker()

# Define the number of records to generate
num_records = 100

# Define field names for the CSV file
fieldnames = [
    'Street Address', 'City', 'Zip Code', 'State', 'Country', 'Country Code',
    'Latitude', 'Longitude', 'Company Name', 'Industry Type', 'Catch Phrase',
     'Job Title', 'First Name', 'Last Name', 'Full Name',
    'Date of Birth', 'Age', 'Email', 'Phone Number', 'Social Security Number',
    'Username', 'Domain Name', 'URL', 'IPv4 Address', 'IPv6 Address', 'User Agent',
    'Password', 'Sentence', 'Paragraph', 'Lorem Ipsum Text', 'Word', 'Credit Card Number',
    'Credit Card Expiration Date', 'Credit Card Provider', 'Currency Code', 'Currency Name',
    'Amount', 'Boolean Value', 'File Path', 'Image URL', 'Color Name', 'Language Name',
    'Time Zone', 'City Prefix', 'City Suffix', 'Date', 'Time',
    'Date and Time', 'Python Data Type', 'Python Function Name', 'University Prefix', 'University Suffix',
    
]

# Generate fake data and write to CSV file
with open('fake_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for _ in range(num_records):
        writer.writerow({
            'Street Address': fake.street_address(),
            'City': fake.city(),
            'Zip Code': fake.zipcode(),
            'State': fake.state(),
            'Country': fake.country(),
            'Country Code': fake.country_code(),
            'Latitude': fake.latitude(),
            'Longitude': fake.longitude(),
            'Company Name': fake.company(),
            'Industry Type': fake.bs(),
            'Catch Phrase': fake.catch_phrase(),
            'Job Title': fake.job(),
            'First Name': fake.first_name(),
            'Last Name': fake.last_name(),
            'Full Name': fake.name(),
            'Date of Birth': fake.date_of_birth(),
            'Age': fake.random_int(min=18, max=100),
            'Email': fake.email(),
            'Phone Number': fake.phone_number(),
            'Social Security Number': fake.ssn(),
            'Username': fake.user_name(),
            'Domain Name': fake.domain_name(),
            'URL': fake.url(),
            'IPv4 Address': fake.ipv4(),
            'IPv6 Address': fake.ipv6(),
            'User Agent': fake.user_agent(),
            'Password': fake.password(),
            'Sentence': fake.sentence(),
            'Paragraph': fake.paragraph(),
            'Lorem Ipsum Text': fake.text(),
            'Word': fake.word(),
            'Credit Card Number': fake.credit_card_number(),
            'Credit Card Expiration Date': fake.credit_card_expire(),
            'Credit Card Provider': fake.credit_card_provider(),
            'Currency Code': fake.currency_code(),
            'Currency Name': fake.currency_name(),
            'Amount': fake.random_number(digits=2),
            'Boolean Value': fake.boolean(),
            'File Path': fake.file_path(),
            'Image URL': fake.image_url(),
            'Color Name': fake.color_name(),
            'Language Name': fake.language_name(),
            'Time Zone': fake.timezone(),
            'City Prefix': fake.city_prefix(),
            'City Suffix': fake.city_suffix(),
            'Date': fake.date(),
            'Time': fake.time(),
            'Date and Time': fake.date_time(),
            'Python Data Type': fake.pyint(),
            'Python Function Name': fake.pystr(),
            
            'University Prefix': fake.prefix(),
            'University Suffix': fake.suffix(),
            
        })

print("CSV file generated successfully!")
