class Player:
    def __init__(self,position,mouvementRange,attackRange,blockRange,blockTime,attackSpeed):
        self.position = position
        self.mouvementRange = mouvementRange
        self.attackRange = attackRange
        self.attackSpeed = attackSpeed
        self.blockRange = blockRange
        self.blockTime = blockTime
        self.hauteur = 0
        self.score =0
        self.jump = False  
        self.attack = False
        self.defense = False   
        self.initPosition = position
        self.touched = False

