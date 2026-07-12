# import streamlit as st
# import pandas as pd

# df = pd.read_excel("student.csv.xlsx")

# st.title("Smart Campus Analytics Dashboard")

# st.write(df)

# st.metric(
#     "Total Students",
#     len(df)
# )

# st.metric(
#     "Average Attendance",
#     round(df["Attendence"].mean(),2)
# )

# st.metric(
#     "Average Marks",
#     round(df["Marks"].mean(),2)
# )

# risk_students = df[
#     (df["Attendence"] < 75)
# ]

# st.subheader("At Risk Students")

# st.dataframe(risk_students)

















import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("campus.db")


df = pd.read_sql_query(
    "SELECT * FROM students",
    conn
)

st.title("Smart Campus Analytics")

st.dataframe(df)

st.metric("Total Students", len(df))

st.metric(
    "Average Attendence",
    round(df["Attendence"].mean(),2)
)

st.metric(
    "Average Marks",
    round(df["Marks"].mean(),2)
)


risk_students = df[
    (df["Attendence"] < 75)
]

st.subheader("At Risk Students")

st.dataframe(risk_students)
