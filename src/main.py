import json
import random
import tkinter as tk
from tkinter import messagebox

# Load questions from JSON file
def load_questions(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Questions file not found.")
        return []
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error reading questions file.")
        return []

# Initialize application
def start_quiz():
    # Load questions from the resources folder
    maths_questions = load_questions("resources/maths_questions.json")
    english_questions = load_questions("resources/english_questions.json")

    if not maths_questions or not english_questions:
        return  # Exit if no questions are loaded

    all_questions = maths_questions + english_questions

    # Variables to track current question and score
    current_question = random.choice(all_questions)
    score = 0

    # Function to update the question
    def next_question():
        nonlocal current_question
        current_question = random.choice(all_questions)
        question_label.config(text=current_question['question'])
        answer_entry.delete(0, tk.END)

    # Function to check the answer
    def check_answer():
        nonlocal score
        user_answer = answer_entry.get().strip()
        correct_answer = current_question['answer']
        
        if user_answer.lower() == correct_answer.lower():
            score += 1
            feedback_label.config(text=f"Correct! Your score: {score}", fg="green")
        else:
            feedback_label.config(text=f"Wrong! The correct answer was: {correct_answer}", fg="red")

        next_question()

    # Create the main application window
    root = tk.Tk()
    root.title("Quiz Game")
    root.geometry("400x300")

    # GUI Elements
    question_label = tk.Label(root, text=current_question['question'], wraplength=350, font=("Arial", 14))
    question_label.pack(pady=20)

    answer_entry = tk.Entry(root, font=("Arial", 14))
    answer_entry.pack(pady=10)

    submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Arial", 12))
    submit_button.pack(pady=10)

    feedback_label = tk.Label(root, text="", font=("Arial", 12))
    feedback_label.pack(pady=10)

    # Start the application
    root.mainloop()

if __name__ == "__main__":
    start_quiz()
