from analyse_data import courses_teaches_from_professor_xy

professors = courses_teaches_from_professor_xy(int(input("Enter professor_id: ")))
for professor in professors:
    print(professor)
