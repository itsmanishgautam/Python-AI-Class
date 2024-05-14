import json
import re
import random

file_path = 'Task_4/dataset.json'

def load_responses(file_path):
    with open(file_path, "r") as file:
        responses = json.load(file)
    return responses

def tokenize(text):
    tokens = text.lower().split()
    return tokens

def respond(user_input, responses):
    tokens = tokenize(user_input)
    
    for token in tokens:
        for pattern, response_list in responses.items():
            regex_pattern = re.compile(pattern, re.IGNORECASE)  # Compile the pattern
            match = regex_pattern.search(token)
            if match:
                return random.choice(response_list)
    
    return random.choice(responses['irritated_responses'])  # Accessing irritated_responses


responses = load_responses(file_path)

print("Bot: Hello! How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = respond(user_input, responses)
    print("Bot:", response)
