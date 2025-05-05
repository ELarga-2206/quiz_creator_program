import tkinter as tk
from tkinter import messagebox 
import random 
import winsound
import time

#added theme
BACKGROUND_COLOR = "#fdf6f0"
QUESTION_FONT = ("Segoe UI", 16)
OPTION_FONT = ("Segoe UI", 12)
FEEDBACK_FONT = ("Segoe UI", 14)
BUTTON_BG = "#e0f7fa"
BUTTON_FG = "#333333"
BUTTON_ACTIVE_BG = "#b2ebf2"


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
        import time
        self.root = root 
        self.root.title("Quiz App")
        self.root.geometry("500x450") # increased to accomodaTe timer
        self.root.configure(bg="#f0f8ff") 
        self.root.configure(bg=BACKGROUND_COLOR)
        self.start_time = time.time()


        self.questions = load_quiz() 
        random.shuffle(self.questions) # shuffle
        self.current = 0
        self.score = 0

        self.timer_label = tk.Label(
            root, text="Time: 0:00", font=("Segoe UI", 12),
            bg=BACKGROUND_COLOR, fg=BUTTON_FG
        )
        self.timer_label.pack(pady=5)
        self.update_timer()  

        self.question_label = tk.Label(
                root, text="", font=QUESTION_FONT, wraplength=450,
                bg=BACKGROUND_COLOR, fg=BUTTON_FG
        )
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            btn = tk.Button(
                root, text="", width=40, font=OPTION_FONT,
                bg=BUTTON_BG, fg=BUTTON_FG, activebackground=BUTTON_ACTIVE_BG,
                command=lambda i=i: self.check_answer(i)
        )
            btn.pack(pady=5) 
            self.options.append(btn)

        self.feedback = tk.Label(
                root, text="", font=FEEDBACK_FONT, bg=BACKGROUND_COLOR, fg=BUTTON_FG
        )
        self.feedback.pack(pady=10)

        self.next_button = tk.Button(
                root, text="Next", font=OPTION_FONT, command=self.next_question,
                bg="#d1e7dd", fg=BUTTON_FG, activebackground="#bce5cb"
        )
        self.next_button.pack(pady=10)

        self.display_question()

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        self.timer_label.config(text=f"Time: {minutes}:{seconds:02d}")
        # Update every second
        self.root.after(1000, self.update_timer)


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
                winsound.PlaySound(r"C:\Users\jenny larga\OneDrive\Documents\quiz_reader\correct.wav", winsound.SND_FILENAME)
            # if false then its not correct
        else:   
                correct_index = ord(correct) - 65  
                correct_text = self.questions[self.current]["options"][correct_index] 
                self.feedback.config(text=f"❌ Incorrect! Correct: {correct}. {correct_text}", fg="red")
                winsound.PlaySound(r"C:\Users\jenny larga\OneDrive\Documents\quiz_reader\wrong.wav", winsound.SND_FILENAME)
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

        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_taken = f"{minutes}:{seconds:02d}"

        final_score = f"You scored {self.score} out of {len(self.questions)}"  
        time_message = f"Time taken: {time_taken}"       
        
        self.root.configure(bg=BACKGROUND_COLOR)
        tk.Label(self.root, text="🎉 Quiz Complete!", font=("Segoe UI", 20), bg=BACKGROUND_COLOR, fg=BUTTON_FG).pack(pady=20)
        tk.Label(self.root, text=final_score, font=QUESTION_FONT, bg=BACKGROUND_COLOR, fg=BUTTON_FG).pack(pady=10)
        tk.Label(self.root, text=time_message, font=QUESTION_FONT, bg=BACKGROUND_COLOR, fg=BUTTON_FG).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()