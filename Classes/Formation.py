"""
    Author: Alejandro Rodriguez
    Brief: Formation Classes for Defensive, Offensive and Special Team Formations
    All formations account only for players on team
"""

class Formation:
    """
        Attributes:
            Name -> Formation Name
            Positions -> Dictionary of formation with the position name in formation and their location left to right
            Description -> Formation Description
    """
    def __init__(self, Name, Description) -> None:
        self.Name = Name
        self.Description = Description
        pass

    def __str__(self) -> str:
        print(f'{self.Name}: {self.Description}')
        pass

    def assignFormation(self):
        self.Positions = {}
        
        for i in range(11):
            newPos = input("Enter Position Name:\t")
            self.Positions[newPos] = i
        print(self.Positions)


class OffensiveFormation(Formation):
    """
        Attributes:
            Personnel -> Offensive Personel in a RB-TE-WR Format
    """
    def __init__(self, Name, Description, Personnel) -> None:
        super().__init__(Name, Description)
        self.Personnel = Personnel

    def __str__(self):
        super().__str__()
        pass

class DefensiveFormation(Formation):
    """
        Attributes:
            Personnel -> Defensive Personnel in a (DL - LB) format. Rest are assumed to be Defensive Backs
    """
    def __init__(self, Name, Description, Personnel) -> None:
        super().__init__(Name, Description)
        self.Personnel = Personnel

    def __str__(self):
        super().__str__()
        pass

class SpecialFormation(Formation):
    """
        Attributes:
            FormationType -> Whether it is a Kickoff (K), Kickoff Return (KR), Punt (P) or PuntReturn(PR)
    """
    def __init__(self, Name, Description, FormationType) -> None:
        super().__init__(Name, Description)
        self.FormationType = FormationType
    
    def __str__(self):
        super().__str__()
        pass