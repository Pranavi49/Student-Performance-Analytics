
import pandas as pd

from functions import (
    SUBJECTS,
    calculate_total,
    calculate_average,
    assign_grade,
    assign_result,
    calculate_statistics,
    subject_analysis,
    find_top_performers
)

# Load the dataset
students = pd.read_csv("students.csv")

print("=" * 60)
print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 60)

# Display dataset information
print("\n1. DATASET OVERVIEW")
print("Total students:", len(students))
print("Departments:", students["Department"].nunique())

# Calculate totals and averages
students = calculate_total(students)
students = calculate_average(students)

# Assign grades and results using loops
grades = []
results = []

for _, row in students.iterrows():
    grades.append(assign_grade(row["Average_Marks"]))
    results.append(assign_result(row))

students["Grade"] = grades
students["Result"] = results

# Display individual student results
print("\n2. STUDENT PERFORMANCE REPORT")
print(
    students[
        ["Student_ID", "Name", "Total_Marks",
         "Average_Marks", "Grade", "Result"]
    ].round(2).to_string(index=False)
)

# Overall class statistics
print("\n3. CLASS PERFORMANCE STATISTICS")

statistics = calculate_statistics(students)

print("Highest student average:", round(statistics["Highest_Average"], 2))
print("Lowest student average:", round(statistics["Lowest_Average"], 2))
print("Overall class average:", round(statistics["Class_Average"], 2))

# Pass/fail statistics
print("\n4. PASS/FAIL ANALYSIS")
print(students["Result"].value_counts().to_string())

# Subject-wise analysis
print("\n5. SUBJECT-WISE PERFORMANCE")
print(subject_analysis(students).round(2).to_string())

# Top five students
print("\n6. TOP FIVE PERFORMERS")
top_students = find_top_performers(students)

print(
    top_students[
        ["Student_ID", "Name", "Average_Marks", "Grade"]
    ].round(2).to_string(index=False)
)

# Attendance analysis
print("\n7. ATTENDANCE ANALYSIS")
print("Average attendance:", round(students["Attendance"].mean(), 2), "%")

low_attendance = students[students["Attendance"] < 75]

print("Students with attendance below 75%:")

if low_attendance.empty:
    print("None")
else:
    print(
        low_attendance[["Student_ID", "Name", "Attendance"]]
        .to_string(index=False)
    )

# Save the analyzed data
students.to_csv("student_performance_report.csv", index=False)

print("\nAnalysis completed successfully!")
print("Report saved as student_performance_report.csv")
