solution = 'hangman'
num_guesses = 0
guesses = []
correct = False
max_guesses = 10


def print_hang_man(solution, guesses):
    print_string = ''
    for l in solution:
        if l in guesses:
            print_string += ' ' + l + ' '
        else:
            print_string += ' _ '
    print('*************************************')
    print(print_string)
    print('*************************************')
    print()


def check_correct(solution, guesses):
    for l in solution:
        if l not in guesses:
            return False
    return True

def make_guess(solution, guesses):
    guess = input('Make a guess: ')

    unique_guess = guess not in guesses

    while not unique_guess:
        guess = input('You already guessed that. Your guesses are: ' + ' '.join(guesses) + '\nTake another guess: ')
        unique_guess = guess not in guesses

    if guess in solution:
        print('Great guess')
    else:
        print('Bad Guess')

    guesses.append(guess)
    return guesses


def get_num_guesses(solution, guesses, max_guesses):
    counter = 0
    for l in guesses:
        if l not in solution:
            counter += 1

    print(str(counter) + '/' + str(max_guesses), 'guesses taken')

    return counter



while not correct & (num_guesses < max_guesses):

    # overwrite the guesses list with an updated guess
    guesses = make_guess(solution, guesses)
    num_guesses = get_num_guesses(solution, guesses, max_guesses)

    print_hang_man(solution, guesses)

    correct = check_correct(solution, guesses)







if correct:
    print('*************************************')
    print('***********Amazing job***************')
    print('*************************************')
else:
    print ('Better luck next time X(')



# print_hang_man(solution, ['a'])
#
# print(check_correct(solution, []))
# print(check_correct(solution, ['a', 'h']))
# print(check_correct(solution, 'h a s n d g m'.split(' ')))
#
#
# guesses = ['a', 'b', 'c']
# guesses = make_guess(guesses)
# print (guesses)
#
# guesses = make_guess(guesses)
# print (guesses)
#
# guesses = make_guess(guesses)
# print (guesses)