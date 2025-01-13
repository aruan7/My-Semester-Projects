#Multiplication Quiz

import random

print("Welcome to Multiplication Quiz!")

score = 0

def questions():
    for i in range(5):
        num1 = random.randint(1,10) #Variable that generates random int from 1-10
        num2 = random.randint(1,10)
        result = int(num1) * int(num2)
        print("What is " + str(num1) + " * " + str(num2))
        answer = int(input()) #Collects user's input
        print("your answer: " + str(answer)) #Tells user what they put as their answer
        if answer == result:
            print("Correct!")
            global score #Updates user's score
            score = score + 1
        else:
            print("Incorrect, the correct answer is " + str(result))

def final_score():
    print("You got " + str(score) + " out of 5 questions correct")

questions()
final_score()
