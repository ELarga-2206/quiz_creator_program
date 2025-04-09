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

            with open("quiz_questions.txt", "a", encoding="utf-8") as file:
                file.write(f"Question: {question}\n")
                file.write(f"A: {choices[0]}\n")
                file.write(f"B: {choices[1]}\n")
                file.write(f"C: {choices[2]}\n")
                file.write(f"D: {choices[3]}\n")
                file.write(f"Correct Answer: {correct_answer}\n")
                file.write("-" * 40 + "\n")
            print("Question saved successfully!")

        except Exception as e:
            print("An error occurred:", e) #added for error catching, due to problems in line 7
            
		 	

main()

# now we have to focus on asking whether if the user wants to create another question
# after asking the correct answer we have to break the loop and ask for permission first-
# before proceeding
# we really have to do this now
