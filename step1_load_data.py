import pandas as pd

df = pd.read_csv("data/electricity_data.csv")

print("Electricity Data:")
print(df.head(3001))

df.to_csv("data/cleaned_electricity.csv", index=False)
print("✅ Cleaned data saved successfully!")
