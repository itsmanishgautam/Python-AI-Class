import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Initialize NLTK's stopwords
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Responses to different types of greetings
GREETING_RESPONSES = ["Hello!", "Hi!", "Hey there!", "Greetings!"]

# Responses to different types of farewells
FAREWELL_RESPONSES = ["Goodbye!", "See you later!", "Take care!"]

# Function to preprocess user input
def preprocess_input(input_text):
    # Tokenize input text
    tokens = word_tokenize(input_text.lower())
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Function to respond to user input
def respond_to_input(user_input):
    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return random.choice(GREETING_RESPONSES)
    elif any(farewell in user_input for farewell in ["goodbye", "bye", "see you"]):
        return random.choice(FAREWELL_RESPONSES)
    else:
        return "I'm sorry, I didn't understand that."

# Main function
def chat():
    print("AI: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("AI: Goodbye!")
            break
        response = respond_to_input(user_input)
        print("AI:", response)

# Start the conversation
chat()
