def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Error: Division by zero is not allowed."
    return result

# Example call to the function
num1 = 10
num2 = 2

# Display the division result
print(f"The division of {num1} by {num2} is: {div(num1, num2)}")
def square(x):
    return x * x

# Example call to the function
num = 5

# Display the square of the number
print(f"The square of {num} is: {square(num)}")
import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Find the maximum and minimum
max_num = max(numbers)
min_num = min(numbers)

# Display the results
print(f"Random numbers: {numbers}")
print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")
# Accept a name from the user
name = input("Please enter your name: ")

# Convert the name to lowercase
lowercase_name = name.lower()

# Display the name in lowercase
print(f"Your name in lowercase is: {lowercase_name}")
