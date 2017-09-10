# get the user's name
name = input("Please tell me your first name: ")

# Boolean expression in an if statement
# name == "Dane" tests to see if "Dane" is in the 'name' variable and
# returns a boolean (true/false)
if name == "Dane":
    # The code to run if the 'name' variable is Dane
    print("Awesome!")
elif name == "idk":
    # The code to run if the user doesn't know its name
    print("You don't know your own name?!")
else:
    # if name is neither "Dane" or "idk" then run this
    print("Name was neither Dane or idk")