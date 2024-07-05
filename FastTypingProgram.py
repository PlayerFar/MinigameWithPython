#Typing Program Made By Farid (4/7/2024)
#Explanation: So Program will Give you a random 6 character and you must type that 6 character below 4 - 32 Second
#Explanation2: This Minigame have 7 Stage
#Im Using Module:inputimeout,random and time
#So Makes sure already installed all the modules
from inputimeout import inputimeout
import random
import time
char = ["a", "b", "c", "d", "e", "f", "g","h", "i","j","k","l","m","n","o","p","q","r","s","t","u",'v',"w","x","y","z"]
tIme = 36
level = 0    
#Main Program Function
def program(char,tIme,level):
    #Program that make all the random char
    char1 = char[random.randrange(0,25)]
    char2 = char[random.randrange(0,25)]
    char3 = char[random.randrange(0,25)]
    char4 = char[random.randrange(0,25)]
    char5 = char[random.randrange(0,25)]
    char6 = char[random.randrange(0,25)]
    char7 = char[random.randrange(0,25)]
    ans = char1 + char2 + char3 + char4 + char5 + char6 + char7
    #the input,Lose,time limit and Level Program
    try:
        print("Level: " + str(int(level + 1)))
        print("You Have " + str(int(tIme - 4)) + " Seconds To Type")
        print("Get Ready! ")
        time.sleep(5)      
        typing = inputimeout(prompt = "Type: " + ans,timeout = 5)
        if typing == ans:
            print("You won!")
            input("Continue.. -press space-")
            system(char,tIme - 4,level + 1)
        else: 
            print("Wrong Input!")
            print("You Lose..!\ntoo bad hahaha")             
    except:
        print("You Lose")
        print("Too bad Sir you so slow... \nGood Bye Have A Nice Day!\nHope Y Win next time")
        exit(1)
#Program that Check Our Level For Winning Condition        
def system(char,time,level):
     if level == 7:
         WinCondition()
     else:   
         program(char,time,level)   
#Program for Winning Condition         
def WinCondition():
    name = input("Wow You win!,Please input your Name: ")
    print("Congratulations!! to you! " + name)
    print("I Dind't expect you will win")     
    time.sleep(2)
    print("But..")
    time.sleep(2)
    print("Still Congrats and Goodbye! ")
    time.sleep(25)
    print("uh... you can go now..")
system(char,tIme,level)    
