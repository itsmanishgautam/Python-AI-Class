# import re
# import json
# import os

# # Define the file path for the brain.json file
# BRAIN_FILE_PATH = "Task_11 NLP ML/brain.json"

# # Load the bot's brain from the JSON file
# def load_brain():
#     if os.path.exists(BRAIN_FILE_PATH):
#         with open(BRAIN_FILE_PATH, "r") as file:
#             return json.load(file)
#     else:
#         print("AI: Brain data not found. Please provide initial brain data in 'brain.json'.")
#         return {}

# def save_brain(brain):
#     with open(BRAIN_FILE_PATH, "w") as file:
#         json.dump(brain, file, indent=4)
#         print("AI: Brain has been updated and saved.")

# # Extract numbers and operation based on known terms in the brain
# def extract_numbers_and_operation(statement, brain):
#     numbers = list(map(float, re.findall(r'\b\d+(?:\.\d+)?\b', statement)))
#     operation = None

#     for term, operation_name in brain.items():
#         if term in statement:
#             operation = operation_name
#             break

#     return numbers, operation

# def perform_calculation(numbers, operation):
#     if operation == "addition":
#         result = sum(numbers)
#     elif operation == "subtraction":
#         result = numbers[0] - sum(numbers[1:])
#     elif operation == "multiplication":
#         result = 1
#         for num in numbers:
#             result *= num
#     elif operation == "division":
#         result = numbers[0]
#         try:
#             for num in numbers[1:]:
#                 result /= num
#         except ZeroDivisionError:
#             result = "Error: Division by zero."
#     else:
#         result = None

#     return result

# def ai_bot():
#     brain = load_brain()
#     print("Loaded brain:", brain)
#     if not brain:
#         return

#     print("Hello! I can help you with basic arithmetic calculations.")
#     while True:
#         user_input = input("You: ").strip().lower()

#         if user_input in ['exit', 'quit']:
#             print("AI: Goodbye!")
#             break

#         numbers, operation = extract_numbers_and_operation(user_input, brain)

#         if not numbers:
#             print("AI: I didn't find any numbers in your statement. Please provide numbers for the calculation.")
#             continue

#         if not operation:
#             print("AI: I am confused, tell me which calculation you would like to perform (e.g., addition, subtraction, multiplication, division).")
#             clarification = input("You: ").strip().lower()

#             if clarification:
#                 print(f"AI: Could you explain what '{clarification}' means (e.g., addition, subtraction, multiplication, division)?")
#                 definition = input("You: ").strip().lower()
                
#                 brain[clarification] = definition
#                 save_brain(brain)
#                 print(f"AI: I have learned that '{clarification}' means '{definition}'. I will remember this for future calculations.")
#                 # Re-extract numbers and operation after learning new term
#                 numbers, operation = extract_numbers_and_operation(user_input, brain)

#         result = perform_calculation(numbers, operation)

#         if result is not None:
#             print(f"AI: The result of the {operation} is: {result}")
#         else:
#             print("AI: I am still confused. Could you please clarify your request?")

# # Run the AI bot
# ai_bot()
