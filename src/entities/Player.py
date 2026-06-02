from src.items.Inventory import Inventory

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.dmg = 5
        self.gold = 10
        self.inventory = Inventory()