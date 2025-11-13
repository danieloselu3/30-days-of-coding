import pandas as pd
import sqlite3



# extract data from CSV
df = pd.read_csv('orders_raw.csv')
raw_count = len(df)

# transform
df["customer"] = df["customer"].str.title()

# handle missing values
avg_amount = df["amount"].mean(skipna=True)
df["amount"] = df["amount"].fillna(avg_amount)

# Filter completed orders
df_clean = df[df["status"] == "completed"]
clean_count = len(df_clean)

# load to sqlite database
conn = sqlite3.connect('orders.db')
df_clean.to_sql("clean_orders", conn, if_exists="replace", index=False)

# 4. Summary
total_revenue = df_clean["amount"].sum()
top_customer = (
    df_clean.groupby("customer")["amount"].sum().sort_values(ascending=False).head(1)
)

print("----- ETL SUMMARY -----")
print(f"Raw rows: {raw_count}")
print(f"Clean rows: {clean_count}")
print(f"Total revenue: {total_revenue}")
print("Top customer:")
print(top_customer)

conn.close()

