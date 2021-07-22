from random import randint
import sys


answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:


        guess = int(input('guess a number 1~10: '))
        if guess > 1 and guess < 11:
            if guess == answer:
                print('you are a genius')
                break
        else:
            print('he! i said 1~10')

    except ValueError:
        print('please enter a number')
        continue