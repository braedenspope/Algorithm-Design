# 1. Name: 
#    Braeden Pope
# 2. Assignment Name: 
#    Lab 02: Authentication Program
# 3. Assignment Description:
#    Reads a file of usernames and passwords, prompts users for a username and password,
#    and then checks if those match in the system.
# 4. What was the hardest part? Be as specific as possible.
#    Getting a hang of what the JSON functions do was tricky, just trying to understand 
#    what they make so I can use them took a bit of time. 
# 5. How long did it take for you to complete the assignment?
#    2 hours

# Initialized check variable for if the file isn't found, or if the user's username isn't in the system.
check = True

# Checks that the Lab02.json file exists, returns an error if not found.
import json
try:
    data = open("Lab02.json", "r")
    text = data.read()
except FileNotFoundError:
    print("Unable to open file Lab02.json.")
    check = False

# Checks that the file was found.
if (check):

# Converts string into a JSON object, then into two lists, one for usernames and one for passwords
    list = json.loads(text)
    usernames = list["username"]
    passwords = list["password"]

# Prompts user for username and password and records them.
    user_name = input("Username: ")
    pass_word  = input("Password: ")

# Finds the location of the given username in the list, and rejects it if it isn't there.
    try:
        index = usernames.index(user_name)
    except ValueError:
        print("You are not authorized to use the system.")
        check = False

# Checks if the password matches the username in the list, then tells the user if they're authenticated or not.
    if (check):
        if (pass_word == passwords[index]):
            print("You are authenticated!")
        else:
            print("You are not authorized to use the system.")
