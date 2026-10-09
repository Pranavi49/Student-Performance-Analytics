
import pandas as pd

from functions import (
    SUBJECTS,
    calculate_total,
    calculate_average,
    assign_grade,
    assign_result,
    calculate_statistics,
    subject_analysis,
    find_top_performers,
    validate_dataset
)


def test_student_calculations():
    data = pd.DataFrame([{
        "Student_ID": 1,
        "Name": "Test Student",
        "Department": "CSE",
        "Maths": 80,
        "Physics": 70,
        "Chemistry": 90,
        "English": 60,
        "Computer_Science": 100,
        "Attendance": 95
    }])

    assert validate_dataset(data)

    calculate_total(data)
    calculate_average(data)

    assert data.loc[0, "Total_Marks"] == 400
    assert data.loc[0, "Average_Marks"] == 80

    assert assign_grade(95) == "A+"
    assert assign_grade(85) == "A"
    assert assign_grade(75) == "B"
    assert assign_grade(65) == "C"
    assert assign_grade(55) == "D"
    assert assign_grade(40) == "F"

    assert assign_result(data.iloc[0]) == "Pass"

    print("Student calculations: PASSED")


def test_failing_student():
    student = pd.Series({
        "Maths": 34,
        "Physics": 80,
        "Chemistry": 80,
        "English": 80,
        "Computer_Science": 80
    })

    assert assign_result(student) == "Fail"

    print("Pass/fail rules: PASSED")


def test_invalid_marks():
    data = pd.DataFrame([{
        "Student_ID": 1,
        "Name": "Invalid Student",
        "Department": "CSE",
        "Maths": 105,
        "Physics": 70,
        "Chemistry": 90,
        "English": 60,
        "Computer_Science": 100,
        "Attendance": 95
    }])

    try:
        validate_dataset(data)
    except ValueError:
        print("Invalid marks validation: PASSED")
    else:
        raise AssertionError("Invalid marks were not rejected")


def test_dataset_analysis():
    students = pd.read_csv("students.csv")
    validate_dataset(students)

    calculate_total(students)
    calculate_average(students)

    stats = calculate_statistics(students)
    subjects = subject_analysis(students)
    top_students = find_top_performers(students)

    assert len(students) == 20
    assert round(stats["Highest_Average"], 2) == 97.0
    assert round(stats["Lowest_Average"], 2) == 34.0
    assert round(stats["Class_Average"], 2) == 74.51
    assert subjects.index[0] == "Computer_Science"
    assert top_students.iloc[0]["Name"] == "Ishita"

    print("Dataset analysis: PASSED")


if __name__ == "__main__":
    test_student_calculations()
    test_failing_student()
    test_invalid_marks()
    test_dataset_analysis()

    print("\nAll tests passed successfully!")
