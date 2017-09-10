# get the user's name as input
name = input("Please in put your name: ")

# Initialize x to 0
x = 0
# While x is less than however many characters are in the string stored in 'name'
while x < len(name):
    # print the number in x (will be 0, then 1, then 2...)
    print(x)
    # increment x (to avoid infinite while loop)
    x = x + 1

# done with while loop here, print done
print("Done")

