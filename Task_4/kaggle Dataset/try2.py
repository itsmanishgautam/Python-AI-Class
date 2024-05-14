import os
import json
import Levenshtein
import random

with open('Task_4/Kaggle Dataset/data.json', 'r') as file:
    data = json.load(file)

def calculate_similarity(input_str, query):
    distance = Levenshtein.distance(input_str.lower(), query.lower())
    similarity = 1 - (distance / max(len(input_str), len(query)))
    return similarity

def generate_response(user_input, query_counts):
    if os.path.exists("Task_4/Kaggle Dataset/query_counts.json"):
        with open("Task_4/Kaggle Dataset/query_counts.json", "r") as file:
            query_counts = json.load(file)

    irritated_responses = [response for intent in data['intents'] if intent['tag'] == 'irritated_responses' for response in intent['responses']]

    similar_queries = [query for query in query_counts.keys() if calculate_similarity(user_input, query) > 0.7]  # Adjust similarity threshold as needed

    if similar_queries:
        query = max(similar_queries, key=lambda x: query_counts[x])
        query_counts[query] += 1
        response = random.choice(irritated_responses)
    elif any(user_input in intent['patterns'] for intent in data['intents']):
        for intent in data['intents']:
            for pattern in intent['patterns']:
                if user_input in pattern:
                    response = random.choice(intent['responses'])
                    break
    else:
        response = "I'm sorry, I don't understand that."
    
    query_counts[user_input.strip().lower()] = query_counts.get(user_input.strip().lower(), 0) + 1

    with open("Task_4/Kaggle Dataset/query_counts.json", "w") as file:
        json.dump(query_counts, file)

    return response


# Chatbot loop
print("Welcome to the Chatbot!")
query_counts = {}

while True:
    user_input = input("You: ").lower()
    if user_input in ['quit', 'bye', 'goodbye']:
        break 
    else:
        response = generate_response(user_input, query_counts)
        print("Bot:", response)

if os.path.exists("Task_4/Kaggle Dataset/query_counts.json"):
    os.remove("Task_4/Kaggle Dataset/query_counts.json")
