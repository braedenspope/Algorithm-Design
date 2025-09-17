# 1. Name:
#      Braeden Pope
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      Prompts the user for a file name, reads the file into a list, sorts the list from smallest to largest,
#      then displays the now sorted list to the user.
# 4. What was the hardest part? Be as specific as possible.
#      I had the wrong type of sort originally, so I had to make some edits to my original design to make it
#      meet the requirements. Figuring out what asserts to add as well was difficult
# 5. How long did it take for you to complete the assignment?
#      2 hours

# Initialized check variable for if the file isn't found, or if the user's username isn't in the system.
check = True

# Checks that the Lab02.json file exists, returns an error if not found.
from array import array
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

    # Creates list from JSON file.
    sort_list = json.loads(text)
    list = sort_list["array"]
    
    assert type(list) != array, "not a list"

    i_pivot = len(list) - 1
    
    assert type(i_pivot) == int, "not an integer"
    assert len(list) >= 0, "negative list length???"

    while i_pivot >= 0:
        # (Re)sets the i_largest value.
        i_largest = 0
        
        for i_check in range(i_pivot):
            
            assert 0 <= i_check <= i_pivot, "i_check out of range"

            # Finds the index with the largest value.
            if (list[i_check] > list[i_largest]):
                i_largest = i_check

        # Swaps the i_pivot value and the i_largest value if i_largest is bigger.
        if (list[i_largest] > list[i_pivot]):
            list[i_pivot], list[i_largest] = list[i_largest], list[i_pivot]
        # Increments to the next index to sort to.
        i_pivot -= 1

    # Prints out the sorted values of the file.
    print("The values in", filename, "are:")
    for index in range(len(list)):
        print("\t", list[index])

