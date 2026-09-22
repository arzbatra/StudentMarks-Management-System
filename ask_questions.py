import os
import google.generativeai as genai
 
from collect_marks import load_and_process_marks
 
# Set your key as an environment variable instead of hardcoding it:
#   export GOOGLE_API_KEY="your-key-here"      (Mac/Linux)
#   set GOOGLE_API_KEY=your-key-here           (Windows)
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
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
    data = load_and_process_marks()
    ask_questions_about_data(data)