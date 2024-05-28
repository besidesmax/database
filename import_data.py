import pandas as pd
from random import choices
from engine import engine
from classes import Address, Student, Course, Program, Grade


# read csv-Data
df_address = pd.read_csv("addresses_2050.csv", encoding="utf-8")
df_student = pd.read_csv("students_2000.csv", encoding="utf-8")
df_study_program = pd.read_csv("study_program_13.csv", encoding="utf-8")
df_course = pd.read_csv("courses_150.csv", encoding="utf-8")
df_grades = pd.read_csv("grades_23000.csv", encoding="utf-8")


# add student_2000.csv to database TODO: add exception, when exist = do nothing
df_address.to_sql(con=engine, name=Address.__tablename__, if_exists="append", index=False)

# add student_2000.csv to database
df_student.to_sql(con=engine, name=Student.__tablename__, if_exists="append", index=False)

# add study_programm_13.csv to database
df_study_program.to_sql(con=engine, name=Program.__tablename__, if_exists="append", index=False)

# add courses_250.csv to database
df_course.to_sql(con=engine, name=Course.__tablename__, if_exists="append", index=False)

# add grades_2300 to database
df_grades.to_sql(con=engine, name=Grade.__tablename__, if_exists="append", index=False)

'''
a = [1, 2, 3, 4, 5]
new_grades = choices(a, k=23000)

b = list(range(1, 2001))
new_students = choices(b, k=23000)

c = list(range(1, 151))
new_courses = choices(c, k=23000)

df_new_students = pd.DataFrame(new_students, columns=["student_id"])

df_new_grades = pd.DataFrame(new_grades, columns=["grade"])

df_new_courses = pd.DataFrame(new_courses, columns=["course_id"])

df_grades.update(df_new_grades)
df_grades.update(df_new_courses)
df_grades.update(df_new_students)
df_grades.to_csv("grades_update.csv", index=False)
'''