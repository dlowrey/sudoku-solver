# A program that takes in a temperature in Fahrenheit and converts it to celsius
# Algorithm:
#   1) prompt for input
#   2) convert input using F to C formula
#   3) print out results

# Prompt the user for input
# cast the return value of the input() function to an int
# store in variable
temp_f_int = int(input("What is the temperature in fahrenheit?: "))

# convert fahrenheit to celsius
temp_c_int = (temp_f_int - 32) / 9

#print the results
print(temp_f_int, "in Celsius is", temp_c_int)

# Do ALL the stuff
print("The temperature in Celsius is:",(int(input("What is the temperature in fahrenheit?: ")) - 32) / 9)