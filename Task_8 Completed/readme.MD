# Title
This program allows users to enter and store product details in a CSV file (`product_data.csv`). It also provides a search functionality where users can input sentences containing keywords to find and display matching products from the CSV file.

# CSV Data Processing

This Python script demonstrates basic CSV data processing tasks, including reading and tokenizing data from a CSV file, as well as appending new data to the CSV file.

## Tokenizing CSV Data

The script reads a CSV file (`product_data.csv`), tokenizes each value in the CSV rows, and stores both the original and tokenized data for processing.

### Functions:

1. **tokenize(value)**: Tokenizes a string value by stripping leading and trailing spaces, converting to lowercase, and splitting into tokens.

2. **format_reply(matched_rows)**: Formats the matched rows into a human-readable reply string.

### Usage:

1. Run the script.
2. Enter a sentence or keywords to search for matching products in the CSV file.
3. The script will tokenize the input, search for matching rows in the CSV data, and display the matched products.

## Appending Data to CSV

The script allows users to enter product data interactively and appends it to the existing CSV file (`product_data.csv`).

### Functions:

1. **get_product_data()**: Prompts the user to enter product data interactively and returns it as a dictionary.

### Usage:

1. Run the script.
2. Enter product details as prompted.
3. The script will append the entered data to the CSV file.
4. Repeat the process to enter data for additional products.

## Dependencies:

- `csv`: For reading and writing CSV files.

## Programmer
Manish Gautam

## Mentor, Brain
Dixanta Bahadur Shrestha