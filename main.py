from sqlalchemy_utils import create_database, database_exists, drop_database
from engine import engine, engine_create, test_database_connection
from classes import Base
from import_data import import_data_csv, check_csv_files_exist
from analyse_data import (students_avg_grade_xy_ects, show_plot_frequency_avg_grade, all_students_from_country_xy,
                          courses_from_student_xy, courses_teaches_from_professor_xy)

# test connection to database
test_database_connection(engine_create)

# Check if DB already exists
if database_exists(engine):
    drop_database(engine)
    create_database(engine)
    print("Database existed. Dropped and created a new one.")
else:
    create_database(engine)
    print("Database did not exist. Created a new one.")

# Create all tables if not exist
Base.metadata.create_all(engine_create)
print("All tables created.")

# Check if all CSV files exist before importing data
if check_csv_files_exist():
    # Import data into the tables
    import_data_csv()
    print("Data imported successfully.")
else:
    print("One or more CSV files are missing. Data import aborted.")