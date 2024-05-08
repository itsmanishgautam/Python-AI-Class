from faker import Faker
import csv
import random

fake = Faker()

def generate_fake_data(num_records):
    with open('fake_data.csv', 'w', newline='') as csvfile:
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

def split_csv(input_file):
    output_files = ['output1.csv', 'output2.csv', 'output3.csv']

    writers = {}
    for file_name in output_files:
        writers[file_name] = csv.DictWriter(open(file_name, 'w', newline=''), fieldnames=['Name', 'Contact', 'Country', 'CountryCode'])
        writers[file_name].writeheader()

    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            output_file = random.choice(output_files)
            writers[output_file].writerow(row)



if __name__ == "__main__":
    num_records = 100000
    generate_fake_data(num_records)
    input_file = 'fake_data.csv'
    split_csv(input_file)
    print("Fake data generated and CSV file split completed.")
