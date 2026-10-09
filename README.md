# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python-based data analysis project that processes student academic records and generates useful performance insights. It uses Python, NumPy, and Pandas to calculate marks, assign grades, identify pass/fail results, analyze subject-wise performance, and identify top-performing students.

## Objectives
- Analyze student academic performance using Python.
- Calculate total and average marks for each student.
- Assign grades using predefined grading criteria.
- Identify students who pass or fail.
- Analyze class and subject-wise performance.
- Identify top-performing students.
- Examine student attendance.
- Generate a processed CSV report.

## Technologies Used
- Python
- NumPy
- Pandas
- Visual Studio Code
- Git and GitHub

## Dataset Description
The dataset contains 20 student records, including:
- Student ID
- Name
- Department
- Mathematics marks
- Physics marks
- Chemistry marks
- English marks
- Computer Science marks
- Attendance percentage

Each subject is assumed to be scored out of 100.

## Features
1. Student dataset loading and validation.
2. Total and average marks calculation.
3. Automatic grade assignment.
4. Pass/fail identification.
5. Class performance statistics.
6. Subject-wise average analysis.
7. Top five performers identification.
8. Department-wise performance analysis.
9. Attendance analysis.
10. CSV report generation.
11. Automated tests for key calculations and validation.

## Grading Criteria
| Average Marks | Grade |
|---|---|
| 90 and above | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

A student is considered to have passed if they score at least 35 marks in every subject.

These are the grading and passing rules defined for this project.

## Project Structure
```text
Stu_Outcome_Analytics/
├── main.py
├── functions.py
├── students.csv
├── test_project.py
├── README.md
└── student_performance_report.csv
```

The generated report file appears after running the main program.

## Installation and Execution

### 1. Install Python
Install Python and ensure it is available from your terminal.

### 2. Install Dependencies
Open the terminal in the project directory and run:

```bash
python -m pip install numpy pandas
```

### 3. Run the Project
Execute:

```bash
python main.py
```

### 4. Run Automated Tests
Execute:

```bash
python test_project.py
```

## Expected Outcomes
The program displays:
- Student-wise total and average marks.
- Grades and pass/fail results.
- Highest, lowest, and overall class averages.
- Pass/fail statistics.
- Subject-wise average marks.
- Top five performers.
- Attendance statistics and students with attendance below 75%.
- Department-wise performance and grade distribution, when those sections are implemented in the main program.

The analyzed student data is saved to `student_performance_report.csv`.

## Learning Outcomes
This project demonstrates the use of Python variables, functions, loops, conditions, NumPy numerical operations, Pandas DataFrames, data validation, and basic data analysis.

## Author
**Name:** Pranavi Nallapuri

## GitHub Repository
https://github.com/Pranavi49/Student-Performance-Analytics