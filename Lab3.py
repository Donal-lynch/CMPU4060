### Examples from class

##for i in range(10):
##    print(i, end = '*')


##for i in range(1,21):
##    if i%2==0:
##        print (i)

##s = input('keep entereing numbers. Enter 0 to end. \n')
##while s!='0':
##    print('you entered ', s)
##    s = input('Enter a number: ')
##print('Goodbye')


### Labs ********************************************************
# Excercise 1:
##i = 1
##
##while i <= 10:
##    print(i)
##    i+=1

# Excercise 2:
##for i in range(10):
##    print (i+1)


# Excercise 3:
##for i in range(21):
##    if i % 2 == 0: # even
##        print (i, 'is even')
##    else:
##        print (i, 'is odd')

### Excercise 4:
#for i in range(1, 11):
#    print (i, '* 9 =', i*9)

### Excercise 4a:
##for i in range(1, 11):
##    for j in range(1, 11):
##        print (i, '*', j, '=', i*j)

# Excercise 5
##total = 0
##
##user_value = int(input('please enter a number: '))
##
##for i in range(user_value+1):
##    total = total + i
##
##print('the sum from 0 to', user_value, 'is', total)


# Excercise 6
##total = 1
##
##user_value = int(input('please enter a number: '))
##
##for i in range(1, user_value+1):
##    total = total * i
##
##print('the factorial of', user_value, 'is', total)


# Excercise 7
##i = 0
##while i >= 0:
##    i = int(input('Please enter a number: '))
##    print('you entered', i)
##print('Goodbye')

# Excercise 8
##for i in range(5):
##    print ('*'*(i+1))

# Excercise 8 with nested loops
##for i in range(1, 6):
##    for j in range(1, i+1):
##        print('*', end = '')
##    print ('') #print a new line. After print default is new line


# Excercise 9
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end = '')
    print('')

                

                       
