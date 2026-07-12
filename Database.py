import sqlite3

conn = sqlite3.connect("campus.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    Student_ID INTEGER,
    Name TEXT,
    Department TEXT,
    Attendence INTEGER,
    Marks INTEGER
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")