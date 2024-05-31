import csv

# Define the CSV filename
csv_filename = "Task_8 Completed/csv/product_data.csv"
tokenized_product_data = []
original_product_data = []

# Function to tokenize a string value
def tokenize(value):
    return value.strip().lower().split()

# Read and tokenize the CSV file
with open(csv_filename, mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Read the header
    for row in reader:
        original_product_data.append(row)  # Keep the original row for better output later
        tokenized_row = []
        for value in row:
            tokenized_row.extend(tokenize(value))
        tokenized_product_data.append(tokenized_row)

# Print the tokenized data for verification (optional)
# for row in tokenized_product_data:
#     print(row)

def format_reply(matched_rows):
    if not matched_rows:
        return "Sorry, no matching products found in the database."
    
    reply = "Matching products found:\n"
    for row in matched_rows:
        reply += ', '.join(row) + '\n'
    return reply

while True:
    keyword = input("Enter the sentence (or 'exit' to quit): ")

    if keyword.lower() == "exit":
        print("Exiting the program...")
        break

    input_tokens = tokenize(keyword)
    # print(f"Tokenized input: {input_tokens}")

    matching_rows = [
        original_product_data[idx] for idx, row in enumerate(tokenized_product_data)
        if any(token in row for token in input_tokens)
    ]
    
    reply = format_reply(matching_rows)
    print(reply)
