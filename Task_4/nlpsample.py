import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import Levenshtein

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define stopwords
stop_words = set(stopwords.words('english'))

# Define a function to calculate similarity using Levenshtein distance
def calculate_similarity(input_str, query):
    input_str = ' '.join(input_str)  # Convert list to string
    return Levenshtein.distance(input_str.lower(), query.lower())

# Define a function to process user input and generate responses
def generate_response(user_input):
    # Tokenize user input
    user_tokens = word_tokenize(user_input.lower())
    user_tokens = [token for token in user_tokens if token.isalnum() and token not in stop_words]

    # Check if the file exists
    if os.path.exists("query_counts.txt"):
        # Read query counts from the file
        with open("query_counts.txt", "r") as file:
            query_counts = eval(file.read())
    else:
        query_counts = {}

    # Check if the user input is a repeated query
    similar_queries = [query for query in query_counts.keys() if calculate_similarity(user_tokens, query.split()) <= 2]
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
            response = "I'm starting to get annoyed by your repeated questions."
    else:
        # If it's a new query, store it in the dictionary
        query_counts[' '.join(user_tokens)] = 1
        
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
