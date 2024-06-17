import pandas as pd

def working_code(bank_interest_url, nepal_data_url, gold_url, nepse_url):
    # Load data from CSV files
    df_bank_interest = pd.read_csv(bank_interest_url)
    df_nepal_data = pd.read_csv(nepal_data_url)
    df_gold = pd.read_csv(gold_url)
    df_nepse = pd.read_csv(nepse_url)

    print("Enter the amount you have")
    x = int(input())
    print("What do you want to buy?")
    print("Number Required")
    print("1 = Gold/Silver")
    print("2 = Shares")
    print("3 = Bank Interest")
    y = int(input())

    if y == 1:
        # Handle buying Gold/Silver
        # Example: Print the first few rows of the Gold/Silver DataFrame
        print("Gold/Silver Data:")
        print(df_gold.head())

        # Add your code for buying Gold/Silver here

    elif y == 2:
        # Handle buying Shares
        # Example: Print the first few rows of the NEPSE DataFrame
        print("NEPSE Data:")
        print(df_nepse.head())

        # Add your code for buying Shares here

    elif y == 3:
        # Handle Bank Interest
        # Example: Print the first few rows of the Bank Interest DataFrame
        print("Bank Interest Data:")
        print(df_bank_interest.head())

        # Add your code for Bank Interest here

    else:
        print("Invalid choice")

if __name__ == '__main__':
    bank_interest_url = 'https://github.com/itsmanishgautam/Python-AI-Class/blob/main/Task_3/csv/bank_interest.csv'
    nepal_data_url = 'https://github.com/itsmanishgautam/Python-AI-Class/blob/main/Task_3/csv/nepal_data.csv'
    gold_url = 'https://github.com/itsmanishgautam/Python-AI-Class/blob/main/Task_3/csv/Gold_Silver_Cost.csv'
    nepse_url = 'https://github.com/itsmanishgautam/Python-AI-Class/blob/main/Task_3/csv/nepse_data.csv'
    working_code(bank_interest_url, nepal_data_url, gold_url, nepse_url)
