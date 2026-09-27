import csv
 
 
def collect_marks(filename="students.csv"):
    """Ask the user for subjects and student marks, and save them to a CSV file."""
    subjects = ["Name", "Roll Number"]
    number_of_subjects = int(input("Enter the number of subjects: "))
    for i in range(number_of_subjects):
        subject_name = input("Enter the subject name: ")
        subjects.append(subject_name)
 
    number_of_students = int(input("Enter the number of students: "))
 
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(subjects)  # write header once
 
        for student in range(number_of_students):
            marks = []  # reset for every student
            name = input("Enter the name of the student: ")
            roll_number = input("Enter the roll number of the student: ")
            marks.append(name)
            marks.append(roll_number)
 
            for i in range(number_of_subjects):
                while True:
                    request = (
                        f"Enter {name}'s marks in {subjects[2 + i]} "
                        f"(0-100): "
                    )
                    mark = int(input(request))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    print("Invalid marks! Please enter a value between 0 and 100.")
 
            writer.writerow(marks)  # write once per student
 
    print(f"Data has been successfully saved to {filename}")
 
 
if __name__ == "__main__":
    print("Welcome to the Marks Management System")
    collect_marks()     