print("Welcome to MagicStone")
Start = input("Want to start a game ? yes/no \n")
if Start == ("yes") :
    print("")
if Start == ("no") :
    print ("Hope you will change your mind")


class Card:
    def __init__(self, name, cost, mana, description):
        self.name = ""
        self.cost = ""
        self.mana = ""
        self.description = ""

card = {"name" : " ", "cost" : " ", "mana" : " ", "description": " "}
cardEx = {"Silence": {"Silence", "0", "0", "Réduit à silence un ennemi adverse"}}

class Mage :
    def __init__(self, hand, discard, gamezone):
        self.name = ""
        self.hand = ""
        self.discard = ""
        self.gamezone = ""

class Cristal(Card):
    def __init__(self, name):
        self.name = ""

class Creature(Card):
    def __init__(self, name,):
        self.name = ""

class Blast(Card):
    def __init__(self, name,):
        self.name = ""