import random

def letter_jumble(word):
    # this function take a sinlge word and randomly swaps two of the middle letters
    
   
    # If a word ends with a comma we do not want to treat that as athe last letter
    # If there is a comma, remove it but also make a flag so that the comma can
    # put it back on at the end
    if word[-1] == ',':
        comma_flag = True
        word = word[:-1] #remove the last character
    else:
         comma_flag = False

    # cannot jumble 1, 2 or 4 letter words
    if len(word) < 4:
        jumbled_word = word
    else:     
        # take out the middle letters and convert to a list
        # Have have to convert to list as strings 'immutable'
        middle_letters = list(word[1:-1])

        # Make two random numbers
        i = random.randint(0, len(middle_letters)-1)
        j = random.randint(0, len(middle_letters)-1)

        # pull out the letters that we want to swap
        middle_letter_i =  middle_letters[i]
        middle_letter_j =  middle_letters[j]

        # do the swap
        middle_letters[i] = middle_letter_j
        middle_letters[j] = middle_letter_i

        # convert list the list letters back to a whole word
        # and reattach the first and last characters

        jumbled_word = word[0] #start with the first letter

        # add on the jumbled letters
        for i in middle_letters:
            jumbled_word += i

        jumbled_word += word[-1]# add on the last letter

        # replace the comma if necessary
        if comma_flag:
            jumbled_word += ','

    return jumbled_word


def word_jumble(word):
    # this function takes a word and repeatedly swaps 2 of the letters

    for i in range(20):
        word = letter_jumble(word)
    return(word)

# Read a file and print the jumbled letters to screen
try:
    file_obj = open('C://Users/lynchdo/Desktop/twinkle.txt', 'r')

    for line in file_obj:
        line_jumbled = ''
        for word in line.split():
            word_jumbled = word_jumble(word)
            line_jumbled = line_jumbled + word_jumbled + ' '
        print(line_jumbled)
    
except IOError:
    print('file does not exist')
else:
    file_obj.close()
    print('\nfile closed successfully')



    
