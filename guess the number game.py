import random
play=True
number=str(random.randint(0,200))
print("I will generate a number from 0 to 200, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
while play:
    guess=input("Give me your best guess! \n")
    if number==guess:
        print("You win the game! HOORAY")
        print("The number was",number)
        break
    else:
        print("Your guess is not correct, try again. \n")