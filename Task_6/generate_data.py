import csv
import random
from faker import Faker

# Create a Faker object
fake = Faker()

# Number of tech companies
num_companies = 300

# Number of employees
num_employees = 50000

# List to store tech companies data
tech_companies = []

# List to store employee data
employees = []

for _ in range(num_companies):
    company_name = fake.company()
    num_vacancies = random.randint(1, 10)  # Number of vacancies per company
    job_titles = []
    skills = []
    for _ in range(num_vacancies):
        job_title = fake.job()
        required_skills = [fake.word() for _ in range(random.randint(1, 5))]
        job_titles.append(job_title)
        skills.append(required_skills)
    work_hours = fake.time(pattern='%H:%M') + ' - ' + fake.time(pattern='%H:%M')
    tech_companies.append({'company_name': company_name, 'job_titles': job_titles, 'skills': skills, 'work_hours': work_hours})


# Generate fake data for employees
for _ in range(num_employees):
    first_name = fake.first_name()
    last_name = fake.last_name()
    skills = [fake.word() for _ in range(random.randint(1, 5))]  # Random skills
    availability = fake.time(pattern='%H:%M') + ' - ' + fake.time(pattern='%H:%M')  # Random availability
    preferred_work_hours = fake.time(pattern='%H:%M') + ' - ' + fake.time(pattern='%H:%M')  # Random preferred work hours
    preferred_days = [fake.day_of_week() for _ in range(random.randint(1, 7))]  # Random preferred days
    employees.append({'first_name': first_name, 'last_name': last_name, 'skills': skills,
                      'availability': availability, 'preferred_work_hours': preferred_work_hours,
                      'preferred_days': preferred_days})

# Export tech companies data to CSV
with open('tech_companies.csv', 'w', newline='') as csvfile:
    fieldnames = ['company_name', 'work_hours', 'job_titles', 'skills']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for company in tech_companies:
        writer.writerow(company)

# Export employee data to CSV
with open('employees.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'skills', 'availability', 'preferred_work_hours', 'preferred_days']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for employee in employees:
        writer.writerow(employee)

print("CSV files generated successfully!")
