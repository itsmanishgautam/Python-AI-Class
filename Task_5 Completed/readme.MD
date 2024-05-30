# Relation Sorting and Matching with Natural Language Processing

This Python script performs two main tasks: sorting relation data into a sorted linked list based on user input and matching user input with relation data using natural language processing (NLP).

## Sorting Relation Data

The script allows users to input relations and ages, categorizes the relations into "senior" or "junior" based on the user's age, and sorts the data into a sorted linked list based on age.

### Classes:

1. **Node**: Represents a node in a linked list.
2. **SortedLinkedList**: Implements a sorted linked list.
  
### Functions:

1. **add_more_relations()**: Prompts the user to add more relations.
2. **sort_into_linked_list(df)**: Sorts the relation data from a DataFrame into a sorted linked list.
3. **display_linked_list(linked_list)**: Displays the contents of the sorted linked list.
4. **export_to_csv(linked_list, filename)**: Exports the sorted data from the linked list to a CSV file.
5. **main()**: Main function to execute the sorting process.

## Matching User Input with Relation Data

The script reads the sorted relation data from a CSV file, preprocesses the user input and relation data using spaCy, and matches the user input with the closest matching relation.

### Dependencies:

- `pandas`: For reading and manipulating CSV data.
- `spacy`: For natural language processing.

### Functions:

1. **match_user_input(user_input, df)**: Matches the user input with relation data from a DataFrame.
2. **main()**: Main function to execute the matching process.

### Usage:

1. Run the script.
2. For sorting relation data:
   - Enter the user age.
   - Enter relations and ages, categorize as "senior" or "junior".
   - Choose to add more relations or exit.
3. For matching user input:
   - Enter user input.
   - The bot responds based on the matched relation.

## Files:

- **relation.csv**: CSV file containing relation data.
- **sorted_relations.csv**: CSV file containing sorted relation data.

