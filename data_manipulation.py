import pandas as pd

# Creating a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer', 'Teacher']
}
df = pd.DataFrame(data)

# Manipulating the data: Add a new column with salary estimates
df['Salary'] = [70000, 80000, 45000, 90000, 50000]

# Save the DataFrame to a JSON file
df.to_json('data.json', orient='records', lines=True)

print("Data manipulation complete. JSON file saved as data.json.")
