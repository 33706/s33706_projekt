from util.decorators import cast_spell


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.gold = 10
        self.mana = 3
        self.new_player = True

    @cast_spell(mana_cost=1)
    def weaken_enemy(self, monster):
        monster.hp = monster.damage // 2
        print(f"{monster.name} weakened! {monster.hp}hp left")