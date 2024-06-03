from engine import engine_create
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, func
from classes import Student, Address, Program, Course, Professor, Grade
import pandas as pd

# provide the Session
Session = sessionmaker(bind=engine_create)
session = Session()


# get all students wich have completed more than 100 ects


def get_students_with_over_100_ects():
    # subquery to calculate the total ECTS per student
    total_ects_subquery = (select(Grade.student_id, func.sum(Course.ects).label("total_ects"))
                           .join(Course, Grade.course_id == Course.course_id)
                           .group_by(Grade.student_id)
                           .subquery())
    # gets a query with all student_id's where the student have in total more than 100 ECTS
    query_student_id = (select(Student.student_id)
                        .join(total_ects_subquery, Student.student_id == total_ects_subquery.c.student_id)
                        .group_by(Student.student_id)
                        .where(total_ects_subquery.c.total_ects > 100)
                        .subquery())

    query = (select(Grade.student_id, Student.first_name, func.avg(Grade.grade).label("avg_grade"))
             .join(Student, Grade.student_id == Student.student_id)
             .group_by(Student.student_id)
             .where(Student.student_id == query_student_id.c.student_id))

    results = session.execute(query).all()

    return results


students_with_over_100_ects = get_students_with_over_100_ects()
df_students_with_over_100_ects = pd.DataFrame(students_with_over_100_ects)
print(df_students_with_over_100_ects)

'''
# Assuming you have an engine created and bound to your database
# engine = create_engine("your_database_url")
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_students_with_over_100_ects(Session):
    # Subquery to calculate the total ECTS per student
    total_ects_subquery = (
        select(
            Grade.student_id,
            func.sum(Course.ects).label("total_ects")
        )
        .join(Course, Grade.course_id == Course.course_id)
        .group_by(Grade.student_id)
        .subquery()
    )

    # Main query to select students with more than 100 ECTS
    query = (
        select(Student)
        .join(total_ects_subquery, Student.student_id == total_ects_subquery.c.student_id)
        .where(total_ects_subquery.c.total_ects > 100)
    )

    return session.execute(query).scalars().all()

# Usage
# with session as Session:
#     students = get_students_with_over_100_ects(session)
#     for student in students:
#         print(student.first_name, student.last_name, student.student_number)

'''
