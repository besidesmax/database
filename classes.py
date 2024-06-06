import datetime
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from typing import Annotated

# define length of String
str_100 = Annotated[str, mapped_column(String(100))]


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    student_number: Mapped[int] = mapped_column()
    first_name: Mapped[str_100] = mapped_column()
    last_name: Mapped[str_100] = mapped_column()
    date_of_birth: Mapped[datetime.date] = mapped_column()
    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.address_id"))
    address: Mapped["Address"] = relationship("Address", uselist=False, back_populates="student")
    grade: Mapped["Grade"] = relationship("Grade", uselist=True, back_populates="student")


class Address(Base):
    __tablename__ = "addresses"

    address_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    country: Mapped[str_100] = mapped_column()
    city: Mapped[str_100] = mapped_column()
    zip_code: Mapped[int] = mapped_column()
    street: Mapped[str_100] = mapped_column()
    building_number: Mapped[int] = mapped_column()
    student: Mapped["Student"] = relationship("Student", uselist=False, back_populates="address")
    professor: Mapped["Professor"] = relationship("Professor", uselist=False, back_populates="address")


class Program(Base):
    __tablename__ = "study_program"

    program_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str_100] = mapped_column()
    course: Mapped["Course"] = relationship("Course", uselist=True, back_populates="study_program")


class Course(Base):
    __tablename__ = "courses"

    course_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str_100] = mapped_column()
    ects: Mapped[int] = mapped_column()
    active: Mapped[bool] = mapped_column()
    optional: Mapped[bool] = mapped_column()
    program_id: Mapped[int] = mapped_column(ForeignKey("study_program.program_id"))
    study_program: Mapped["Program"] = relationship("Program", uselist=True, back_populates="course")
    grade: Mapped["Grade"] = relationship("Grade", uselist=True, back_populates="course")
    professor_id: Mapped[int] = mapped_column(ForeignKey("professor.professor_id"))
    professor: Mapped["Professor"] = relationship("Professor", uselist=True, back_populates="courses")


class Professor(Base):
    __tablename__ = "professor"

    professor_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    first_name: Mapped[str_100] = mapped_column()
    last_name: Mapped[str_100] = mapped_column()
    date_of_birth: Mapped[datetime.date] = mapped_column()
    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.address_id"))
    address: Mapped["Address"] = relationship("Address", uselist=False, back_populates="professor")
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.course_id"))
    courses: Mapped["Course"] = relationship("Course", uselist=True, back_populates="professor")


class Grade(Base):
    __tablename__ = "grades"

    grade_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.course_id"))
    course: Mapped["Course"] = relationship("Course", uselist=True, back_populates="grade")
    student_id: Mapped[int] = mapped_column(ForeignKey("students.student_id"))
    student: Mapped["Student"] = relationship("Student", uselist=True, back_populates="grade")
    grade: Mapped[int] = mapped_column()
