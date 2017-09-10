
def encrypt(user_message):
    # encryption algorithm goes here
    encrypted_str = ""

    # For each character in the user's message
    for one_character in user_message:
        # Get the ascii value
        ascii_value = ord(one_character)
        # Cast to string so we can append it to a string
        ascii_value_str = str(ascii_value)
        # Append it to our encrypted_str
        encrypted_str += ascii_value_str

    # return the result
    return encrypted_str






def decrypt(user_message_encrypted):
    # decryption algorithm goes here
    decrypted_str = ""
    str_index = 0

    while str_index < len(user_message_encrypted):

        # Get the current character in the message
        current_ascii_char = user_message_encrypted[str_index]

        if current_ascii_char == "1":
            # The ASCII value is 3 digits long, get
            # the next two digits
            second_digit = user_message_encrypted[str_index + 1]
            third_digit = user_message_encrypted[str_index + 2]

            # Concatenate them with the current ascii character
            ascii_value_str = current_ascii_char + second_digit + third_digit

            # get the numerical version of the ascii value
            ascii_val_int = int(ascii_value_str)

            # find the character value of the Ascii value using casting
            current_char = chr(ascii_val_int)

            # increment our index to avoid infinite loop
            str_index += 3
        else:
            # The ASCII value is 2 digits long, get
            # the next digit
            second_digit = user_message_encrypted[str_index + 1]

            # Concatenate the second digit with the current ascii character
            ascii_value_str = current_ascii_char + second_digit

            # find the numerical version of the ascii value using casting
            ascii_val_int = int(ascii_value_str)

            # find the character value of the ASCII value using casting
            current_char = chr(ascii_val_int)

            # increment index to avoid infinite loop
            str_index += 2

        # append to our decrypted string
        decrypted_str += current_char

    # after while loop is done
    # return resulting string
    return decrypted_str




##########################################################################################################################
#
#
# End of function code; Beginning of application code
#
#
##########################################################################################################################

#  get message as input from user
user_message = input("What is your message?: ")

# get user's option (1 = encrypt, 2 = decrypt)
user_option = input("Would you like to (1) encrypt or (2) decrypt?: ")


new_message = ""
if user_option == "1":
    new_message = encrypt(user_message)
elif user_option == "2":
    new_message = decrypt(user_message)
else:
    new_message = "Invalid option " + user_option + " selected. Please try again."

# print out the resulting message
print(new_message)