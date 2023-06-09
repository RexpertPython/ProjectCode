import pandas as pd
import csv

file_input = "/Users/anas/Documents/UoR/MSc Project/Report/Logs/logtxt.csv"
'''
with open(file_input, 'r') as file:
    reader = csv.reader(file)

# Create an empty list to store the rows
rows = []

# Open the file in read mode
with open(file_input, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Read the header
    header = next(reader)

# Print header labels

    print(header)

    # Iterate over each row in the file
    for row in reader:
        # Process each row as needed
        # Here, we're just appending the row to the list for demonstration purposes
        rows.append(row)

# Create a DataFrame from the list of rows
df = pd.DataFrame(rows)

# Now you can work with the complete DataFrame
# For example, you can print the first few rows
print(df.head())
'''
chunk_size = 10000

# Store header names
header = []

with open(file_input, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    while True:
        # Read the next chunk of rows
        rows = []
        rows_read = False  # Flag to check if any rows were read
        
        for _ in range(chunk_size):
            try:
                row = next(reader)
                if len(row) == len(header):
                    rows.append(row)
                    rows_read = True
            except csv.Error as e:
                print(f"Error reading row: {e}")
                continue
        
        # Break the loop if no rows were read
        if not rows_read:
            break

        df_chunk = pd.DataFrame(rows, columns = header)
# Concatenate all the chunks into a single DataFrame
df = pd.concat(chunks)

print(df_chunk.head())
print(df.shape())


