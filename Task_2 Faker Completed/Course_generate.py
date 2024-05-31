import random
import csv

def generate_fake_courses(num_records):
    courses = ['Java', 'Python', 'PHP', 'C#']  # List of available courses

    with open('Task_2/csv/Courses.csv', 'w', newline='') as csvfile:
        fieldnames = ['Course']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_records):
            writer.writerow({'Course': random.choice(courses)})  # Choose a random course from the list

if __name__ == "__main__":
    num_records = 100000
    generate_fake_courses(num_records)
