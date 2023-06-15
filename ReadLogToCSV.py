import csv

input_file = "/Users/anas/Documents/UoR/MSc Project/Report/Logs/20230301_anon.log"
output_file = "/Users/anas/Documents/UoR/MSc Project/Report/Logs/ConvertToLog.csv"
# Create a list to store all keys in order
# Create a list to store all keys in order
keys = []

# Read the log file and extract keys and values
with open(input_file, 'r') as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()

        if line:
            # Split the line into key-value pairs
            pairs = line.split(';')

            # Process each key-value pair
            for pair in pairs:
                # Check if the pair has an equal sign
                if '=' in pair:
                    # Split the pair into key and value
                    key, value = pair.split('=', 1)

                    # Add the key to the list of keys
                    if key not in keys:
                        keys.append(key)

# Write the keys and values to the CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row with the keys
    writer.writerow(keys)

    # Write the values row by row
    for line in lines:
        line = line.strip()

        if line:
            # Split the line into key-value pairs
            pairs = line.split(';')

            # Create a dictionary to store the values
            values = {}

            # Process each key-value pair
            for pair in pairs:
                # Check if the pair has an equal sign
                if '=' in pair:
                    # Split the pair into key and value
                    key, value = pair.split('=', 1)

                    # Store the value in the dictionary
                    values[key] = value

            # Write the values to the CSV file in the order of the keys
            writer.writerow([values.get(key, '') for key in keys])

print("CSV file generated successfully.")