# FOR LOOP

# Write a function using a while loop that takes a number greater than 0 as input
# and prints each number from 0 to that number

# ALGORITHM:
# 1) get user input (ask for number greater than 0 )
# 2) initialize a variable that will count all the way up to the number from 0 (this is what we will print out in the loop)
# 3) loop through and print out each number from 0 to the number entered


# get user input number and cast it as integer
my_number = int(input("Please input a number greater than 0:"))

# intit count to 0
count = 0


# for each number in the range from count to my_number inclusive
for x in range(count, my_number +1):
    # print the number out
    print(x)
    # for loop will automatically increment x for us,
    # x will be 0, then 1, then 2, then 3... all the way to my_number + 1