# Database

## Overview
The Database program is designed to create a MySQL database and analyze its data using various built-in functions. It enables detailed data management and analysis, particularly for student and course information.

## Installation Instructions

### Prerequisites
- Python 3.12
- Anaconda Navigator
- MySQL Server 8.0

### Steps to Install
1. Clone the repository
2. Create a MySQL Server:
   - Set up a MySQL server and take note of the following details: hostname, port, username, and password.
3. Import Conda Environment:
   - Open Anaconda Navigator.
   - Import the `database.yaml` file from the cloned repository to set up the required environment.
4. Run the Main Program
   - Enter the MySQL server details (hostname, port, username, and password) when prompted. These will be saved as defaults for future ru

## Usage Instructions   
### Analysis Functions
For data analysis, you can run the following scripts directly:

- **students_avg_grade_xy_ects.py**: Returns the average grade of all students who have completed more than a specified number of ECTS credits.
- **show_plot_frequency_avg_grade.py**: Plots the frequency distribution of average grades for students with at least a specified number of ECTS credits.
- **all_students_from_country_xy.py**: Retrieves and displays a list of students from a specified country.
- **courses_from_student_xy.py**: Shows the courses that a specified student has completed.
- **courses_teaches_from_professor_xy.py**: Retrieves a list of courses taught by a specified professor along with the program name.

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
