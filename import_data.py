import os
import pandas as pd
from engine import engine
from classes import Address, Student, Course, Program, Grade, Professor


# read csv-Data
df_address = pd.read_csv("addresses_2050.csv", encoding="utf-8")
df_student = pd.read_csv("students_2000.csv", encoding="utf-8")
df_study_program = pd.read_csv("study_program_13.csv", encoding="utf-8")
df_course = pd.read_csv("courses_150.csv", encoding="utf-8")
df_grades = pd.read_csv("grades_23000.csv", encoding="utf-8")
df_professor = pd.read_csv("professor_50.csv", encoding="utf-8")


def import_data_csv():

    # add student_2000.csv to database
    df_address.to_sql(con=engine, name=Address.__tablename__, if_exists="append", index=False)

    # add student_2000.csv to database
    df_student.to_sql(con=engine, name=Student.__tablename__, if_exists="append", index=False)

    # add study_programm_13.csv to database
    df_study_program.to_sql(con=engine, name=Program.__tablename__, if_exists="append", index=False)

    # add professor_50.csv to database
    df_professor.to_sql(con=engine, name=Professor.__tablename__, if_exists="append", index=False)

    # add courses_250.csv to database
    df_course.to_sql(con=engine, name=Course.__tablename__, if_exists="append", index=False)

    # add grades_2300.csv to database
    df_grades.to_sql(con=engine, name=Grade.__tablename__, if_exists="append", index=False)

def check_csv_files_exist():
    """
    Check if all the specified CSV files exist.

    Returns:
        bool: True if all files exist, False otherwise.
    """
    csv_files = ["addresses_2050.csv",
                 "students_2000.csv",
                 "study_program_13.csv",
                 "courses_150.csv",
                 "grades_23000.csv",
                 "professor_50.csv"
                 ]
    for file in csv_files:
        if not os.path.isfile(file):
            print(f"File not found: {file}")
            return False
    return True
