from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    students_id = Column("students_ID", Integer, primary_key=True, nullable=False)
    first_name = Column("first_name", String(50))
    last_name = Column("last_name", String(50))
    date_of_birth = Column("date_of_birth", DateTime)
    address = Column("address", String(100))

    def __init__(self, students_id, first_name, last_name, date_of_birth, address):
        self.students_id = students_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address

    def __repr__(self):
        return f"{self.students_id} , {self.first_name} , {self.last_name} , \
                 {self.date_of_birth} , {self.address}"


class Course(Base):
    __tablename__ = "courses"

    course_id = Column("course_id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(50))
    ects = Column("ects", Integer)
    active = Column("active", Boolean)
    optional = Column("optional", Boolean)
    requirement_1 = Column("requirement_1", ForeignKey("courses.course_id"))
    requirement_2 = Column("requirement_2", ForeignKey("courses.course_id"))
    requirement_3 = Column("requirement_3", ForeignKey("courses.course_id"))
    requirement_4 = Column("requirement_4", ForeignKey("courses.course_id"))
    requirement_5 = Column("requirement_5", ForeignKey("courses.course_id"))

    def __init__(self, course_id, name, ects, active, optional, requirement_1,
                 requirement_2, requirement_3, requirement_4, requirement_5):
        self.course_id = course_id
        self.name = name
        self.ects = ects
        self.active = active
        self.optional = optional
        self.requirement_1 = requirement_1
        self.requirement_2 = requirement_2
        self.requirement_3 = requirement_3
        self.requirement_4 = requirement_4
        self.requirement_5 = requirement_5

    def __repr__(self):
        return (F"{self.course_id} , {self.name} , {self.ects} , {self.active} , {self.optional} \
                {self.requirement_1} , {self.requirement_2} , {self.requirement_3} \
                {self.requirement_4} , {self.requirement_5}")
