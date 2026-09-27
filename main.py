from collect_marks import collect_marks
from analyze_marks import load_data, get_subject_columns, all_student_comparison, one_student_analysis
from ask_questions import configure_model, ask_questions_about_data
 
 
def main():
    print("Welcome to the Marks Management System")
 
    collect_marks()
 
    student_data = load_data()
    subject_columns = get_subject_columns(student_data)
 
    all_student_comparison(student_data)
    one_student_analysis(student_data, subject_columns)
 
    configure_model()
    ask_questions_about_data(student_data)
 
 
if __name__ == "__main__":
    main()