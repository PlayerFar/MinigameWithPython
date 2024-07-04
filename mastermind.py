#Mastermind Program Made by Farid,(25/6/2024)
import random
print("Welcomes to Games of Mastermind!")
#random system
num1 = random.randrange(0,8)
num2 = random.randrange(0,8)
num3 = random.randrange(0,8)
num4 = random.randrange(0,8)
life = 10
#guessing system
def program(num1, num2, num3, num4, life):
    answer = str(num1) + str(num2) + str(num3) + str(num4)
    tuple_answer = tuple(answer)
    guess = input("Input 4 Numbers!")
    tuple_guess = tuple(guess)
    if guess == answer:
        print("You won!")
        print("The Right Answer is = " + answer)
        exit(1)
    if guess != answer:
        if tuple_guess[0] == tuple_answer[0]:
            print(tuple_guess[0] + " Is Red")
        elif tuple_guess[0] in tuple_answer:
            print(tuple_guess[0] + " Is White")
        else:
            print(tuple_guess[0] + " Is black")
        if tuple_guess[1] == tuple_answer[1]:
            print(tuple_guess[1] + " Is Red")
        elif tuple_guess[1] in tuple_answer:
            print(tuple_guess[1] + " Is White")
        else:
            print(tuple_guess[1] + " Is black")
        if tuple_guess[2] == tuple_answer[2]:
            print(tuple_guess[2] + " Is Red")
        elif tuple_guess[2] in tuple_answer:
            print(tuple_guess[2] + " Is White")
        else:
            print(tuple_guess[2] + " Is black")
        if tuple_guess[3] == tuple_answer[3]:
            print(tuple_guess[3] + " Is Red")
        elif tuple_guess[3] in tuple_answer:
            print(tuple_guess[3] + " Is White")
        else:
            print(tuple_guess[3] + " Is black")
        life -= 1
        print("Your Lifes: " + str(life))
        system(num1, num2, num3, num4, life)
#life and Lose System        
def system(num1, num2, num3, num4, life):
    while life != 0:
        program(num1, num2, num3, num4, life)      
    else:
        print("You Lose!")
        exit(1) 
system(num1, num2, num3, num4, life)        
