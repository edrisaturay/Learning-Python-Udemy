from random import randint

#generate a number 1-10
answer = randint(1, 10)

#check that input is a number 1-10

while True:
    try:
        # Input from user
        num = input('Guess a number 0-10: ')
        if int(num) > 0 and int(num) < 11:
            print('You got the number')
            break
        else:
            continue
    except ValueError:
        print('Please enter a number')


