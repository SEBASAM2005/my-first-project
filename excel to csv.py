import pandas as pd
excel_file = "example.xlsx"

df = pd.read_excel(excel_file)
csv_file = "output.csv"

df.to_csv(csv_file, index=False)

print(f"has been converted  {excel_file} to {csv_file} seccessfully!")
