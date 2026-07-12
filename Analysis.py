import pandas as pd

df = pd.read_excel("student.csv.xlsx")

print(df)

print("\nTotal Students:", len(df))

print("\nAverage Attendence:")
print(df["Attendence"].mean())

print("\nAverage Marks:")
print(df["Marks"].mean())


import matplotlib.pyplot as plt

department_marks = df.groupby("Department")["Marks"].mean()

department_marks.plot(kind="line")

plt.title("Department Wise Marks")

plt.show()