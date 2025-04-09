#so how do we ask the
	#question
	#the 4 choices
	# and its answer
	#for some reason it has to save itself to a text file 
	#ask for a new question (Y/N)

#for asking the questions → while loop

#while true:
	# user=input(“your question”)
	# ask for a key to stop the loop
	# say thanks for using the program
	# break

#The 4 questions:

	#print(“what choices do you want”)
	# Questions = input [ “A: B: C: D: ]
	#break

#The correct answer:
 	 #print (“what is the correct answer? A/B/C/D”)
	# we need to figure out a code that will check if the answer is correct*
	# also an error catcher in case the user inputs unknown letters

# still not sure about data to text file, we have to record every input and be able to access it in a txt file. need research for this  

# also about the tkinter library, still figuring out whether we can put music/sound effects, backgrounds, or any design/interactive
# buttons. 

def main():
    while True:
        user_input = input("enter your question: ")

        if user_input == "a":
            break
        
		try:
			print("enter 4 choices:")     
			choices = [ input("A: "), input("B: "), input("C: "), input("D: ")]
        
if __name__ == "__main__":
    main()


#next goal: is ask for the choices from A to D

# notice that when run, it keeps asking the same thing unless you press 'a'
# we have to sequentially shift to the next question after the user answers the 1st: ("whats your question")
# it has to shift to asking the choices immidiately