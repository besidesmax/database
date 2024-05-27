from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Address(Base):
    __tablename__ = "addresses"

    address_id = Column("address_id", Integer, primary_key=True)
    country = Column("country", String(100))
    city = Column("city", String(100))
    zip_code = Column("zip_code", Integer)
    street = Column("street", String(100))
    building_number = Column("building_number", Integer)

    def __init__(self, address_id, country, city, zip_code, street, building_number):
        self.address_id = address_id
        self.country = country
        self.city = city
        self.zip_code = zip_code
        self.street = street
        self.building_number = building_number

    def __repr__(self):
        return f"{self.address_id} , {self.country} , {self.city} , {self.zip_code} ,\
                 {self.street} , {self.building_number}"

class Student(Base):
    __tablename__ = "students"

    student_id = Column("student_id", Integer, primary_key=True)
    student_number = Column("student_number", Integer)
    first_name = Column("first_name", String(50))
    last_name = Column("last_name", String(50))
    date_of_birth = Column("date_of_birth", DateTime)
    address_id = Column("address_id", ForeignKey("addresses.address_id"))

    def __init__(self, student_id, student_number, first_name, last_name, date_of_birth, address_id):
        self.student_id = student_id
        self.student_number = student_number
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address_id = address_id

    def __repr__(self):
        return f"{self.student_id} , {self.student_number} , {self.first_name} , {self.last_name} , \
                 {self.date_of_birth} , {self.address_id}"


class Course(Base):
    __tablename__ = "courses"

    course_id = Column("course_id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(50))
    ects = Column("ects", Integer)
    active = Column("active", Boolean)
    optional = Column("optional", Boolean)
    study_program = Column("study_program", ForeignKey("study_program.program_id"))
    requirement_1 = Column("requirement_1", ForeignKey("courses.course_id"))
    requirement_2 = Column("requirement_2", ForeignKey("courses.course_id"))

    def __init__(self, course_id, name, ects, active, optional, study_program, requirement_1,
                 requirement_2):
        self.course_id = course_id
        self.name = name
        self.ects = ects
        self.active = active
        self.optional = optional
        self.study_program = study_program
        self.requirement_1 = requirement_1
        self.requirement_2 = requirement_2

    def __repr__(self):  # TODO show course.name insteadof course.id at requirements also study_program
        return f"{self.course_id} , {self.name} , {self.ects} , {self.active} , {self.optional} \
                {self.study_program} , {self.requirement_1} , {self.requirement_2}"


class Program(Base):
    __tablename__ = "study_program"

    program_id = Column("program_id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(50))

    def __init__(self, program_id, name):
        self.program_id = program_id
        self.name = name

    def __repr__(self):
        return f" {self.program_id} , {self.name}"


class Professor(Base):
    __tablename__ = "professor"

    professor_id = Column("professor_id", Integer, primary_key=True, nullable=False)
    first_name = Column("first_name", String(50))
    last_name = Column("last_name", String(50))
    date_of_birth = Column("date_of_birth", DateTime)
    address_id = Column("address_id", ForeignKey("addresses.address_id"))

    def __init__(self, professor_id, first_name, last_name, date_of_birth, address_id):
        self.professor_id = professor_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address_id = address_id

    def __repr__(self):
        return f"{self.professor_id} , {self.first_name} , {self.last_name} , \
                 {self.date_of_birth} , {self.address_id}"


class Grade(Base):
    __tablename__ = "grades"

    grade_id = Column("grades_id", Integer, primary_key=True, autoincrement=True)
    course_id = Column("course_id", ForeignKey("courses.course_id"))
    student_id = Column("student_id", ForeignKey("students.student_id"))
    grade = Column("grades", Integer)

    def __init__(self, grade_id, course_id, student_id, grade):
        self.grade_id = grade_id
        self.course_id = course_id
        self.student_id = student_id
        self.grade = grade

    def __repr__(self):
        return f" {self.grade_id} , {self.course_id} , {self.student_id} , {self.grade}"



