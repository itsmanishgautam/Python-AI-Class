import csv
import pandas as pd

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        elif self.head.data[2] > data[2]: 
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data[2] < data[2]: 
                current = current.next
            new_node.next = current.next
            current.next = new_node

def add_more_relations():
    return input("Would you like to add more relations? (yes/no): ").lower() == "yes"

def sort_into_linked_list(df):
    linked_list = SortedLinkedList()
    if df is not None:
        for index, row in df.iterrows():
            relation = row["Relation"].lower()
            category = row["Category"].lower()
            age = row["Age"]
            linked_list.insert((relation, category, age))
    return linked_list

def display_linked_list(linked_list):
    current = linked_list.head
    while current:
        print("Relation:", current.data[0])
        print("Category:", current.data[1])
        print("Age:", current.data[2])
        print("-------------------")
        current = current.next

def export_to_csv(linked_list, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Relation", "Category", "Age"])
        current = linked_list.head
        while current:
            writer.writerow(current.data)
            current = current.next
    print("Data exported to", filename)

def main():
    try:
        existing_filename = "Task_5/relation.csv"
        try:
            existing_df = pd.read_csv(existing_filename)
        except FileNotFoundError:
            existing_df = pd.DataFrame(columns=["Relation", "Category", "Age"])

        new_data = []
        while add_more_relations():
            relation = input("Enter the relation: ").lower()
            category = input("Enter the category (Senior/Junior): ").lower()
            age = int(input("Enter the age: "))
            new_data.append({"Relation": relation, "Category": category, "Age": age})

        new_df = pd.DataFrame(new_data)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)

        linked_list = sort_into_linked_list(combined_df)
        print("Data sorted into a sorted linked list:")
        display_linked_list(linked_list)

        sorted_filename = "Task_5/sorted_relations.csv"
        export_to_csv(linked_list, sorted_filename)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
