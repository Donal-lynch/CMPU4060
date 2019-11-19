print('\n ==================== Excercise 1 ==================== \n')
# Exercise 1: Write a Python program that opens a text file, # reads the contents line by line and saves it into
# a second file.
# Make sure you use try/except to handle and possible problems with incorrect filenames.

try:
    write_file = open('junk.txt', 'r')
    input_file = open('twinkle.txt', 'r')
except IOError:
    print('could not open files')
else:
    for line in input_file:
        try:
            write_file.write(line[:10])
        except IOError:
            print('do not have permission to write')
            break
        else:
            if line != '\n':  # Dont print a new line if the line is a blank line
                write_file.write('\n')

print('\n ==================== Excercise 2 ==================== \n')
# Exercise 2: Write a Python program that opens a text file, reads the contents line
# by line and prints each line in reverse.
with open('twinkle.txt', 'r') as input_file:
    for line in input_file:
        print(line[-1::-1].strip(), end='\n')

print('\n ==================== Excercise 3 ==================== \n')
# Exercise 3: Write a Python program that reads a text file and prints only the lines
# that start with 'When'.
with open('twinkle.txt', 'r') as input_file:
    for line in input_file:
        if line.split(sep = ' ')[0] == 'When':
            print(line, end='')

print('\n ==================== Excercise 4 ==================== \n')
# Exercise 4: Write a Python program that reads a text file and prints the length of each line.
with open('twinkle.txt', 'r') as input_file:
    for line in input_file:
        print(str(len(line)))
