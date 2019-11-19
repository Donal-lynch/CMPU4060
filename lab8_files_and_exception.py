'''
input_file = open('twinkle.txt', 'r')

for line in input_file:
    print(line)

input_file.close()


#example from note pg 19
out_file = open('numbers.txt', 'w')

for i in range(10):
    out_file.write(str(i))
    out_file.write('\n')
out_file.close()




while True:
    num = input('enter a number: ')

    try:
        int_num = int(num)
        print('your number is', str(int_num))
    except ValueError:
        print('that aint no number')
'''

print('\n ==================== Excercise 1 ==================== \n')
# Exercise 1: Write a Python program that opens a text file, # reads the contents line by line and saves it into
# a second file.
# Make sure you use try/except to handle and possible problems with incorrect filenames.
with open('junk.txt', 'r') as write_file:
    with open('twinkle.txt', 'r') as input_file:
        for line in input_file:
            try:
                write_file.write(line[:10])
            except IOError:
                print('major file error')
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
        print(len(line))