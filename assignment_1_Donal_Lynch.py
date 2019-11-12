# Donal Lynch
# Marked Lab 22/10/19

# Question 1 ***************************************************

year_1 = int(input('Enter start year: '))
year_2 = int(input('Enter end year: '))

print ('Leap years in the period', year_1, 'to', year_2, 'are:')
no_leap_years = True

for i in range(year_1, year_2 + 1):
    if (i % 4 == 0) and (i % 100 != 0):
        print (i)
        no_leap_years = False

if no_leap_years:
    print ('There are no leap years in the range')



# Question 2 ***************************************************
user_num = input('Please enter a number: ')
accumulator = 0

# Loop over each digit in user_num as it is a string
for i in user_num:
    accumulator += int(i)**3

if accumulator == int(user_num):
    print(user_num, 'is narcissistic number')
else:
    print(user_num, 'is NOT narcissistic number')



# Question 3 ***************************************************
user_word = input('Welcome! Enter a word: ')
counter = 0

while user_word != '*':
    if user_word[0] == 'a':
        counter +=1
    user_word = input('Enter a word: ')

print('There were', counter, "words starting with an 'a'")


