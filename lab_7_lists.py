# Exercise 1: Write a Python function to sum all numbers in a list
print ('*************excercise 1 *******************\n')

def list_sum(my_list):
    counter = 0

    for i in my_list:
        counter += i
    return counter

my_list = [1, 2, 3, 4, 5, 7, 6]
print(list_sum(my_list))

print ('\n*************excercise 2 *******************\n')

# Exercise 2: Write a Python function to get the largest number from a list.
def list_max(my_list):
    max_element = my_list[0]

    for i in my_list:
        if i > max_element:
            max_element = i

    return max_element

print(list_max(my_list))

print ('\n*************excercise 3 *******************\n')
# Exercise 3  Write a Python function that takes a list of words and counts how many
# of them begin with ‘a’

def a_counter(word_list):
    counter = 0
    for word in word_list:
        if word[0] == 'a':
            counter += 1
    return counter

# make a word list. NOTE split at the end converts string to list
word_list = 'Lorem ipsum dolor sit amet aonsectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'.split(' ')
print(a_counter(word_list), 'words starting with "a"')


print ('\n*************excercise 4 *******************\n')
# Exercise 4: (modify Ex3)
# Write a Python function that takes a list of words and a character, and counts how
# many of the words in the list begin with that character.


def letter_counter(word_list, letter):
    counter = 0
    for word in word_list:
        if word[0] == letter:
            counter += 1
    return counter


first_letter = input('enter a first letter: ')
print(letter_counter(word_list, first_letter), 'words starting with', first_letter)


print ('\n*************excercise 5 *******************\n')

# Exercise 5:
# Write a Python function that takes a list of numbers and returns a
# new list containing only the even numbers from the first list

def even_checker(my_list):
    new_list = []

    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
print(even_checker(my_list))
