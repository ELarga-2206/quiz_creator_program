# what we need to know so far is:

# how to program a file reader
# convert it to a quiz
# use GUI for creativity


# Part 1 of creating a pseudocode, it must match with our program requirement

        # file reader (we'll use read.file)
       
#so:
        # def load quiz (file = quiz_questions.txt)
            # open the file "r"
                # then file.read

# since our txt file follows a specific format, the code must be able to read it

        # so program it in such a way:
            # each line cutouts = blocks, 1 block = 1 question
            # on our text file it must strip the word "question" and the ABCD aswell
            # we somehow have to extract the text
            # and store it so we can use it later

# so:
        # use for loop
        # convert the borders in the txt file into 'blocks'
        # strip unecessary spaces to get the pure words only
        # append to a list
        # then we can call that list whenever

# part 3 of the pseudocode, we'll focus on the tkinter on this one

        # on using tkinter we need to setup the:
            # window size
            # buttons
            # fonts 
        
        # how do we display the questions again?
            # we need to display the question

        # after that, we need to create the ff function:

        # function for checking the answer
        # function for next question button
        # function for calculation of correct answer and total score

# add ons will follow once we get the program working

           

