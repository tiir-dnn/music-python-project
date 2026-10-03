import pandas as pd

# read the CSV file into a table (a "DataFrame")
df = pd.read_csv("data/dataset.csv")

print("Rows and columns:", df.shape)
print()
print("Column names:")
print(list(df.columns))
print()
print("First 5 rows:")
print(df.head())