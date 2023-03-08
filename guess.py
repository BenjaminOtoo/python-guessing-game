import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    tries = 0
    maxtries = num
    while guess != random_number and tries != maxtries:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess == random_number:
            print("Congratulations you guessed the number!")
            break
        elif tries < maxtries - 1:
            tries += 1
            print("Sorry try again, You have", maxtries - tries, "attempts remaining")    
        else:
            print("GAME OVER, You have no attempts remaining")
            print("The number was", random_number)
            break    

#User must input the maximum number for the range of guesses
maxnum = int(input("Enter the maximum number: "))
num = int(input("How many attempts do you want: "))
guess(maxnum)