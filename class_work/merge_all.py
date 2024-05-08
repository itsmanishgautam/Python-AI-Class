import pandas as pd

# def merge_csv_complex(out1, out2, out3, mergedcsv, output_file1, output_file2, output_file3):
#     merged_df1 = pd.merge(out1, mergedcsv, on=['Country'])
#     merged_df1.to_csv(output_file1, index=False)

#     merged_df2 = pd.merge(out2, mergedcsv, on=['Country'])
#     merged_df2.to_csv(output_file2, index=False)

#     merged_df3 = pd.merge(out3, mergedcsv, on=['Country'])
#     merged_df3.to_csv(output_file3, index=False)

if __name__ == "__main__":
    out1 = pd.read_csv("csv/output1.csv")
    out2 = pd.read_csv("csv/output2.csv")
    out3 = pd.read_csv("csv/output3.csv")
    mergedcsv = pd.read_csv("csv/CountryAdd_onCurrency_output.csv")

    output_file1 = 'csv/finaldata1.csv'
    output_file2 = 'csv/finaldata2.csv'
    output_file3 = 'csv/finaldata3.csv'

    # merge_csv_complex(out1, out2, out3, mergedcsv, output_file1, output_file2, output_file3)
