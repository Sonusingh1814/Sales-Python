import pandas as pd


# Read data from a text file
df = pd.read_csv('sales-december-2019.txt', delimiter=',')  # Ensure delimiter matches your data format

# Save to CSV file
df.to_csv('sales-december-2019.csv', index=False)

print("sales-december-2019.csv")
