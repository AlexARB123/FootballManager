"""
    Author: Alejandro Rodriguez
    Brief: Class to instantiate a team
"""
from Classes.Player import Player

class Team:
    """
        Class Attributes:
            Players -> List of all current players in the team, sorted by Player's idNum
            Offense -> List of all current Offensive Players, sorted by Player's idNum
            Defense -> List of all current Defensive Players, sorted by Player's idNum
            Special -> List of all current Special Teamers, sorted by Player's idNum
            Formations -> List of all formations the team manages including Offense, Defense and Special Teams
    """
    # Tuples for distinction between Positions and assignation
    OffensivePositions = ("QB", "RB", "WR", "TE", "OT", "OG", "C")
    DefensivePositions = ("DL", "DE", "ILB", "OLB", "CB", "S")
    SpecialPositions = ("P","K", "PR", "KR", "LS")
    
    # Initialization class that takes just a list of players and creates the other lists alongside it
    def __init__(self, Players):
        self.Players = Players
        self.Offense = []
        self.Defense = []
        self.Special = []
        self.Formations = []
        Players.sort(key = lambda x: x.idNum)
        
        for i in Players:
            self.assignPlayer(i)

    # Helper function for in real time player assignation
    def assignPlayer(self, Player):
        for j in Player.Position:
                if j in Team.OffensivePositions and Player not in self.Offense:
                    self.Offense.append(Player)
                elif j in Team.DefensivePositions and Player not in self.Defense:
                    self.Defense.append(Player)
                elif j in Team.SpecialPositions and Player not in self.Special:
                    self.Special.append(Player)
    
    # Function to add a Player to the team
    def addPlayer(self, Player):
        self.Players.append(Player)
        self.assignPlayer(Player)
    
    # Function to print all Players on the team by assignation  
    def printTeam(self):
        print("Offense")
        for i in self.Offense:
            print(i)
            
        print("Defense")
        for i in self.Defense:
            print(i)
            
        print("Special Teams")
        for i in self.Special:
            print(i)
            

