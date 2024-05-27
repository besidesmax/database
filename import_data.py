import pandas as pd
from engine import engine
from classes import Address, Student

# read csv-Data
df_address = pd.read_csv("addresses_2050.csv", encoding="utf-8")
df_student = pd.read_csv("students_2000.csv", encoding="utf-8")

# add student_2000.csv to database TODO: add exception, when exist = do nothing
# df_address.to_sql(con=engine, name=Address.__tablename__, if_exists="append", index=False)

# add student_2000.csv to database
# df_student.to_sql(con=engine, name=Student.__tablename__, if_exists="append", index=False)

# add student_2000.csv to database
# df_student.to_sql(con=engine, name=Student.__tablename__, if_exists="append", index=False)
