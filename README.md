# Database

## Overview
Database is a program to create a database and/ or analyse the data of a database with a few given functions
## Installation Instructions

### Prerequisites
- Python 3.12
- import database.yaml with anconda

## Usage Instructions
1. Clone the repository
2. create a sql-server  and remeber: hostname, port, username and password
3. run main.py and put hostname, port, username and password in - this will be saved as default and if it isn't change, the next time you just need to press enter.
4.For analysing the data you have 5 function:
-students_avg_grade_xy_ects: This function returns the average grade of all students
    who have completed more than a specified amount of ECTS credits.

-show_plot_frequency_avg_grade: Plots the frequency distribution of average grades for students with at least a specified number of ECTS credits.

-all_students_from_country_xy:  Retrieves and displays a list of students from a specified country.

-courses_from_student_xy: shows which course student xy has completed

-courses_teaches_from_professor_xy:  Retrieves a list of courses taught by a specified professor along with the program name.

## Features

## Dependencies
needed python libraries(insall with conda):
-sqlalchemy  2.0.25 
-sqlalchemy-utils 0.41.1
-pymysql 1.0.2  
-pandas 2.2.1
-matplotlib 3.8.4 



