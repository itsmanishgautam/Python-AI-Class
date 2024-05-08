from faker import Faker
import csv
import random
import pandas as pd

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


def merge_csv(df1,df2):
    merged_df = pd.concat([df1, df2], axis=1)
    merged_df.to_csv("csv/merged_Courses_output.csv", index=False)



def split_csv(input_file):
    output_files = ['output1.csv', 'output2.csv', 'output3.csv']

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

    df1 = pd.read_csv("csv/fake_data.csv")
    df2 = pd.read_csv("csv/Courses.csv")
    merge_csv(df1,df2)

    input_file = 'csv/merged_Courses_output.csv'
    split_csv(input_file)
    print("Fake data generated and CSV file split completed.")
