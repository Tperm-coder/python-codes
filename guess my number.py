import os
os.system('color b')
os.system('cls')
omen = True
while omen :
    os.system('cls')
    jett = input('if you want me to guess your number type pop \nif you want to guess my number type bob')
    if jett == 'bob' :
        print('i will choose a random number from 1 to 100 and you have to guess it \ni will guide you along the way')
        import random
        x = random.randint(1,100)
        guess = int(input('what is your guess ?'))
        counter = 1
        while guess != x :
            while guess>x :
                print('no your guess is high')
                guess= int(input('try again '))
                counter = counter + 1

            while guess<x :
                print('no your guess is low')
                guess= int(input('try again '))
                counter = counter + 1

        print('you got me it took you ' +str(counter) +' tries')
        input()
    # import random
    # os.system('cls')
    # x = random.randint(1,100)
    # guess = int(input('what is your guess ?'))
    # counter = 0
    # while guess!=x :
    #     if guess > x :
    #         os.system('cls')
    #         print('no your guess is high')
    #         guess= int(input('try again '))
    #         counter = counter + 1
    #     elif guess < x :
    #         os.system('cls')
    #         print('no your guess is high')
    #         guess= int(input('try again '))
    #         counter = counter + 1



    if jett == 'pop' :
        import random
        print('choose a random number from 1 to 100 and i will guess it ')
        input('press enter when you are ready ')
        x = random.randint(1,100)
        ans = input('is ' + str(x) + ' your number yes or no ?')
        maximum = 100
        minimum = 0
        counter =1
        while ans  == 'no' :
            reply = input('is my guess high or low ?')
            if reply == 'high' :
                maximum = x-1
                x= random.randint(minimum,(x-1))
                ans =input('is ' + str(x) + 'your number yes or no ?')
                counter = counter + 1


            elif reply == 'low'  :
                minimum = 1 + x
                x = random.randint((x+1),maximum)
                ans =input('is ' + str(x) + ' your number yes or no ?')
                counter = counter + 1

        print ('i got you it took me '+ str(counter) + ' tries')
        input()
    sage = input('do you want to try again yes or no ?')
    if sage == 'yes' :
        omen = True
    else :
        omen = False
