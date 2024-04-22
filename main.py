from Classes.Player import Player
from Classes.Team import Team
from Classes.Formation import *
import json

Players = []
while True:
    s = input("Enter A if you wish to add a new player, enter Q if you wish to quit and proceed")
    
    if s == "A":
        name = input("Enter Player Name: ")
        Num = input("Enter Player's Jersey Number: ")
        id = input("Enter player's league ID: ")
        Positions = []
        primary = input("Enter player's primary position: ")
        Positions.append(primary)
        decision = input("Would you like to add a special teams position? Y/N")
        if decision == "Y":
            secondary = input("Enter Player's special team's position")
            Positions.append(secondary)
        
        newPlayer = Player(id,name,Num,Positions)
        Players.append(newPlayer)
    elif s == "Q":
        break
    else:
        print("Invalid Input")

thisTeam = Team(Players)
thisTeam.printTeam()

file = thisTeam.convertToDict()
s = json.dumps(file)
print(s)



