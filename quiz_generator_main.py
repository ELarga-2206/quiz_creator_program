def main():
    while True:
        question = input("Enter your question (type 'a' to stop): ") 

        if question.lower == "a": 
            break

        try:
            print("Enter 4 choices:")
            choices = [
                input("A: ").strip(),
                input("B: ").strip(),
                input("C: ").strip(),
                input("D: ").strip()
            ]
            
            while True: 
                correct_answer = input("Enter the correct answer (A/B/C/D): ").upper().strip()
                if correct_answer in ['A', 'B', 'C', 'D']:
                        break 
                        print("Invalid! Please enter A, B, C, or D only.")

            with open("quiz_questions.txt", "a", encoding="utf-8") as file:
                file.write(f"Question: {question}\n")
                file.write(f"A: {choices[0]}\n")
                file.write(f"B: {choices[1]}\n")
                file.write(f"C: {choices[2]}\n")
                file.write(f"D: {choices[3]}\n")
                file.write(f"Correct Answer: {correct_answer}\n")
                file.write("-" * 40 + "\n")
            print("Question saved successfully!")

            while True:
                cont = input("\nAdd another question? (Y/N): ") 
                if cont in ['Y', 'N']:
                    break
                print("Please enter Y or N.")

            if cont == 'N':
                print("\nQuiz creation complete. Questions saved to 'quiz_questions.txt'")
                break

        except Exception as e:
            print(f"\nAn error occurred: {e}\nPlease try again.")
            
		 	
if __name__ == "__main__":
    main()

