import tkinter as tk
from tkinter import messagebox 
import random 

def load_quiz(filename="quiz_questions.txt"):
        with open(filename, "r") as file:
                content = file.read().strip() 

        
        blocks = content.split("----------------------------------------")
        questions = [] 

        for block in blocks:
                lines = block.strip().split("\n") 
                if len(lines) < 6: 
                        continue

                try:
                        question_text = lines[0].replace("Question:", "").strip() 
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
        self.root = root 
        self.root.title("Quiz App")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f8ff") 

        self.questions = load_quiz() 
        random.shuffle(self.questions) # shuffle
        self.current = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=450, bg="#f0f8ff")
        self.question_label.pack(pady=20) 

        self.options = []
        for i in range(4):
            btn = tk.Button(root, text="", width=40, font=("Arial", 12), bg="#e6f2ff", command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5) 
            self.options.append(btn)

        self.feedback = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
        self.feedback.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", font=("Arial", 12), command=self.next_question, bg="#d1e7dd") 
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
                self.end_quiz() 

    def check_answer(self, selected_index):
        correct = self.questions[self.current]["answer"] 
        if chr(65 + selected_index) == correct: 
                self.score += 1    
                self.feedback.config(text="✅ Correct!", fg="green")
            # if false then its not correct
        else:   
                correct_index = ord(correct) - 65  
                correct_text = self.questions[self.current]["options"][correct_index] 
                self.feedback.config(text=f"❌ Incorrect! Correct: {correct}. {correct_text}", fg="red")
        for btn in self.options:   
                btn.config(state="disabled") 

    def next_question(self):
        self.current += 1  
        if self.current < len(self.questions): 
                for btn in self.options: 
                        btn.config(state="normal")
                self.display_question() 
        else:
                self.end_quiz()

    def end_quiz(self):
        for widget in self.root.winfo_children(): 
                widget.destroy()  
        final_score = f"You scored {self.score} out of {len(self.questions)}"         
        tk.Label(self.root, text="🎉 Quiz Complete!", font=("Arial", 20), bg="#f0f8ff").pack(pady=20)
        tk.Label(self.root, text=final_score, font=("Arial", 16), bg="#f0f8ff").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()