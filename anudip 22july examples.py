file=open("anudip.txt",'r')
#*****//below commented code is for write data in file//*****
#file.write("welcome to python class")
#print("data inserted in the file")
file.seek(12)
data=file.read(5)
print(data)
print(file.tell())
file.close()

print("************************************************")
file=open("india.txt",'r')
#file.write("i love my india. india is a democratic country")
file.close()
#print("data inserted")
def count_word_occurrences(file_path,word):
    count = 0
    with open(r"C:\Users\DELL\AppData\Local\Programs\Python\Python38\india.txt", 'r') as file:
        for line in file:
            words = line.split()
            for w in words:
                if w.lower() == word.lower():
                    count += 1
    return count

file_path = 'India.txt'
word = 'india'
occurrences = count_word_occurrences(r"C:\Users\DELL\AppData\Local\Programs\Python\Python38\india.txt", word)
print(f"The word '{word}' occurs {occurrences} times in the file {file_path}.")
print("************************************************")

file=open("story.txt",'r')
#file.write("time is cruical today story is based on it")
#file.close()
def count_and_display_lines_starting_with_t(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('t'):
                count += 1
                print(line.strip())
    return count

file_path = 'story.txt'
count = count_and_display_lines_starting_with_t(file_path)
print(f"\nTotal lines starting with 't': {count}")
print("************************************************")

file=open("Myfile.txt",'r')
#file.write("hello how are you")
#file.close()
def count_vowels_and_consonants(file_path):
    vowels = 'AEIOUaeiou'
    vowel_count = 0
    consonant_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():  # Check if character is a letter
                    if char in vowels:
                        vowel_count += 1
                    else:
                        consonant_count += 1
                        
    return vowel_count, consonant_count

file_path = 'myfile.txt'
vowels, consonants = count_vowels_and_consonants(file_path)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
print("************************************************")

file=open("word.txt",'r')
#file.write("toffee coffee ")
#file.close()
def count_words_starting_with_t(file_path):
    count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.startswith('T') or word.startswith('t'):
                    count += 1
    
    return count

file_path = 'Word.txt'
t_word_count = count_words_starting_with_t(file_path)
print(f"Number of words starting with 'T': {t_word_count}")
print("************************************************")

file=open("Notes.txt",'r')
#file.write('hello how r you.\n')
#file.write('i am fine and you harshi.\n')
#file.close()
def count_lines_with_more_than_five_words(filename):
   count = 0
   with open(filename, 'r') as file:
        for line in file:
           words = line.split()
           word_count = len(words)
           if word_count > 5:
                count += 1
   return count
filename = 'word.txt'
lines_count = count_lines_with_more_than_five_words(filename)
print(f'Number of lines with more than five words: {lines_count}')

print("********************************************************************")
import struct

def write_student_data_to_binary_file(filename):
    # Open the binary file in write mode
    with open(filename, 'wb') as file:
        while True:
            # Get student details from the user
            roll_no = input("Enter student roll number: ")
            name = input("Enter student name: ")
            marks = input("Enter student marks: ")
            
            # Convert roll number and marks to integers, and name to a fixed length string
            try:
                roll_no = int(roll_no)
                marks = float(marks)
            except ValueError:
                print("Invalid input. Roll number and marks should be numbers.")
                continue
            
            # Format name to a fixed length of 30 characters (pad with spaces if necessary)
            name = name.ljust(30)[:30]
            
            # Pack data into a binary format
            packed_data = struct.pack('I30sf', roll_no, name.encode('utf-8'), marks)
            
            # Write packed data to file
            file.write(packed_data)
            
            # Ask the user if they want to enter more data
            more_data = input("Do you want to enter another student (yes/no)? ").strip().lower()
            if more_data != 'yes':
                break

# Specify the filename
filename = 'stu.dat'

# Call the function to write student data to the binary file
write_student_data_to_binary_file(filename)

print(f"Student data has been written to {filename}.")
print("********************************************************************")
import struct

def display_marks_of_students_above_threshold(filename, threshold):
    try:
        # Open the binary file in read mode
        with open(filename, 'rb') as file:
            while True:
                # Read a chunk of data from the file
                data = file.read(struct.calcsize('I30sf'))
                
                # If no more data is left, break the loop
                if not data:
                    break
                
                # Unpack the binary data
                roll_no, name, marks = struct.unpack('I30sf', data)
                
                # Check if marks are greater than the threshold
                if marks > threshold:
                    # Display student details
                    print(f"Roll Number: {roll_no}, Name: {name.decode('utf-8').strip()}, Marks: {marks}")
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the filename and threshold
filename = 'stu.dat'
threshold = 81

# Call the function to display marks
display_marks_of_students_above_threshold(filename, threshold)

