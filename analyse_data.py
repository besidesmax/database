import matplotlib.pyplot as plt
from engine import engine_create
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, func
from classes import Student, Address, Program, Course, Professor, Grade
import pandas as pd

# provide the Session
Session = sessionmaker(bind=engine_create)
session = Session()


# get the avg_grade of all students which completed xy ECTS
# TODO: add exception-handler
def students_avg_grade_xy_ects(ects_input):
    """
    This Function returns the avg_grade off all Students which completed a specified amount of ECTS
    Input = specified amount of ECTS (e.g.: 100)
    """
    # Subquery to calculate the total ECTS per student
    total_ects_subquery = (select(Grade.student_id, func.sum(Course.ects).label("total_ects"))
                           .join(Course, Grade.course_id == Course.course_id)
                           .group_by(Grade.student_id)
                           .subquery())

    # Subquery to get student_ids with total ECTS greater than the input value
    query_student_id = (select(Student.student_id)
                        .join(total_ects_subquery, Student.student_id == total_ects_subquery.c.student_id)
                        .group_by(Student.student_id)
                        .where(total_ects_subquery.c.total_ects > ects_input)
                        .subquery())

    # Main query to get the average grade for the filtered students
    query = (select(Grade.student_id, Student.last_name, Student.first_name, func.avg(Grade.grade).label("avg_grade"))
             .join(Student, Grade.student_id == Student.student_id)
             .where(Student.student_id == query_student_id.c.student_id)
             .group_by(Grade.student_id)
             .order_by(Grade.student_id))

    results = session.execute(query).all()

    return results


# counts how many times the same avg_grade
def show_frequency_avg_grade(ects_input):
    """
    creates a plot which displays the avg_grades of all students,
    which completed a certain amount of ects (=Input)
    """
    # Get the data frame based on the input ECTS
    df = pd.DataFrame(students_avg_grade_xy_ects(ects_input))
    column_serie = df["avg_grade"]

    # Calculate the frequency of each average grade
    frequency = column_serie.value_counts().sort_index()
    df_frequency = pd.DataFrame(frequency, columns=["count"])

    count_list = df_frequency["count"].tolist()
    index_list = df_frequency.index.tolist()

    # Create a plot
    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(index_list, count_list, width=0.05, label="Grades")

    # Adding legend, grid, labels, and title
    ax.legend()
    ax.grid(visible=True, color="gray", linestyle='--', linewidth=0.5)
    ax.set_ylabel("Number of Students")
    ax.set_xlabel("Average Grade")
    ax.set_title("Distribution of Average Grades with Minimum ECTS")

    plt.show()


def show_all_students_from_country_xy(input_country: str):
    """
    shows all student from a country
    :param input_country:
    :return:
    """
    query = (select(Student.student_id, Student.student_number,
                    Student.first_name, Student.last_name, Address.country)
             .join(Address, Address.address_id == Student.address_id)
             .where(Address.country == input_country)
             .group_by(Student.student_id))

    results = session.execute(query).all()
    return results


def show_courses_from_student_xy(student_input):
    """
    shows which course student xy has completed
    :param student_input: student_id
    :return:
    """
    query = (select(Grade.student_id, Student.first_name, Student.last_name,
                    Course.course_id, Course.name, Program.name)
             .join(Student, Student.student_id == Grade.student_id)
             .join(Course, Course.course_id == Grade.course_id)
             .join(Program, Program.program_id == Course.program_id)
             .where(Grade.student_id == student_input)
             )

    results = session.execute(query).all()
    return results


tests = show_courses_from_student_xy(5)
for test in tests:
    print(test)


'''
students_with_over_100_ects = students_avg_grade_xy_ects(100)
df_students_with_over_100_ects = pd.DataFrame(students_with_over_100_ects)
print(df_students_with_over_100_ects)


dict_1 = {index_list[i]: count_list[i] for i in range(len(index_list))}
'''
