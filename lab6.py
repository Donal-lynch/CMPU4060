# Exercise 1: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def counter(num):
    for i in range(1, num+1):
        print (i, end = ' ')
    print()

counter(5)
print('*--------------------*')

# Exercise 2: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def even_checker(num):
    
    # Output wants a comma between each print out, but not at end
    end = ', '

    for i in range(num+1):
        if i % 2 == 0:
            print(i, 'is even', end = end)
        else:
             print(i, 'is odd', end = end)

        if i == num-1:
            end = '.'
    print()

even_checker(4)
print('*--------------------*')

# Exercise 3: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def times_tables(num):
    for i in range(num+1):
        print(i, '* 9 =', i*9)
    print()

times_tables(12)
print('*--------------------*')

# Exercise 4: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_up(num):
    i = 0
    for j in range(1, num+1):
        i += j
    print (i)


add_up(6)
print (1 + 2 + 3 + 4 + 5 + 6)

print('*--------------------*')
# Exercise 5: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def factorial(num):
    i = 1
    for j in range(2, num+1):
        i*= j
    print(i)
    
factorial(5)
print(5*4*3*2)
print('*--------------------*')

# Exercise 6: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def head_and_tail(string):
    if len(string) < 4:
        print('string should have 4 or more characters')
    else:
        return string[:2] + string[-2:]

print(head_and_tail('hello there'))
print('*--------------------*')

# Exercise 7: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       
def odd_out(string):
    return string[1:len(string):2]

print(odd_out('1a2a3a4a5a6a7a8a9b'))
print('*--------------------*')

# Exercise 8: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def string_first_half(string):
    return (string[0:int(len(string)/2)])

print(string_first_half('Python'))
print('*--------------------*')

# Exercise 9: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def insert_sting_middle(out_string, in_string):
    return out_string[:int(len(out_string)/2)] + in_string + out_string[int(len(out_string)/2):]

print(insert_sting_middle('{{}}', 'PHP'))
print('*--------------------*')

# Exercise 10: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def remove_substring(string, pos1, pos2):
    return string[:pos1] + string[pos2+1:]
    
print(remove_substring('Hello there', 2, 6))






