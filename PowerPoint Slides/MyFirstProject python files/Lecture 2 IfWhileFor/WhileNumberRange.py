# WHILE LOOP
# Write a function using a while loop that takes a number greater than 0 as input
# and prints each number from 0 to that number

# ALGORITHM:
# 1) get user input (ask for number greater than 0 )
# 2) initialize a variable that will count all the way up to the number from 0 (this is what we will print out in the loop)
# 3) loop through and print out each number from 0 to the number entered

# get input
num = int(input("Please input a number greater than zero: "))

# initialize counter variable
count = 0

# while count is less than num
while count <= num: # here we use less than or equal to <= because we want the loop to run all the way THROUGH the number stored in 'num'
    # print out the count
    print(count)
    # increment count to avoid infinite while loop
    count = count + 1