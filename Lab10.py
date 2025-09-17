# 1. Name:
#      Braeden Pope
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      Prompts the user for a number, and discovers and displays the francois number of that index.
# 4. What was the hardest part? Be as specific as possible.
#      figuring out good asserts, with the program being so small it was a bit harder
#      to think of more asserts
# 5. How long did it take for you to complete the assignment?
#      Hour and a half

# Initializes the francois list and loop variable.
francois = [2, 1]
test = True
# Loops if the user gives a number less than 1.
while (test):

    # Prompts the user for a Francois number to calculate.
    number = int(input("Which Francois number would you like to see? "))
    if (number > 0):
        #Calculates the Francois numbers up to the given number.
        for index in range(2, number):
            francois.append(francois[index - 1] + francois[index - 2])

        assert len(francois) >= number, "wrong number of iterations"
        for num in francois:
            assert type(num) == int, "wrong type"

        # Displays the requested Francois number.
        print(f"Francois number {number} is {francois[number - 1]}.")
        test = False
    else:
        print("Not a valid number, please try again.")