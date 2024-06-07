from analyse_data import courses_from_student_xy

students = courses_from_student_xy(int(input("Enter student_id: ")))
for student in students:
    print(student)
