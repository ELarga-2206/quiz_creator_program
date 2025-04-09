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

        except Exception as e:
            print("An error occurred:", e) #added for error catching, due to problems in line 7

main()

# now we have to worry about the consistency of the loop