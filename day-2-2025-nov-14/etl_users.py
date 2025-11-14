import requests
import pandas as pd
import sqlite3

# 1. Extract
url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()

results = data["results"]

# 2. Transform (flatten)
users = []

for item in results:
    users.append({
        "first_name": item["name"]["first"],
        "last_name": item["name"]["last"],
        "gender": item["gender"],
        "email": item["email"],
        "city": item["location"]["city"],
        "country": item["location"]["country"]
    })

df = pd.DataFrame(users)

# 3. Load
conn = sqlite3.connect("users.db")
df.to_sql("random_users", conn, if_exists="replace", index=False)

# 4. Summary
print("---- ETL SUMMARY ----")
print(f"Users fetched: {len(df)}")
print("\nCount by gender:")
print(df["gender"].value_counts())

print("\nTop 3 countries:")
print(df["country"].value_counts().head(3))

conn.close()
