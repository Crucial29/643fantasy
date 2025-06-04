import pandas as pd

url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=sta&type=1&season=2024&team=all&lg=all&qual=100&ind=0&csv=1'

# Load data directly into a DataFrame
df = pd.read_csv(url)

# Preview
print(df.head())

# Save to CSV
df.to_csv("fangraphs_pitchers_2025.csv", index=False)

# Load data directly into a DataFrame
df = pd.read_csv(url)

# Preview
print(df.head())

# Save to CSV
df.to_csv("fangraphs_pitchers_2025.csv", index=False)
