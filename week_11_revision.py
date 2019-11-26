# Exercise 1:
# Write a Python function to read a sentence (text) and return a list of the 
# length of each word in the sentence.
# Use the function to read text from a file and calculate the length of each word in each
# line.

my_sen = 'There is anothing I love amore than pyhton'

def word_length(sentance):
    
    mylist = []

    for word in sentance.split(' '):

        length = len(word)

        mylist.append(length)

    return mylist        

twinkle = open('twinkle.txt', 'r')

for line in twinkle:
    print(word_length(line))
twinkle.close()



# Exercise 2:
# Write a Python function to read a sentence and reverse every word that 
# starts with ‘a’. 
# Use the function to read text from a file, reverse each word that start with ‘a’ and 
# save the result into another file.

def word_reverse(sentance):

    my_new_sen = ''
    
    for word in sentance.split(' '):
        if word[0].lower() == 'a':
            word_backwards = word.strip()[::-1] #need this to remove \n
            my_new_sen = my_new_sen + ' ' + word_backwards
        else:
            my_new_sen = my_new_sen + ' ' + word

    return my_new_sen.strip()


twinkle = open('twinkle.txt', 'r')
out_file = open('out_file.txt', 'w')

for line in twinkle:
    out_file.write(word_reverse(line) + '\n')
    
twinkle.close()
out_file.close()
    

# Exercise 3:
# Write a Python function replace_all(list, l_out, l_in) that takes three parameters:
# a list of numbers, a list of numbers to be replaced and a list of numbers to use as
# replacements.
# For example 
# replace_all([1,2,5,6,2,7,1,2], [2,4],[200,400]) will replace all 
# occurrences of 2 with 200 and all occurrences of 4 with 400 in the list 
# [1,2,5,6,2,7,1,2], so should return [1,200,5,6,200,7,1,200]

def replace_all(list_in, l_out, l_in):
    my_list = list_in.copy()

    for j in range(len(list_in)):
        for i in range(len(l_out)):
            if list_in[j] == l_out[i]:
                my_list[j] = l_in[i]
    return my_list

print(replace_all([1,2,5,6,2,7,4,2], [2,4],[200,400]))


# Exercise 4:
# Write a Python function to replace every third word in a sentence with “hello”. 
# Use the function to read a text from a file, replace every third word with ‘hello’
# and write the output in another file.


def hello_third_word(sentance):
    sentance_list = sentance.split(' ')

    for i in range(2, len(sentance_list), 3):
            sentance_list[i] = 'hello'

    return ' '.join(sentance_list)


# print(hello_third_word(my_sen))

twinkle = open('twinkle.txt', 'r')
out_file = open('out_file.txt', 'w')

for line in twinkle:
    out_file.write(hello_third_word(line) + '\n')
    
twinkle.close()
out_file.close()
    

# Exercise 5: Write a Python function to replace every word in a
# sentence which is longer than 6 characters with “blah”. 

def blah_word(sentance):
    sentance_list = sentance.split(' ')

    for i in range(len(sentance_list)):
       if len(sentance_list[i]) > 6:
           sentance_list[i] = 'blah'
        
    return ' '.join(sentance_list)
          
print(blah_word(my_sen))


# Exercise 6: Write a Python program that reads text from a file and generates
# a dictionary – a list of unique words. Save those words in a new file, one word per line.





