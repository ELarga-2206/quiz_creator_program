# file reader (we'll use read.file)
       
#so:
        # def load quiz (file = quiz_questions.txt)
            # open the file "r"
                # then file.read

# use for loop
        # convert the borders in the txt file into 'blocks'
        # strip unecessary spaces to get the pure words only
        # append to a list
        # then we can call that list whenever


import tkinter as tk
from tkinter import messagebox # for info display
import random 

def load_quiz(filename="quiz_questions.txt"):
        with open(filename, "r") as file:
                content = file.read().strip() # strip the spaces

        # we'll split: 1 block = 1 question
        blocks = content.split("----------------------------------------")
        questions = [] # store it here

        for block in blocks:
                lines = block.strip().split("\n") # remove extra empty space at the very beginning and end
                if len(lines) < 6: # If the "slice" has fewer than 6 lines, skip
                        continue

                try:
                        question_text = lines[0].replace("Question:", "").strip() # we remove the word 'question' and .strip to remove trailing spaces
                        option_a = lines[1].replace("A:", "").strip()
                        option_b = lines[2].replace("B:", "").strip()
                        option_c = lines[3].replace("C:", "").strip()
                        option_d = lines[4].replace("D:", "").strip()
                        correct = lines[5].replace("Correct Answer:", "").strip().upper() 

                        questions.append({
                        "question": question_text,
                        "options": [option_a, option_b, option_c, option_d],
                        "answer": correct 
                        })

                except Exception as e:
                        print(f"Error indentifying block:\n{block}\nError: {e}")
                        continue

        return questions

class QuizApp:
    def __init__(self, root):
        self.root = root # to interact with and manage the main window (root).
        self.root.title("Quiz App")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f8ff") # this is light blue

        # were gonna call load_quiz now, to make quiz data available to the QuizApp func
        self.questions = load_quiz() 
        random.shuffle(self.questions) # shuffle
        # for the index of the question that the user is currently on:
        self.current = 0
        # store the user's score as they answer the questions
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=450, bg="#f0f8ff")
        self.question_label.pack(pady=20) # part of the app class, so it can be updated later

        self.options = []
        for i in range(4):
            btn = tk.Button(root, text="", width=40, font=("Arial", 12), bg="#e6f2ff", command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5) 
            self.options.append(btn)

        self.feedback = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
        self.feedback.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", font=("Arial", 12), command=self.next_question, bg="#d1e7dd") # must have troubleshooting
        self.next_button.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current < len(self.questions):
                q = self.questions[self.current]
                self.question_label.config(text=f"Q{self.current + 1}: {q['question']}")
                for i, option in enumerate(q["options"]):
                        self.options[i].config(text=f"{chr(65+i)}. {option}")
                self.feedback.config(text="")
        else:
                self.end_quiz() # wrong alignment

    def check_answer(self, selected_index):
        correct = self.questions[self.current]["answer"] # to get question data for the current question.
        if chr(65 + selected_index) == correct: # 65 since its ASCII for A (calculates the ASCII code of the correct letter)
                self.score += 1    # checks if the user's choice matches the correct answer, automatically adds 1
                self.feedback.config(text="✅ Correct!", fg="green")
            # if false then its not correct
        else:   
                correct_index = ord(correct) - 65  # We subtract 65 because the ASCII value of "A" is 65
                correct_text = self.questions[self.current]["options"][correct_index] # Gets the question data, lists of choices, and correct ans
                self.feedback.config(text=f"❌ Incorrect! Correct: {correct}. {correct_text}", fg="red")
        for btn in self.options:   # loop through each button in the self.options list
                btn.config(state="disabled") #  disables all the answer option buttons

    def next_question(self):
        self.current += 1  # index of the question being displayed
        if self.current < len(self.questions): # checks if there are more questions to show.
                for btn in self.options: # loop goes through each button in the selfoptions list 
                        btn.config(state="normal")
                self.display_question() # show the next question and its answer options
        else:
                self.end_quiz()

    def end_quiz(self):
        for widget in self.root.winfo_children(): ## method returns a list of all the widgets (labels, buttons, etc)
                widget.destroy()  # remove the widget from the window and destroy it
        final_score = f"You scored {self.score} out of {len(self.questions)}"         # display users score
        tk.Label(self.root, text="🎉 Quiz Complete!", font=("Arial", 20), bg="#f0f8ff").pack(pady=20) # Displays a large CONGRATULATIONS
        tk.Label(self.root, text=final_score, font=("Arial", 16), bg="#f0f8ff").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()