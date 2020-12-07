from random import randint
import sys
#create a list of play options
t = ["Rock", "Paper", "Scissors", "Fire", "Water"]

#assign a random play to the computer
computer = t[randint(0,4)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors, Fire, Water ? For Quit type Exit\n")
    print(computer)
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer in ["Paper" or "Water"]:
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer in ["Scissors" or "Fire"]:
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer in ["Rock" or "Fire"]:
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    elif player == "Fire":
        if computer in ["Water","Rock"]:
            print("You lose...", computer, "extinguish", player)
        else:
            print("You win!", player, "burn", computer)
    elif player == "Water":
        if computer in ["Paper","Scissors"]:
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "drown", computer)
    elif player == "Exit":
        sys.exit()
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,4)]
