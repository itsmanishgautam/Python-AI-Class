# Chatbot with User Input Matching and Irritated Responses

This Python script implements a chatbot that matches user input with predefined patterns and responses, and includes functionality for handling irritated responses.

## Functionality:

- **Matching User Input**: The chatbot matches user input with predefined patterns using string similarity calculations.
- **Irritated Responses**: If the user input is similar to previous queries, the chatbot responds with an irritated message.

### Dependencies:

- `os`: For interacting with the operating system.
- `json`: For reading and writing JSON files.
- `Levenshtein`: For calculating string similarity.
- `random`: For selecting random responses.

### Functions:

1. **calculate_similarity(input_str, query)**: Calculates the similarity between two strings using the Levenshtein distance.
2. **generate_response(user_input, query_counts)**: Generates a response based on user input, checking for similarity with previous queries and predefined patterns.
3. **main()**: Main function to execute the chatbot loop.

### Files:

- **data.json**: JSON file containing predefined intents and responses.
- **query_counts.json**: JSON file containing counts of user queries.

### Usage:

1. Run the script.
2. Enter user input.
3. The chatbot responds based on matched patterns and previous queries.
4. If the user input is similar to previous queries, the chatbot may respond with an irritated message.

## Predefined Intents:

The script includes predefined intents for greeting, goodbye, creator information, chatbot name, college hours, contact information, and more.

## Notes:

- Adjust the similarity threshold as needed for matching user input.
- Customize the predefined intents and responses in the `data.json` file.

## Programmer
Manish Gautam

## Mentor, Brain
Dixanta Bahadur Shrestha