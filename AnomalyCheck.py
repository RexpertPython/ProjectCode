import pandas as pd
import csv
import matplotlib.pyplot as plt

def count_csv_columns(filename):
    column_counts = {}

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read the header row

        for row in csv_reader:
            num_columns = len(row)
            if num_columns in column_counts:
                column_counts[num_columns] += 1
            else:
                column_counts[num_columns] = 1

    return column_counts

def plot_csv_columns(filename):

    column_counts = count_csv_columns(filename)
    x = list(column_counts.keys())
    y = list(column_counts.values())

    plt.bar(x, y)
    plt.xlabel('Number of Features')
    plt.ylabel('Number of Logs')
    plt.title('Feature Count Bar Graph')
    plt.show()

def header_length(filename):
    with open(filename,'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        print(f"Number of features are: {len(header)}")

# Provide file path
file_input = "/Users/anas/Documents/UoR/MSc Project/Report/Logs/logtxt.csv"

# Print header length
header_length(file_input)

# Make a bar chart of number of features vs. number of records
plot_csv_columns(file_input)
