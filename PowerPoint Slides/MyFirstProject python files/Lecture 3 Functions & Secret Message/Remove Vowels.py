
# This is the function signature or definition
# define [function name](parameters the function uses)
def remove_vowels(my_string):
    # Initialize a new variable to hold the resulting
    # string after we have removed all vowels
    new_string = ""

    # For each character (stored in the variable 'char' here)
    # in my_string, if the character is NOT a vowel,
    # append it to the new_string
    for char in my_string:
        # here we use char.lower() to convert all characters
        # to lower case to compare them to our list of vowels
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            new_string += char

    # return the new_string value to whatever called this function
    return new_string


# Now we can take the user input and call our function on it
user_string = input("Please input a string (word, sentence): ")

string_without_vowels = remove_vowels(user_string)

print("Your string before was: ", user_string)
print("But now it is: ", string_without_vowels)