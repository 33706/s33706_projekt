import json

from engine.Menu import Menu


class GameEngine:
    def __init__(self):
        self.player = None
        self.running = True

    def start(self):
        # add welcome display
        while self.running:
            if self.player is None:
                Menu.display_main_menu()
                choice = Menu.display_main_menu()
                match choice:
                    case "1":
                        print()
                        #create new character
                        self.player = Menu.create_new_hero()
                    case "2":
                        print()
                        #load game
                    case "3":
                        self.running = False
            else:
                #Main game logic
                print()

    def save_game(self):
        save_file = {
            "name": self.player.name,
            "hp": self.player.hp,
            "dmg": self.player.dmg,
            "gold": self.player.gold,
            "inventory": self.player.inventory
        }
        with open("data/saves/save_slot1.json", "w") as file:
            json.dump(save_file, file)
        print("Game saved!")