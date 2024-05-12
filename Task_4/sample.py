import os
import Levenshtein

# Define a function to calculate similarity using Levenshtein distance
def calculate_similarity(input_str, query):
    return Levenshtein.distance(input_str.lower(), query.lower())

# Define a function to process user input and generate responses
def generate_response(user_input):
    # Check if the file exists
    if os.path.exists("query_counts.txt"):
        # Read query counts from the file
        with open("query_counts.txt", "r") as file:
            query_counts = eval(file.read())
    else:
        query_counts = {}

    # Define a list of irritated responses
    irritated_responses = [
        "I've already answered that.",
        "You already asked me that.",
        "Do you enjoy repeating yourself?",
        "I'm starting to get annoyed by your repeated questions."
    ]
    
    # Check if the user input is a repeated query
    similar_queries = [query for query in query_counts.keys() if calculate_similarity(user_input, query) <= 2]
    if similar_queries:
        query = max(similar_queries, key=lambda x: query_counts[x])
        query_counts[query] += 1
        count = query_counts[query]
        
        # Generate an irritated response based on the count of repeated queries
        if count == 3:
            response = "I already told you that. Are you not listening?"
        elif count == 4:
            response = "Seriously? How many times do I have to repeat myself?"
        elif count > 4:
            response = irritated_responses[(count - 1) % len(irritated_responses)]
    else:
        # If it's a new query, store it in the dictionary
        query_counts[user_input.strip().lower()] = 1
        
        # Generate a neutral response for new queries
        response = "Hello!"

    # Write updated query counts back to the file
    with open("query_counts.txt", "w") as file:
        file.write(str(query_counts))

    return response

# Delete the query_counts.txt file if it exists
if os.path.exists("query_counts.txt"):
    os.remove("query_counts.txt")

# Main loop to interact with the user
while True:
    # Take user input
    user_input = input("You: ")
    
    # Generate response
    response = generate_response(user_input)
    
    # Print response
    print("System:", response)
