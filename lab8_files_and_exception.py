'''
input_file = open('twinkle.txt', 'r')

for line in input_file:
    print(line)

input_file.close()
'''

with open('twinkle.txt', 'r') as input_file:
    for line in input_file:
        print(line, end='')