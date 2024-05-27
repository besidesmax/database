import pandas as pd
from engine import engine
from classes import Student, Address
# read csv-Data
df_address = pd.read_csv("addresses_2050.csv", encoding="utf-8")

# add student_2000.csv to database TODO: add exception, when exist = do nothing
df_address.to_sql(con=engine, name=Address.__tablename__, if_exists="append", index=False)


