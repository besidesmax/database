from engine import engine_create
from sqlalchemy.orm import sessionmaker
from classes import Grade, Student, Program

# provide the Session
Session = sessionmaker(bind=engine_create)
session = Session()

# show all students witch have a grade in course 5

programms = session.query(Program).filter_by(program_id="5").all()

for program in programms:
    print(f'{program.name}')