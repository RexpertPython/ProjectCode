import pandas as pd
import csv
import concurrent.futures

file_input = "/Users/anas/Documents/UoR/MSc Project/Report/Logs/logtxt.csv"

def process_row(row):
    return pd.DataFrame([row])


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
    dfs = []
     # Create a thread pool executor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Iterate over each row in the file
        for row in reader:
            # Submit the row to the executor for processing
            future = executor.submit(process_row, row)
            # Append the future object to the list
            dfs.append(future)

    # Wait for all futures to complete
    concurrent.futures.wait(dfs)

    # Extract the data frames from the completed futures
    dfs = [future.result() for future in dfs]

# Concatenate all data frames into a single data frame
df = pd.concat(dfs, ignore_index=True)
# Now you can work with the complete DataFrame
# For example, you can print the first few rows
print(df.head())

'''
chunk_size = 10000

# Store header names
header = []
rows = []
rows_read = False


def read_into(file_input):
    with open(file_input, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        while True:
            # Read the next chunk of rows
            # Flag to check if any rows were read
            
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
        df = pd.concat(df_chunk)
        return df


file_input = "/Users/anas/Documents/UoR/MSc Project/Report/Logs/logtxt.csv"
df = read_into(file_input)

print(df.shape())

'''