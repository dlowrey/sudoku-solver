# Calculate the area and circumference of a circle from its radius.
# Algorithm:
#   1) Prompt for a radius
#   2) Apply the circumference formula
#   3) Apply the area formula
#   4) print out the results


import math

# Get the radius from the user
radius_str = input("Enter the radius of your circle: ")
# Cast the radius_str into an integer (int)
radius_int = int(radius_str)

# apply the circumference formula 2 x pi x r
circumference = 2 * math.pi * radius_int
# apply the area formula pi x r^2
area = math.pi * (radius_int ** 2)

# print out the results
print("The circumference is:", circumference, "and the area is", area)






