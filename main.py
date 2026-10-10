
import pandas as pd

from functions import (
    SUBJECTS,
    validate_dataset,
    calculate_total,
    calculate_average,
    assign_grade,
    assign_result,
    calculate_statistics,
    subject_analysis,
    find_top_performers
)


def main():
    # 1. Load and validate the dataset
    print("=" * 65)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)

    students = pd.read_csv("students.csv")

    validate_dataset(students)
    print("\nDataset validation successful!")

    print("\n1. DATASET OVERVIEW")
    print("-" * 40)
    print("Total students:", len(students))
    print("Total departments:", students["Department"].nunique())
    print("Total subjects:", len(SUBJECTS))
    print("Available columns:", len(students.columns))

    # 2. Calculate total and average marks
    students = calculate_total(students)
    students = calculate_average(students)

    # 3. Assign grades and pass/fail results
    grades = []
    results = []

    for _, row in students.iterrows():
        grades.append(assign_grade(row["Average_Marks"]))
        results.append(assign_result(row))

    students["Grade"] = grades
    students["Result"] = results

    # 4. Display student performance report
    print("\n2. STUDENT PERFORMANCE REPORT")
    print("-" * 65)

    report_columns = [
        "Student_ID",
        "Name",
        "Department",
        "Total_Marks",
        "Average_Marks",
        "Grade",
        "Result"
    ]

    print(
        students[report_columns]
        .round(2)
        .to_string(index=False)
    )

    # 5. Overall class performance statistics
    print("\n3. CLASS PERFORMANCE STATISTICS")
    print("-" * 40)

    statistics = calculate_statistics(students)

    print(
        "Highest student average:",
        round(statistics["Highest_Average"], 2)
    )
    print(
        "Lowest student average:",
        round(statistics["Lowest_Average"], 2)
    )
    print(
        "Overall class average:",
        round(statistics["Class_Average"], 2)
    )

    # 6. Pass/fail analysis
    print("\n4. PASS/FAIL ANALYSIS")
    print("-" * 40)

    result_counts = (
        students["Result"]
        .value_counts()
        .reindex(["Pass", "Fail"], fill_value=0)
    )

    print(result_counts.to_string())

    pass_rate = (
        (students["Result"] == "Pass").mean() * 100
    )

    print(f"Pass percentage: {pass_rate:.2f}%")

    # 7. Subject-wise performance analysis
    print("\n5. SUBJECT-WISE PERFORMANCE")
    print("-" * 40)

    subject_report = subject_analysis(students)
    print(subject_report.round(2).to_string())

    print(
        "\nBest-performing subject:",
        subject_report.idxmax()
    )
    print(
        "Lowest-performing subject:",
        subject_report.idxmin()
    )

    # 8. Top five performers
    print("\n6. TOP FIVE PERFORMERS")
    print("-" * 40)

    top_students = find_top_performers(students, count=5)

    top_columns = [
        "Student_ID",
        "Name",
        "Average_Marks",
        "Grade"
    ]

    print(
        top_students[top_columns]
        .round(2)
        .to_string(index=False)
    )

    # 9. Attendance analysis
    print("\n7. ATTENDANCE ANALYSIS")
    print("-" * 40)

    average_attendance = students["Attendance"].mean()

    print(f"Average attendance: {average_attendance:.2f}%")

    low_attendance = students[
        students["Attendance"] < 75
    ]

    print("\nStudents with attendance below 75%:")

    if low_attendance.empty:
        print("No students found.")
    else:
        print(
            low_attendance[
                ["Student_ID", "Name", "Attendance"]
            ].to_string(index=False)
        )

    # 10. Department-wise performance analysis
    print("\n8. DEPARTMENT-WISE PERFORMANCE")
    print("-" * 65)

    department_report = students.groupby("Department").agg(
        Total_Students=("Student_ID", "count"),
        Average_Performance=("Average_Marks", "mean"),
        Average_Attendance=("Attendance", "mean"),
        Passed_Students=(
            "Result",
            lambda results: (results == "Pass").sum()
        ),
        Failed_Students=(
            "Result",
            lambda results: (results == "Fail").sum()
        )
    )

    print(department_report.round(2).to_string())

    best_department = department_report[
        "Average_Performance"
    ].idxmax()

    print(
        "\nDepartment with the highest average performance:",
        best_department
    )

    # 11. Grade distribution
    print("\n9. GRADE DISTRIBUTION")
    print("-" * 40)

    grade_order = ["A+", "A", "B", "C", "D", "F"]

    grade_counts = (
        students["Grade"]
        .value_counts()
        .reindex(grade_order, fill_value=0)
    )

    print(grade_counts.to_string())

    # 12. Save the complete performance report
    output_file = "student_performance_report.csv"

    students.to_csv(output_file, index=False)

    print("\n10. REPORT GENERATION")
    print("-" * 40)
    print("Report saved successfully:", output_file)

    print("\n" + "=" * 65)
    print("       ANALYSIS COMPLETED SUCCESSFULLY!")
    print("=" * 65)


if __name__ == "__main__":
    main()
