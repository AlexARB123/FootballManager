"""
    Author: Alejandro Rodriguez
    Brief: Document contains implementation for the player class
"""

class Player:
    """
        Class Attributes:
            currID -> Class attribute for assigning an individual ID to each player
            idNum -> Unique ID number for each player used for identification and interaction with other classes. (USED INTERNALLY)
            LeagueID -> Player's ID number for the league
            Name -> Player's Name
            Number -> Jersey number if available, else represented with a -1
            Position (List) -> List of Player's Positions
                Offensive -> QB, RB, WR, TE, OT, OG, C
                Defensive -> DL, DE, ILB, OLB, CB, S
                Special Teamer -> P, K, PR, KR, LS
            these are supposed to be general and not representative of the formation they play. Aside from their regular position a player is also
            allowed to be in special teams.
    """
    currID = 1

    # Initialization method
    def __init__(self, LeagueID, Name, Number, Position):
        self.idNum = Player.currID
        Player.currID = Player.currID + 1
        self.LeagueID = LeagueID
        self.Name = Name
        self.Number = Number
        self.Position = Position

    # Setter methods for overriding
    def setLeagueID(self, LeagueID):
        self.LeagueID = LeagueID
    
    def setName(self, Name):
        self.Name = Name
    
    def setNumber(self, Number):
        self.Number = Number
    
    def setPosition(self, Position):
        self.Position = Position
    
    # Edit Player function for more general editing
    def editPlayer(self, LeagueID, Name, Number, Position):
        self.LeagueID = LeagueID
        self.Name = Name
        self.Number = Number
        self.Position = Position

    
    # Treating as a string
    def __str__(self) -> str:
        return f"{self.Number} \t {self.Name} \t {self.Position}"