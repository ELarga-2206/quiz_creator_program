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