import csv
import io
import re

# Define the CSV data
csv_data = """Product Name,Cost,Category,Color,Container
cheese popcorn,200.0,junk food,yellow,plastic
Tomato,35.0,vegetable,red,plastic
Tomato Small(Tunnel),50.0,vegetable,red,plastic
Tomato Small(Indian),29.0,vegetable,red,plastic
Tomato Small(Terai),45.0,vegetable,red,plastic
Potato Red,55.0,vegetable,red,plastic"""

tokenized_product_data = []
original_product_data = []

# Function to tokenize a string value
def tokenize(value):
    return value.strip().lower().split()

# Read and tokenize the CSV data
file = io.StringIO(csv_data)
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

def extract_product_and_quantity(user_input):
    pattern = re.compile(r'(\d+)\s*packet\s*(.*)', re.IGNORECASE)
    match = pattern.search(user_input)
    if match:
        quantity = int(match.group(1))
        product_name = match.group(2).strip()
        return product_name, quantity
    return None, None

def find_product_cost(product_name):
    product_name_tokens = tokenize(product_name)
    for idx, row in enumerate(tokenized_product_data):
        if all(token in row for token in product_name_tokens):
            return float(original_product_data[idx][1])  # Assuming cost is the second column
    return None

def format_reply(product_name, quantity, total_cost):
    if total_cost is None:
        return f"Sorry, {product_name} is not available in the database."
    return f"Sure, it will cost {quantity} * {total_cost / quantity} = {total_cost:.2f}"

while True:
    keyword = input("Enter the sentence (or 'exit' to quit): ")

    if keyword.lower() == "exit":
        print("Exiting the program...")
        break

    product_name, quantity = extract_product_and_quantity(keyword)
    if product_name and quantity:
        cost_per_unit = find_product_cost(product_name)
        if cost_per_unit is not None:
            total_cost = cost_per_unit * quantity
        else:
            total_cost = None
        reply = format_reply(product_name, quantity, total_cost)
    else:
        reply = "Invalid input format. Please enter the sentence in the format: '<quantity> packet <product name>'."

    print(reply)
