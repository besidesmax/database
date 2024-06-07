# Database

## Overview
Database is a program to create a database and analyse the data of a database with a few given functions
## Installation Instructions

### Prerequisites
- Python 3.12
- Anaconda Navigator
- MySQL Server 8.0

## Usage Instructions
1. Clone the repository
2. create a MySQL-server  and remember: hostname, port, username and password
3. use Anaconda Navigator and import the database.yaml from the repository
4. run main.py
5. needed input: hostname, port, username and password in - These will be saved as defaults for future runs.
6. for data analysis you can run:
    - students_avg_grade_xy_ects.py
    - show_plot_frequency_avg_grade.py
    - all_students_from_country_xy.py
    - courses_from_student_xy.py
    - courses_teaches_from_professor_xy.py
7. or you can input the func from analyse_data in a new file and work with them
   
### Analysis Functions
The program provides the following functions for data analysis:

- **students_avg_grade_xy_ects**: Returns the average grade of all students who have completed more than a specified number of ECTS credits.
- **show_plot_frequency_avg_grade**: Plots the frequency distribution of average grades for students with at least a specified number of ECTS credits.
- **all_students_from_country_xy**: Retrieves and displays a list of students from a specified country.
- **courses_from_student_xy**: Shows the courses that a specified student has completed.
- **courses_teaches_from_professor_xy**: Retrieves a list of courses taught by a specified professor along with the program name.

## Features
- Create and manage a SQL database.
- Analyze and visualize student and course data.
- Retrieve detailed information on students, courses, and professors.

## Dependencies
The following Python libraries are required and can be installed via Anaconda:
- sqlalchemy 2.0.25
- sqlalchemy-utils 0.41.1
- pymysql 1.0.2  
- pandas 2.2.1
- matplotlib 3.8.4
