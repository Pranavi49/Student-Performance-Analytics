
import numpy as np

# Subject columns used for calculating marks
SUBJECTS = [
    "Maths",
    "Physics",
    "Chemistry",
    "English",
    "Computer_Science"
]


# Calculate total marks for each student
def calculate_total(data):
    data["Total_Marks"] = data[SUBJECTS].sum(axis=1)
    return data


# Calculate average marks for each student
def calculate_average(data):
    data["Average_Marks"] = np.mean(
        data[SUBJECTS].to_numpy(), axis=1
    )
    return data


# Assign grades based on average marks
def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Determine pass or fail
def assign_result(row):
    if all(row[subject] >= 35 for subject in SUBJECTS):
        return "Pass"
    else:
        return "Fail"


# Calculate class performance statistics
def calculate_statistics(data):
    averages = data["Average_Marks"].to_numpy()

    return {
        "Highest_Average": np.max(averages),
        "Lowest_Average": np.min(averages),
        "Class_Average": np.mean(averages)
    }


# Analyze average marks subject-wise
def subject_analysis(data):
    return data[SUBJECTS].mean().sort_values(ascending=False)


# Identify top-performing students
def find_top_performers(data, count=5):
    return data.nlargest(count, "Average_Marks")




import pandas as pd


def validate_dataset(data):
    """Validate student records before analysis."""

    required_columns = [
        "Student_ID",
        "Name",
        "Department",
        *SUBJECTS,
        "Attendance"
    ]

    # Check required columns
    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check for an empty dataset
    if data.empty:
        raise ValueError("The student dataset is empty.")

    # Check for missing values
    if data[required_columns].isnull().any().any():
        raise ValueError("The dataset contains missing values.")

    # Check duplicate student IDs
    if data["Student_ID"].duplicated().any():
        raise ValueError("Duplicate student IDs found.")

    # Validate marks and attendance
    for column in SUBJECTS + ["Attendance"]:
        data[column] = pd.to_numeric(
            data[column], errors="raise"
        )

        if not data[column].between(0, 100).all():
            raise ValueError(
                f"{column} must contain values between 0 and 100."
            )

    return True
