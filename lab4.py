## Lab 4

### Excercise 1
##for i in range(2000, 3201):
##    if (i % 7 == 0) and (i % 5 !=0):
##        print (i)


### Excercise 2
##while True:
##    user_string = input('Please entere a combination of letters and numbers: ')
##    counter = 0
##
##    for l in user_string:
##        if '0' <= l <= '9':
##            counter +=1
##    print (counter)


### Excercise 3
##while True:
##    user_string = input('Please entere a combination of letters and numbers: ')
##    num_counter = 0
##    let_counter = 0
##
##    for l in user_string:
##        if '0' <= l <= '9':
##            num_counter +=1
##        #elif ('A' <= l <= 'z'):
##        elif ('A' <= l <= 'Z') or ('a' <= l <= 'z'):
##            let_counter +=1
##            print(l)
##        
##    print ('you entered', num_counter, 'numbers and', let_counter, 'letters')


    
### Excercise 4

##user_string = input('Please enter a numbers: ')
##counter = 0
##
##for digit in user_string:
##    counter+=int(digit)
##
##print ('the sum of digits is', counter)



### Excercise 4a
##user_string = int(input('Please enter a number: '))
##answer = 0
##
##while user_string != 0:
##    answer += user_string % 10
##    user_string = user_string // 10
##    
##print ('the sum of digits is', answer) 


### Excercise 5

##user_number = 1
##counter = 0
##
##while user_number >= 0:
##    user_number = int(input('Please enter a number: '))
##
##    if user_number  >= 0:
##        if counter == 0:
##            min_number = user_number
##        elif user_number < min_number:
##            min_number = user_number
##
##        counter += 1
## print('you entered', counter, 'positive numbers. The lowest number was', min_number)



# Test if a number is happy. *************************************************************
# A happy number is when you add the squares of the digits repeatedly until you get 1
# A nuber is unhappy if you do it until you get 4.
# You will always get 1 or 4

##start_num = 0
##intermediate_num = start_num
##counter = 0
##
##while counter < 20:
##
##    start_num += 1
##
##    intermediate_num = start_num
##
##    while intermediate_num != 1 and intermediate_num != 4:
##
##        temp = 0
##
##        for i in str(intermediate_num):
##            temp += int(i)**2
##
##        intermediate_num = temp
##        #print(intermediate_num)
##
##
##    if intermediate_num == 1:
##        print(start_num, 'is a happy number')
##        counter+=1
##    #else:
##    #    print(start_num , 'is not a happy number')



# Redo the happy number with a function ***********************************************

##def is_happy(number):
##    while number != 1 and number != 4:
##        temp = 0
##        for i in str(number):
##            temp += int(i)**2
##        number = temp
##
##    return number == 1
##
##
##counter = 0
##test_num = 1
##
##while counter<20:
##    if (is_happy(test_num)):
##        print (test_num)
##        counter += 1
##    test_num+=1


## Additional excercises *****************************************************************
##2. Ask the user for a number and print all divisors of that number.
##A divisor is a number that divides evenly into another number.
##For example 2, 3, 4 and 6 are divisors of 12.

##user_input = 12
##counter = 0
##for i in range(2, int(user_input/2) + 1):
##    if user_input % i == 0:
##        print (i, end=' ')
##        counter+=1
##
##if counter==0:
##    print('you entered a prime number')
    

##3. Write a program for checking the speed of drivers. This program
#               should ask the user for the speed and do one of the following:
##
##    If speed is less than 70, it should print “Ok”.
##    Otherwise, for every 5km above the speed limit (70),
##     it should give the driver one demerit point and print the total number
##     of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
##    If the driver gets more than 12 points, the function should print: “License suspended”

driver_speed = 78
while True:
    driver_speed = int(input('Please enter a drivers speed: '))

    if driver_speed <= 70:
        print ('OK')
    elif driver_speed < 70+5*12:
        print ('Points', (driver_speed - 70) // 5)
    else:
        print ('License suspended')
