import os
import json
import Levenshtein
import random

# Load JSON file data
with open('Task_4/Kaggle Dataset/data.json', 'r') as file:
    data = json.load(file)

def calculate_similarity(input_str, query):
    return Levenshtein.distance(input_str.lower(), query.lower())

def generate_response(user_input, query_counts):
    # Load query counts
    if os.path.exists("Task_4/Kaggle Dataset/query_counts.txt"):
        with open("Task_4/Kaggle Dataset/query_counts.txt", "r") as file:
            query_counts = eval(file.read())

    # Fetch the irritated responses from the JSON data
    irritated_responses = [response for intent in data['intents'] if intent['tag'] == 'irritated_responses' for response in intent['responses']]
    
    similar_queries = [query for query in query_counts.keys() if calculate_similarity(user_input, query) <= 2]
    if similar_queries:
        query = max(similar_queries, key=lambda x: query_counts[x])
        query_counts[query] += 1
        response = random.choice(irritated_responses)
    
    else:
        best_similarity = float('inf')
        best_response = None
        
        for intent in data['intents']:
            for pattern in intent['patterns']:
                similarity = calculate_similarity(user_input, pattern)
                if similarity < best_similarity:
                    best_similarity = similarity
                    best_response = random.choice(intent['responses'])
        
        if best_similarity <= 2:
            response = best_response
        else:
            response = "I'm sorry, I don't understand that."

    # Update query counts
    query_counts[user_input.strip().lower()] = query_counts.get(user_input.strip().lower(), 0) + 1

    # Save query counts
    with open("Task_4/Kaggle Dataset/query_counts.txt", "w") as file:
        file.write(str(query_counts))

    return response

# ChatBot Loop
print("Welcome to the Chatbot!")
query_counts = {}

while True:
    user_input = input("You: ").lower()
    if user_input in ['quit', 'bye', 'goodbye']:
        break 
    else:
        response = generate_response(user_input, query_counts)
        print("Bot:", response)

# Remove the query_counts.txt file after chatbot loop
if os.path.exists("Task_4/Kaggle Dataset/query_counts.txt"):
    os.remove("Task_4/Kaggle Dataset/query_counts.txt")
