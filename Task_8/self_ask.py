import re
import csv

csv_file = 'Task_8/csv/product_data.csv'

def tokenize(value):
    return value.strip().lower().split()

# user_input= input('what do you want? : ')

def input_token(user_input):
    tokenized_input = tokenize(user_input)
    return tokenized_input

# tokekenized_input = input_token(user_input)
# print(tokekenized_input)


# Read and tokenize the CSV file
# with open(csv_filename, mode='r', newline='') as file:
#     reader = csv.reader(file)
#     headers = next(reader)  # Read the header
#     for row in reader:
#         original_product_data.append(row)  # Keep the original row for better output later
#         tokenized_row = []
#         for value in row:
#             tokenized_row.extend(tokenize(value))
#         tokenized_product_data.append(tokenized_row)

fetched_csv = []

with open(csv_file, mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        fetched_csv.append(row)
        
            
        
        
