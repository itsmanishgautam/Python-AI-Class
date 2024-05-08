import pandas as pd

def merge_csv_complex(df3, df4, output_file):
    merged_df = pd.merge(df4, df3, on=['Currency_Code'])
    merged_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    df3 = pd.read_csv("Task_2/csv/forex.csv")
    df4 = pd.read_csv("Task_2/csv/Country_and_CurrencyCode.csv")
    output_file = 'Task_2/csv/CountryAdd_onCurrency_output.csv'
    merge_csv_complex(df3, df4, output_file)
