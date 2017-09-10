# get user's name
name = input("Please input your name: ")

# Loop through each character in the string stored in 'name'
# IN ENGLISH: "For each character in the word stored in the variable 'name' ":
for character in name:
    # Print that character
    print(character)


# NOTE: 'character' is a variable in the for loop that the for loop
#       automatically takes care of. The for loops assigns each character in the string
#       stored in 'name' to the variable 'character' i.e if name = "DANE" the for loop
#       would assign character = "D", then character = "A", then character = "N", then
#       character = "E", and then the for loop would exit because that was each character in
#       the word "Dane"

