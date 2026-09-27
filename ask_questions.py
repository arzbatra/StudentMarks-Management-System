import google.generativeai as genai
 
from analyze_marks import load_data
 
model = None
 
 
def configure_model():
    """Ask for an API key and set up the Gemini model."""
    global model
    genai.configure(api_key=input("Enter Your API Key to get real time analysis of data: "))
    model = genai.GenerativeModel("gemini-3.6-flash")
 
 
def ask_questions_about_data(data):
    """Let the user ask questions about the marks data until they type 'exit'."""
    data_as_text = data.to_csv()
 
    print("\nYou can now ask questions about the data. Type 'exit' to stop.")
 
    while True:
        question = input("\nAsk a question about the data: ")
        if question.lower() == "exit":
            break
 
        prompt = (
            f"Here is student marks data in CSV format:\n\n{data_as_text}\n\n"
            f"Question: {question}\n\nAnswer based only on this data."
        )
 
        response = model.generate_content(prompt)
        print(f"\nBot: {response.text}")
 
 
if __name__ == "__main__":
    configure_model()
    student_data = load_data()
    ask_questions_about_data(student_data)