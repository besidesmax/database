from sqlalchemy import Column, Integer, String, DateTime
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
