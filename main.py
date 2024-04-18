from Classes.Player import Player
from Classes.Team import Team
from Classes.Formation import *

P1 = Player(17213, 'Roberto', 9, ['OLB', 'QB'])
P2 = Player(88888, 'Oliver', 0, ['ILB', 'P'])

Players = [P1, P2]

t = Team(Players)

t.printTeam()

F1 = DefensiveFormation("Nickel", "Nickel formation for defending passes", "4-3")
F1.assignFormation()
print(F1)
