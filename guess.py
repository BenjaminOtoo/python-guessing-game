import random

def guess(x):
    random_number = random.randint(1, x)
    tries = 0
    maxtries = num
    numlst = list()  
    while True:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess == random_number:
            print("\nCONGRATULATIONS!! you guessed the number!")
            break
        elif tries < maxtries - 1 and guess > random_number:
            numlst.append(guess)
            tries += 1
            print("\nGUESS LOWER\nYou have", maxtries - tries, "attempts remaining")
            print("previous guesses", numlst, "\n")
        elif tries < maxtries - 1 and guess < random_number:
            numlst.append(guess)
            tries += 1
            print("\nGUESS HIGHER\nYou have", maxtries - tries, "attempts remaining") 
            print("previous guesses", numlst, "\n")       
        else:
            print("\nGAME OVER, You have no attempts remaining")
            print("The number was", random_number)
            break    

#User must input the maximum number for the range of guesses and maximum attempts
maxnum = int(input("Enter the maximum number: "))
num = int(input("How many attempts do you want?: "))
guess(maxnum)