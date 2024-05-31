import pandas as pd

def merge_csv_complex(out1, out2, out3, mergedcsv1, output_file1, output_file2, output_file3):

    # Convert "Country" column to lowercase for case-insensitive matching
    mergedcsv1['Country'] = mergedcsv1['Country'].str.lower()
    out1['Country'] = out1['Country'].str.lower()
    out2['Country'] = out2['Country'].str.lower()
    out3['Country'] = out3['Country'].str.lower()

    # Perform the merge
    merged_df1 = pd.merge(out1, mergedcsv1, on=['Country'])
    merged_df2 = pd.merge(out2, mergedcsv1, on=['Country'])
    merged_df3 = pd.merge(out3, mergedcsv1, on=['Country'])
    
    # Write the merged DataFrames to CSV files
    merged_df1.to_csv(output_file1, index=False)
    merged_df2.to_csv(output_file2, index=False)
    merged_df3.to_csv(output_file3, index=False)

if __name__ == "__main__":
    mergedcsv = pd.read_csv("Task_2/csv/CountryAdd_onCurrency_output.csv")
    # Reorder columns
    df = mergedcsv[['Country', 'Currency_Code', 'Currency_x', 'Currency_y', 'Units', 'Buy', 'Sell']]
    # Write back to CSV
    df.to_csv('Task_2/csv/CountryRearrange.csv', index=False)

    mergedcsv1 = pd.read_csv('Task_2/csv/CountryRearrange.csv')
    out1 = pd.read_csv("Task_2/csv/splitoutput1.csv")
    out2 = pd.read_csv("Task_2/csv/splitoutput2.csv")
    out3 = pd.read_csv("Task_2/csv/splitoutput3.csv")

    output_file1 = 'Task_2/csv/finaldata1.csv'
    output_file2 = 'Task_2/csv/finaldata2.csv'
    output_file3 = 'Task_2/csv/finaldata3.csv'

    merge_csv_complex(out1, out2, out3, mergedcsv1, output_file1, output_file2, output_file3)






























# import pandas as pd

# def merge_csv_complex(out1, out2, out3, mergedcsv1, output_file1, output_file2, output_file3):

#     # Convert "Country" column to lowercase for case-insensitive matching
#     out2['Country'] = out2['Country'].str.lower()
#     mergedcsv1['Country'] = mergedcsv1['Country'].str.lower()

#     # Perform the merge
#     merged_df2 = pd.merge(out2, mergedcsv1, on=['Country'])
    
#     # Write the merged DataFrame to a CSV file
#     merged_df2.to_csv(output_file2, index=False)

# if __name__ == "__main__":
#     mergedcsv = pd.read_csv("Task_2/csv/CountryAdd_onCurrency_output.csv")
#     # Reorder columns
#     df = mergedcsv[['Country', 'Currency_Code', 'Currency_x', 'Currency_y', 'Units', 'Buy', 'Sell']]
#     # Write back to CSV
#     df.to_csv('Task_2/csv/CountryRearrange.csv', index=False)

#     mergedcsv1 = pd.read_csv('Task_2/csv/CountryRearrange.csv')
#     out1 = pd.read_csv("Task_2/csv/splitoutput1.csv")
#     out2 = pd.read_csv("Task_2/csv/splitoutput2.csv")
#     out3 = pd.read_csv("Task_2/csv/splitoutput3.csv")

#     output_file1 = 'Task_2/csv/finaldata1.csv'
#     output_file2 = 'Task_2/csv/finaldata2.csv'
#     output_file3 = 'Task_2/csv/finaldata3.csv'

#     merge_csv_complex(out1, out2, out3, mergedcsv1, output_file1, output_file2, output_file3)
