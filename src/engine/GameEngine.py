import json
import random

from engine.Menu import Menu
from entities.Player import Player
from story.Story import Story
from entities.Enemy import Enemy
from util.excepltions import SlotEmptyException

class GameEngine:
    def __init__(self):
        self.player = None
        self.running = True

    def start(self):
        while self.running:
            if self.player is None:
                choice = Menu.display_main_menu()
                match choice:
                    case "1":
                        self.player = Menu.create_new_hero()
                    case "2":
                        slot = input("Enter slot number: ")
                        try:
                            self.load_game(slot)
                        except FileNotFoundError:
                            print("no slot found!")
                        except SlotEmptyException as e:
                            print(f"{e.message}")
                    case "3":
                        self.running = False
            else:
                if self.player.hp <= 0:
                    Story.death()
                    self.running = False
                    break
                if self.player.new_player is True:
                    Story.start_adventure(self.player.name)
                    self.player.new_player = False
                    input("Press any key to continue...")
                if self.player.gold >= 50:
                    Story.end_adventure()
                    self.running = False
                    break
                newMonster = Enemy(Enemy.get_rand_name(), random.randint(1, 20), random.randint(1, 10))
                if newMonster.damage <= 5:
                    Story.encounter1(newMonster)
                    print("Cast Weaken enemy for 1 mana ?\n"
                          "1. Yes\n2. No\n")
                    if input() == "1":
                        self.player.weaken_enemy(newMonster)
                    roll = Menu.roll_d20()
                    if roll >= newMonster.damage:
                        Story.encounter1_win(newMonster)
                        input()
                        self.victory(newMonster)
                    else:
                        Story.encounter1_loss(newMonster)
                        input()
                        self.loss()
                elif newMonster.damage in range(5, 15):
                    Story.encounter2(newMonster)
                    print("Cast Weaken enemy for 1 mana ?\n"
                          "1. Yes\n2. No\n")
                    if input() == "1":
                        self.player.weaken_enemy(newMonster)
                    roll = Menu.roll_d20()
                    if roll >= newMonster.damage:
                        Story.encounter2_win(newMonster)
                        input()
                        self.victory(newMonster)
                    else:
                        Story.encounter2_loss(newMonster)
                        input()
                        self.loss()
                elif newMonster.damage >= 15:
                    Story.encounter3(newMonster)
                    print("Cast Weaken enemy for 1 mana ?\n"
                          "1. Yes\n2. No\n")
                    if input() == "1":
                        self.player.weaken_enemy(newMonster)
                    roll = Menu.roll_d20()
                    if roll >= newMonster.damage:
                        Story.encounter3_win(newMonster)
                        input()
                        self.victory(newMonster)
                    else:
                        Story.encounter3_loss(newMonster)
                        input()
                        self.loss()
                print("continue or save and quit ?")
                choice2 = input("1. next adventure\n2. save and quit\n")
                if choice2 == "1":
                    continue
                elif choice2 == "2":
                    slot = input("Enter slot number: ")
                    self.save_game(slot)
                    self.running = False

    def victory(self, newMonster):
        self.player.gold += newMonster.reward
        print(f"You take your payment of {newMonster.reward} gold")
        print(f"You currently have {self.player.gold} gold")
        print(f"Just {50 - self.player.gold} gold left to go!\n")

    def loss(self):
        self.player.hp -= 1
        print(f"You lose 1hp and move on. ({self.player.hp}hp left)\n")

    def save_game(self, slot):
        save_file = {
            "name": self.player.name,
            "hp": self.player.hp,
            "gold": self.player.gold,
            "mana": self.player.mana,
            "new_player": self.player.new_player
        }
        with open(f"data/saves/save_slot{slot}.json", "w") as file:
            json.dump(save_file, file)
        print("Game saved!")

    def load_game(self, slot):
        with open(f"data/saves/save_slot{slot}.json", "r") as file:
            save_file = json.load(file)
        self.player = Player(save_file["name"])
        self.player.hp = int(save_file["hp"])
        self.player.gold = int(save_file["gold"])
        self.player.mana = int(save_file["mana"])
        self.player.new_player = save_file["new_player"]
        print("Game loaded!")