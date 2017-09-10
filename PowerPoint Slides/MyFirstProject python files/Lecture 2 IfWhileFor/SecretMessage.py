# Write a program that will take in a message and an input of 1 or 2
# and then encrypts (1) or decrypts (2) that message and prints out
# the result.

# ALGORITHM:
# 1) take in user input of message
# 2) take in user input of 1 or 2
# 3) if the number in #2 is 1, encrypt the message
# 4) if the number in #2 is 2, decrypt the message
# 5) otherwise, print the user has input an invalid option

message = input("What is your message?: ")
option = int(input("Please enter 1 for encryption or 2 for decryption: "))

if option == 1:

    # run encryption method and print result
    # init variable to hold new message with empty string
    encrypted_message = ""
    for char in message:
        # For each character in the message,
        # find its ASCII value , cast it to a string, and append it to
        # our encrypted message
        encrypted_message = encrypted_message + str(ord(char))
    # print result
    print(encrypted_message)



elif option == 2:
    # run decryption method and print result

    # init variable to hold new message with empty string
    decrypted_message = ""
    x = 0
    while x < len(message):
        current_secret_char = message[x]
        plain_char = ''

        if current_secret_char == "1":
            # The character's ascii is 3 digits long
            next_char = message[x + 1]
            last_char = message[x + 2]
            plain_char = chr(int(current_secret_char + next_char + last_char))
            decrypted_message += plain_char
            x += 3
        else:
            # The character's ascii is 2 digits long
            last_char = message[x + 1]
            plain_char = chr(int(current_secret_char + last_char))
            decrypted_message += plain_char
            x += 2

    print(decrypted_message)

else:
    print("Invalid option. Please try again.")