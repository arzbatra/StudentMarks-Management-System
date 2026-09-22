import csv
import pandas as pd
 
 
def collect_and_save_marks(filename="students.csv"):
    """Ask the user for student marks and write them to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
 
        no_of_students = int(input("Enter the number of students you want to enter: "))
        no_of_subjects = input(
            "Enter the name of subjects you want to enter (include Name as a field in your input"
        )
        titles = no_of_subjects.split(",")
        writer.writerow(titles)
 
        while no_of_students > 0:
            values = input(f"Enter the values in the same order as {titles}: ")
            no_of_students -= 1
            writer.writerow(values.split(","))
            