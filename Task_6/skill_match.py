import pandas as pd

# Assuming the tech_companies.csv and employees.csv files are already created and populated

tech_companies_df = pd.read_csv('sample_tech_company.csv')
tech_companies_df['vacancies'] = tech_companies_df['vacancies'].apply(eval)  # Convert string representation of list to actual list
employees_df = pd.read_csv('sample_employee.csv')

def match_skills(employees_df, tech_companies_df):
    matches = []
    for _, company in tech_companies_df.iterrows():
        for vacancy in company['vacancies']:
            required_skills = set(vacancy['required_skills'])
            for _, employee in employees_df.iterrows():
                employee_skills = set(employee['skills'])
                if required_skills.issubset(employee_skills):
                    matches.append({'company_name': company['company_name'], 'job_title': vacancy['job_title'],
                                    'employee_name': employee['first_name'] + ' ' + employee['last_name']})
                    break  # Break loop after finding a match for the vacancy
    return matches

matched_jobs = match_skills(employees_df, tech_companies_df)

# Convert the list of dictionaries to DataFrame
matches_df = pd.DataFrame(matched_jobs)

# Print the first 2 matches
print(matches_df.head(2))
