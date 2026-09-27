import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
 
def load_data(filename="students.csv"):
    """Load student marks from CSV and add an Average_Marks column."""
    student_data = pd.read_csv(filename)
    student_data.set_index("Name", inplace=True)
    student_data["Average_Marks"] = np.mean(student_data.iloc[:, 2:], axis=1)
    return student_data
 
 
def get_subject_columns(student_data):
    """Return just the subject columns (excludes Roll Number and Average_Marks)."""
    return [c for c in student_data.columns if c not in ("Roll Number", "Average_Marks")]
 
 
def all_student_comparison(student_data):
    """Bar chart comparing average marks across all students."""
    analysis_series = pd.Series(student_data["Average_Marks"])
    analysis_series.plot(kind="bar")
    plt.title("Average Marks - All Students")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.show()
 
 
def one_student_analysis(student_data, subject_columns):
    """Bar chart of one student's marks across subjects."""
    new_df = student_data[subject_columns]
    name = input("Enter the name of the student: ")
    new_df.loc[name].plot(kind="bar")
    plt.title(f"{name}'s Marks by Subject")
    plt.ylabel("Marks")
    plt.tight_layout()
    plt.show()
 
 
if __name__ == "__main__":
    student_data = load_data()
    subject_columns = get_subject_columns(student_data)
    all_student_comparison(student_data)
    one_student_analysis(student_data, subject_columns)