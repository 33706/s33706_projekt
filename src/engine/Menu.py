import re
from entities.Player import Player


class Menu:
    @staticmethod
    def display_main_menu():
        print("[]" * 20)
        print("[]----------WELCOME TO TINYRPG--------[]")
        print("[]" * 20)
        print("1. New Game")
        print("2. Load Game")
        print("3. Quit")
        print("[]" * 20)

    @staticmethod
    def get_main_menu_choice():
        while True:
            choice = input("Pick an option: ").strip()
            if choice in ["1","2","3"]:
                return choice
            else: print("Pick a valid option")

    @staticmethod
    def create_new_hero():
        print("[]" * 20)
        print("[] Whats your hero's name? []")
        print("[]" * 20)
        while True:
            playername = input().strip()
            if re.match("^[A-Za-z]{2,15}", playername):
                return Player(playername)
            else:
                print("Pick a valid name (no special characters, min. 3 letters long)")