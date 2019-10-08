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

user_number = 1
counter = 0

while user_number >= 0:
    user_number = int(input('Please enter a number: '))

    if user_number  >= 0:
        if counter == 0:
            min_number = user_number
        elif user_number < min_number:
            min_number = user_number

        counter += 1

print('you entered', counter, 'positive numbers. The lowest number was', min_number)



