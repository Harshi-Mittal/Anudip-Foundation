def count_characters(input_string):
    letters = 0
    digits = 0
    symbols = 0

    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif not char.isspace():  # Count anything that is not a space as a symbol
            symbols += 1

    return letters, digits, symbols

# Given input string
input_string = "P@#yn26at^&i5ve"

# Count the characters
chars, digits, symbols = count_characters(input_string)

# Display the results
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")
