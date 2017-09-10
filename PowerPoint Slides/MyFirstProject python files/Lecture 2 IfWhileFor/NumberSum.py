# Write a program that will add the numbers 1 - 100 and print out the sum

# Algorithm:
# 1) initialize a variable to keep track of the sum to 0
# 2) in a loop (for or while), loop through all the numbers 1 - 100 and add them each time to the varaible keeping track of the sum
# 3) print out the result
# 4) profit


# WITH THE FOR LOOP

# initialize our sum
the_sum = 0
# The range function is exclusive, so if we were to say
# range(1,100) instead, it would only sum up the numbers 1-99 (not including 100)
for number in range(1,101):
    # Add this number to the sum
    the_sum = the_sum + number
# print result (after for loop is done)
print("The sum of all the numbers (using for loop) in the range 1-100 is:", the_sum)


# --------------------------Same program with a while loop below---------------------------------------------------------------------------------------------


# WITH A WHILE LOOP
# initialize a variable to keep track of the sum
my_sum = 0

# initialize a counter varible to count how many times our loop has run
loop_counter = 0

while loop_counter <= 100:
    # add the number to our sum
    my_sum = my_sum + loop_counter
    # increment our counter variable to avoid infinite loop
    loop_counter = loop_counter + 1

# print the result after loop is done
print("The sum of all the numbers (using while loop) in the range 1-100 is:", my_sum)
