import turtle
import random
angie=turtle.Turtle()

def pick_a_number():
    num = int(input("Please guess a number"))
    ran = int(random.randint(1,10))
    if ran == int(random.randint(1,10)):
        print("Congratulations!")
    else:
        print("You have lost. The correct number was: " + str(ran))

pick_a_number()
