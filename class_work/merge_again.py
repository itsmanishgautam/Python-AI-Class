import pandas as pd

def merge_csv_complex(df3, df4, output_file):
    merged_df = pd.merge(df3, df4, on=['Country'])
    merged_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    df3 = pd.read_csv("csv/CountryAdd_onCurrency_output.csv")
    df4 = pd.read_csv("csv/output1.csv")
    output_file = "csv/final.csv"
    merge_csv_complex(df3, df4, output_file)
