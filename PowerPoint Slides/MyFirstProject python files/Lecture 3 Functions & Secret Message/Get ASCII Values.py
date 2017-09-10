

# Get the ascii value of 'a' and print
a_ascii = ord("a")
print("The ASCII value of 'a' is: ", a_ascii)

# Get the ascii value of 'A' and print
A_ascii = ord("A")
print("The ASCII value of 'A' is: ", A_ascii)

# Get the ascii values for each character in my name
my_name = "Dane"
for one_character in my_name:
    # Get the ascii value
    ascii_value = ord(one_character)
    # print it
    print("The character", one_character, "in ASCII is", ascii_value)

# REMEMBER
# ord() returns an integer not a string, if you need to convert
# it to a string you need to use the cast function str()