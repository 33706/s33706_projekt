import random

name_lst = ["goblin", "orc", "troll", "drowner", "ghoul", "werewolf", "", "zombie", "vampire"]

class Enemy:
    def __init__(self, name, damage, reward):
        self.name = name
        self.damage = damage
        self.reward = reward

    @staticmethod
    def get_rand_name():
        new_names = [x for x in name_lst if x != ""]
        return random.choice(new_names)