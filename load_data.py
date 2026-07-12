import pandas as pd
import sqlite3

df = pd.read_excel("student.csv.xlsx")

conn = sqlite3.connect("campus.db")

df.to_sql(
    "students",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data Loaded Successfully")