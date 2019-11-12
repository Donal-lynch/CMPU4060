# Exercise 1: Write a Python function to sum all numbers in a list
my_list = [1, 2, 3, 4, 5, 7, 6]

counter = 0

for el in my_list:
    counter += el

print(counter)


# Exercise 2: Write a Python function to get the largest number from a list.
print(max(my_list))


# Exercise 3  Write a Python function that takes a list of words and counts how many
# of them begin with ‘a’
my_list = 'Lorem ipsum dolor sit amet aonsectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'.split(' ')

counter = 0
for word in my_list:
    if word[0].lower() == 'a':
        counter += 1
print(counter, 'words starting with "a"')



# Exercise 4: (modify Ex3)
# Write a Python function that takes a list of words and a character, and counts how
# many of the words in the list begin with that character.

my_list = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore' \
          ' magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat' \
          ' Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore' \
          ' eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum'.split(' ')

first_letter = input('enter a first letter: ')

counter = 0
for word in my_list:
    if word[0].lower() == first_letter.lower():
        counter += 1
print(counter, 'words starting with', first_letter.lower())





# Exercise 5:
# Write a Python function that takes a list of numbers and returns a
# new list containing only the even numbers from the first list

my_list = [1, 2, 3, 4, 5, 7, 6]
new_list = []

for i in my_list:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)


