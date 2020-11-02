import pandas as pd

df = pd.read_excel("input/caa_courses.xlsx", index_col = "id")
print(len(df))
print(df.columns)
print(df.index)