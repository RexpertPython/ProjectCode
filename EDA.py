import pandas as pd
import csv
import time
import warnings

warnings.filterwarnings("ignore")

def read_into_df(filename):
    return pd.read_csv(filename)

def check_duplicates(df):
    duplicated_df = df.duplicated()
    print(f'Number of duplicated rows: {duplicated_df.sum()}')

def check_null_values(df):
    missing_values = df.isnull().sum()
    total_rows = len(df)
    percentage_null_values = (missing_values/total_rows)*100
    result = []
    for column, count in missing_values.items():
        percentage = percentage_null_values[column]
        print(f'{column}: {count}. % Null values: {percentage:.2f}%')
        result.append({'Column': column, 'Null Count': count, '% Null Values': percentage})

    result_df = pd.DataFrame(result)
    result_df.to_csv('/Users/anas/Documents/UoR/MSc Project/Report/Logs/Column Null Values.csv', index=False)

def check_unique_values(df):
    # unique_values = {}
    # for column in df.columns:
    #     unique_values[column] = df[column].unique()
    #     print(f"Unique values: {df[column].unique()}")
    #     print()
    # unique_values = []
    # for column in df.columns:
    #     unique_values = df[column].unique()
    #     print(f"Column: {column}")
    #     print(f"Unique values: {unique_values}")
    #     print()
    result = []
    for column in df.columns:
        unique_values_count = df[column].nunique()
        print(f"Column: {column}")
        print(f"Number of unique values: {unique_values_count}")
        print()
        result.append({'Column': column, 'Unique Values': unique_values_count})

    result_df = pd.DataFrame(result)
    result_df.to_csv('/Users/anas/Documents/UoR/MSc Project/Report/Logs/Column Unique Values.csv', index=False)


filename = "/Users/anas/Documents/UoR/MSc Project/Report/Logs/ConvertToLog.csv"
with open(filename, 'r') as file:
    start = time.time()
    chunk = pd.read_csv(filename,chunksize=1000000)
    end = time.time()
    print("Read csv with chunks: ",(end-start),"sec")
    start = time.time()
    pd_df = pd.concat(chunk)
    end = time.time()
    print("Concatenation time: ",(end-start),"sec")
    
#     print("Info")
#     print(pd_df.info(memory_usage = "deep"))
#     print("Shape")
#     print(pd_df.shape)
#     print("Description")
#     print(pd_df.describe)
#     print()

# #    check_duplicates(pd_df)
#     start = time.time()
    check_null_values(pd_df)
#     end = time.time()
#     print(f'Null value time check:  {end - start}, sec')

    check_unique_values(pd_df)
