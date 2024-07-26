# #Write a Python program to reverse words in a string
#  String = “Deeptech Python Training”

def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words back into a single string
    return ' '.join(reversed_words)

# Given input string
input_string = "Deeptech Python Training"

# Reverse the words in the string
reversed_string = reverse_words(input_string)

# Display the result
print(f"Reversed words: {reversed_string}")

# # Write a Python program to count and display the vowels of a given
#  text
#  String=”Welcome to python Training
def count_and_display_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = {v: 0 for v in vowels}  # Initialize a dictionary to keep track of each vowel's count

    for char in text:
        if char in vowels:
            vowel_count[char] += 1

    # Display the counts of each vowel
    for vowel, count in vowel_count.items():
        if count > 0:
            print(f"'{vowel}': {count}")

# Given input string
text = "Welcome to python Training"

# Count and display the vowels in the string
count_and_display_vowels(text)


# #Write a Python program to remove a newline in Python
#  String = "\nBest \nDeeptech \nPython \nTraining\n"
## Given input string
input_string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters
cleaned_string = input_string.replace('\n', '')

# Display the result
print(f"Cleaned String: '{cleaned_string}'")

# # Write a Python program to count the occurrences of each word in a
#  given sentence
#  string = “To change the overall look of your document. To change the look
#  available in the gallery”

from collections import Counter
import re

def count_word_occurrences(sentence):
    # Convert the sentence to lowercase to ensure case insensitivity
    sentence = sentence.lower()
    
    # Remove punctuation and split the sentence into words
    words = re.findall(r'\b\w+\b', sentence)
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    return word_counts

# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Count the occurrences of each word
word_counts = count_word_occurrences(sentence)

# Display the word counts
for word, count in word_counts.items():
    print(f"'{word}': {count}")
