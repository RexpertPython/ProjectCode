#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:03:57 2023

@author: anas
"""
import pandas as pd
import csv

# Define the file path
file_path = "/Users/anas/Documents/UoR/MSc Project/Report/Logs/20230301_anon.log"

# Read the file and extract the key-value pairs
#data = {'Key': [], 'Value': []}

data = []
log_data = {}

# Split the data into individual records
records = [record.strip().split('\n') for record in data.strip().split('startdate') if record.strip()]

# Get all unique keys from the records
keys = set()
for record in records:
    for key_value in record:
        key = key_value.split()[0]
        keys.add(key)

# Create a CSV file and write the data
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keys)
    writer.writeheader()
    for record in records:
        row = {}
        for key_value in record:
            key, value = key_value.split()
            row[key] = value
        writer.writerow(row)

print("CSV file created successfully.")

# with open(file_path, 'r') as file:
#     count = 0
#     for line in file:
#         line = line.strip()
#         key_value_pairs = re.findall(r'\$([\w-]+)=\'([\w\-:]+)\'', line)
#         count += 1
#         for key, value in key_value_pairs:
#             data['Key'].append(key)
#             data['Value'].append(value)
#         count += 1
#         if count == 10:
#             break
                
        

# Create a data frame from the extracted data
df = pd.DataFrame(data_list)
print(df.head())
# df.to_csv("/Users/anas/Documents/UoR/MSc Project/Report/Logs/Test.csv", index = False)
