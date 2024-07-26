# # Write a Python program to remove duplicate characters of a given
#  string.
#  Input = “String and String Function”
#  Output: String and Function

def remove_duplicates_from_words(input_string):
    def remove_duplicates_from_word(word):
        seen = set()
        result = []
        for char in word:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)

    # Split the input string into words
    words = input_string.split()

    # Remove duplicates from each word
    processed_words = [remove_duplicates_from_word(word) for word in words]

    # Join the processed words back into a single string
    return ' '.join(processed_words)

# Given input string
input_string = "String and String Function"

# Remove duplicate characters from each word
output_string = remove_duplicates_from_words(input_string)

# Display the output string
print(f"Output: {output_string}")
