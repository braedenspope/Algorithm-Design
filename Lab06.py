# 1. Name:
#      Braeden Pope
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Prompts the user for a file and a word to search for, searches for the word in the list, 
#      and tells the user if it exists in the file.
# 4. Algorithmic Efficiency
#      This program has the efficency of O(log n), as the values get progressively closer together
#      as it iterates through the program, speeding up the process.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how to handle an empty list, but I realized I could resolve
#      it with an if statement.
# 6. How long did it take for you to complete the assignment?
#      1 hour

# Initialized check variable for if the file isn't found, or if the user's username isn't in the system.
check = True

# Checks that the Lab02.json file exists, returns an error if not found.
import json
filename = input("What is the name of the file? ")
try:
    data = open(filename, "r")
    text = data.read()
except FileNotFoundError:
    print("Unable to open file", filename)
    check = False

# Checks that the file was found.
if (check):
    # Creates the dictionary, and then the list the program will be checking.
    list = json.loads(text)
    names_list = list["array"]

    # Initilaizes variables that the program will you to perform an advanced search.
    first = 0
    last = len(names_list)
    found = False

    # Prompts the user for a word to search for. 
    name = input("What name are we looking for? ")

    # Checks the list isn't empty
    if (first != last):


        while (first <= last and not found):
        
            # Variable for which spot to check
            index = int((first + last) / 2)

            # Increases front variable if the word would be higher
            if (names_list[index] < name):
                first = index + 1
            # Decreases back variable if the word would be lower
            elif (names_list[index] > name):
                last = index - 1

            # The word has been found!
            else:
                found = True

    # Displays if the word was found in the file
    if (found):
        print("We found", name, "in", filename)
    else:
        print("We did not find", name, "in file", filename)

    
