def main():
    while True:
        user_input = input("Enter your question: ")

        if user_input == "a":
            break

        try:
            print("Enter 4 choices:")
            choices = [
                input("A: "),
                input("B: "),
                input("C: "),
                input("D: ")
            ]
            
             
            correct_answer = input("Enter the correct answer (A/B/C/D): ")
            if correct_answer in ['A', 'B', 'C', 'D']:
                    break # added a stopper here, so we can manually start the loop again via (Y/N)
                    print("Please enter A, B, C, or D only.")

            file.write(f"Q: {user_input}\n")
            for i, opt in enumerate(choices):
                    file.write(f"{chr(65 + i)}) {opt}\n")
                file.write(f"Correct: {correct}\n\n")

        except Exception as e:
            print("An error occurred:", e) #added for error catching, due to problems in line 7
            
		 	

main()

# now we have to focus on asking whether if the user wants to create another question
# after asking the correct answer we have to break the loop and ask for permission first-
# before proceeding
