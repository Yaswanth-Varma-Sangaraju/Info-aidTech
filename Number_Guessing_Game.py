import random
a=input('Hello, your good name please ?: ')
print('1. You have to guess a number in between 1 & 100\n 2. The computer will let you know wether the number you\'ve guessed is Too high (or) Too low.')
while True:
    b=random.randint(0,100)
    for i in range(10):
        c=input('Enter your Guess : ')
        try:
            c=int(c)
            if c < b-10:
                print('You are too low.')
            elif c > b+10:
                print('You are too high.')
            elif c < b:
                print('You are low.')
            elif c > b:
                print('You are high.')
            elif c==b:
                print('You won the game, Congratulations.')
                break
            print(str(9-i) + " Chances left.")
        except:
            print("Please enter a valid integer.")
    print("The number was: " + str(b))
    yesorno = input("Do you want to play(yes or no): ")
    if yesorno.lower() == "yes":
        continue
    else:
        break