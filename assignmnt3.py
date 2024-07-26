# Given input string
input_string = "Welcome to Python Assignment"

# Define the vowels
vowels = "aeiouAEIOU"

# Initialize the vowel count
vowel_count = 0

# Iterate through each character in the string
for char in input_string:
    if char in vowels:
        vowel_count += 1

# Display the count of vowels
print(f"Total vowels are: {vowel_count}")
