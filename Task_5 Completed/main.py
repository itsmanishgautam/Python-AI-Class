import pandas as pd
import spacy

df = pd.read_csv("Task_5 Completed/sorted_relations.csv")
nlp = spacy.load("en_core_web_sm")

def match_user_input(user_input, df):
    doc_user_input = nlp(user_input)
    
    for index, row in df.iterrows():
        doc_relation = nlp(row['Relation'])
        
        for token_user_input in doc_user_input:
            if any(token_user_input.text == token_relation.text for token_relation in doc_relation):
                return row
    
    return None

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    matched_row = match_user_input(user_input, df)
    
    if matched_row is not None:
        if matched_row['Relation'] == matched_row.iloc[0] and matched_row.iloc[1] == 'senior':
            reply = f"Namaste {matched_row['Relation']}, I am a bot."
        elif matched_row['Relation'] == matched_row.iloc[0] and matched_row.iloc[1] == 'junior':
            reply = f"Hello {matched_row['Relation']}, I am a bot."
    else:
        reply = "Sorry, You are not in my database."

    print("Bot:", reply)


