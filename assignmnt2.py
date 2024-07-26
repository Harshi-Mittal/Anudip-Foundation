# Given input string
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Initialize counters
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
special_count = 0

# Iterate through each character in the string
for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        numeric_count += 1
    elif not char.isspace():  # consider anything that is not a space, digit, or letter as special
        special_count += 1

# Display the counts
print(f"UpperCase : {uppercase_count}")
print(f"LowerCase : {lowercase_count}")
print(f"NumberCase : {numeric_count}")
print(f"SpecialCase : {special_count}")
