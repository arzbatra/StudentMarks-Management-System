# Marks Management System

This is a small project I built to manage student marks - started off as a basic script to enter marks and save them to a CSV, then kept adding stuff to it as I learned more (pandas, matplotlib, and eventually hooked it up to Gemini so you can just ask questions about the data instead of digging through the CSV yourself).

## What it does

- Takes in subjects and student marks (with roll numbers) and saves everything to `students.csv`
- Calculates average marks per student and gives a remark (Excellent / Good / Needs Improvement etc.)
- Plots bar charts - one comparing all students, one for a single student's marks across subjects
- Lets you ask questions about the data in plain English using Gemini (e.g. "who scored highest in maths")

## Files

- `collect_marks.py` - entering marks
- `analyze_marks.py` - averages + charts
- `ask_questions.py` - the AI part
- `main.py` - runs everything in order

## Running it

```
pip install -r requirements.txt
python main.py
```

You'll need a Gemini API key for the AI question part - get one free at https://aistudio.google.com/apikey, it'll just ask you for it when you run that part.

## Notes to self / known limitations

- No way to edit a student's marks once entered, you'd have to redo the whole CSV
- Only handles one class/CSV at a time right now
- The web version doesn't save anywhere except your own browser (localStorage), so don't expect it to sync across devices

## Why I made this

Wanted something more useful than a plain calculator-type script, and it turned into a good excuse to actually use pandas/numpy for something real instead of just tutorial exercises. Still adding to it when I get ideas.
