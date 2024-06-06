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
    This function returns the average grade of all students
    who have completed more than a specified amount of ECTS credits.

    Args:
        ects_input (int): The minimum number of ECTS credits to filter students by.

    Returns:
        List of tuples: Each tuple contains student_id, last_name, first_name, and avg_grade.
    """
    # Check if the input is positive int
    if not isinstance(ects_input, int) or ects_input < 0:
        raise TypeError("The ects_input must be a non-negative integer.")

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
def show_plot_frequency_avg_grade(ects_input):
    """
    Plots the frequency distribution of average grades for students with at least a specified number of ECTS credits.

    Args:
        ects_input (int): The minimum number of ECTS credits to filter students by.

    Returns:
        None: This function displays a plot of the frequency distribution of average grades.
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


def all_students_from_country_xy(input_country: str):
    """
    Retrieves and displays a list of students from a specified country.

    Args:
        input_country (str): The country to filter students by.

    Returns:
        str: A formatted string containing student details including:
             - student_id
             - student_number
             - first_name
             - last_name
             - country
    """
    # Check if the input is a string
    if not isinstance(input_country, str):
        raise TypeError("The input_country must be a string.")

    query = (select(Student.student_id, Student.student_number,
                    Student.first_name, Student.last_name, Address.country)
             .join(Address, Address.address_id == Student.address_id)
             .where(Address.country == input_country)
             .group_by(Student.student_id))

    results = session.execute(query).all()

    # Check if there are no results
    if not results:
        return "No student from this country"

    # Prepare the header row with column names
    header = f"{'student_id':<12} {'student_number':<15} {'first_name':<12} {'last_name':<12} {'country':<10}\n"
    header += '-' * 65 + '\n'

    # Prepare the data rows
    rows = [
        (f"{student.student_id:<12} {student.student_number:<15} "
         f"{student.first_name:<12} {student.last_name:<12} {student.country:<10}")
        for student in results]

    # Combine header and rows
    result_string = header + '\n'.join(rows)
    return result_string


def courses_from_student_xy(student_input):
    """
    shows which course student xy has completed
    :param student_input: student_id
    :return: List of tuples with student and course information
    """
    # Checks if the input is an int higher than 0
    if not isinstance(student_input, int) or student_input < 1:
        raise TypeError("The student_input must be a non-negative integer, higher than 0")

    # Checks if the input is a element of Student.student_id
    # gets all element of Student.student_id
    query_element = select(Student.student_id)
    result_element = (pd.DataFrame(session.execute(query_element).all()))["student_id"].tolist()
    if student_input not in result_element:
        raise ValueError("The student_input is not a student_id")

    # main query
    query = (select(Grade.student_id, Student.first_name, Student.last_name,
                    Course.course_id, Course.name, Program.name.label('program_name'))
             .join(Student, Student.student_id == Grade.student_id)
             .join(Course, Course.course_id == Grade.course_id)
             .join(Program, Program.program_id == Course.program_id)
             .where(Grade.student_id == student_input)
             )

    results = session.execute(query).all()

    return results


def courses_teaches_from_professor_xy(input_prof_id):
    """
    Retrieves a list of courses taught by a specified professor along with the program name.

    Args:
        input_prof_id (int): The ID of the professor.

    Returns:
        List[Dict]: A list of dictionaries, each containing the professor's details,
                    course ID, course name, and program name.
    """
    # Checks if the input is an int higher than 0
    if not isinstance(input_prof_id, int) or input_prof_id < 1:
        raise TypeError("The input_prof_id must be a non-negative integer, higher than 0")

    # Checks if the input is an element of Student.student_id
    # gets all element of Professor.professor_id
    query_element = select(Professor.professor_id)
    result_element = (pd.DataFrame(session.execute(query_element).all()))["professor_id"].tolist()
    if input_prof_id not in result_element:
        raise ValueError("The input_prof_id is not a professor_id")

    # Construct the query
    query = (select(Professor.professor_id, Professor.first_name, Professor.last_name,
                    Course.course_id, Course.name.label("course_name"), Program.name.label("program_name"))
             .join(Course, Course.professor_id == Professor.professor_id)
             .join(Program, Program.program_id == Course.program_id)
             .where(Professor.professor_id == input_prof_id))

    # Execute the query
    results = session.execute(query).all()

    # Convert the results to a list of dictionaries
    result_list = [
        {
            "professor_id": row.professor_id,
            "first_name": row.first_name,
            "last_name": row.last_name,
            "course_id": row.course_id,
            "course_name": row.course_name,
            "program_name": row.program_name
        }
        for row in results
    ]

    return result_list

