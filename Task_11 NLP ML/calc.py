
import re
import json

json_file = "Task_11 NLP ML/keyword_set.json"

with open(json_file, 'r') as file:
    keywords_set = json.load(file)

operations_set = {
    'sum': '+',
    'difference': '-',
    'product': '*',
    'division': '/',
    'power': '**',
}



def extract_keyword(input_text):
    for operation, synonyms in keywords_set.items():
        if any(word in input_text for word in synonyms):
            return operation
    return None

def extract_numbers(input_text):
    number_pattern = r'\d+'
    numbers = re.findall(number_pattern, input_text)
    return numbers



input_text = input("Enter Text: ")
operation = extract_keyword(input_text)

if operation:
    operation_symbol = operations_set.get(operation)
    if operation_symbol:
        numbers = extract_numbers(input_text)
        print(f"Operation: {operation}\nOperation Symbol: {operation_symbol}\nNumbers: {numbers}")
    else:
        print("No operation symbol defined for:", operation)
else:
    print("No operation keyword found in the text.")


num1 = int(numbers[0])
num2 = int(numbers[1])


if operation in operations_set:
    operator = operations_set[operation]
    expression = f"{num1} {operator} {num2}"
    result = eval(expression)
    print(f"The {operation} of {num1} and {num2} is {result}")
else:
    print("Unsupported operation")



