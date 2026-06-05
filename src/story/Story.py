class Story:
    @staticmethod
    def start_adventure(name):
        print(f"'And don't you dare come back into my inn without 50 gold!' said the innkeeper.\n"
              f"And so does you story begin, a broke, washed up hedge knight by the name of {name}.\n"
              f"You travel out into the wilds, taking contract after contract, hunting various monsters for gold.\n"
                f"Just so you may pay off your tab at the inn and start anew\n")

    @staticmethod
    def end_adventure(name):
        print(f"'Merlin's beards, are my eyes mistaken or is it {name}!?' - exclaims the innkeeper\n"
              f"'I assume you wouldn't be so foolish as to come back without my gold now would you ?'\n"
              f"You slide the coins his way on the counter, he looks in disbelief\n"
              f"'Well would you look at that! A smart choice my friend' satisfied he says\n"
              f"'Listen up all you drunkards, next round's on {name}!")

    @staticmethod
    def encounter1(monster):
        print(f"Creeping behind the branches you find a {monster.name}! ({monster.damage}dmg)\n"
              f"It growls at you menacingly. You're both at a stare-off for a couple seconds.\n"
              f"suddenly it leaps towards you!\n")

    @staticmethod
    def encounter1_win(monster):
        print(f"With lightning reflexes, you sidestep the lunging {monster.name}!\n"
              f"You find a perfect opening and strike a decisive blow, sending the beast to the ground.\n"
              f"The area falls silent. You stand victorious!\n")

    @staticmethod
    def encounter1_loss(monster):
        print(f"The {monster.name} moves faster than your eyes can follow!\n"
              f"Its brutal attack knocks you off balance, sending your weapon flying into the dirt.\n"
              f"Darkness closes in as you realize this was a fight you couldn't win...\n")

    @staticmethod
    def encounter2(monster):
        print(f"The air turns freezing cold as a shadow detaches itself from the walls. It's a {monster.name}! ({monster.damage}dmg)\n"
              f"Its eyes glow with an eerie, unnatural light through the thick mist.\n"
              f"There is no time to run – draw your weapon!\n")

    @staticmethod
    def encounter2_win(monster):
        print(f"Sensing the danger, you parry the {monster.name}'s icy claws just in time.\n"
              f"You counter with a fierce attack, shattering its defense and banishing the creature back into the dark.\n"
              f"You catch your breath, your heart pounding, but you are alive.\n")

    @staticmethod
    def encounter2_loss(monster):
        print(f"The freezing aura of the {monster.name} paralyzes your limbs.\n"
              f"You try to swing your sword, but your grip fails as the monster delivers a devastating strike.\n"
              f"You scamper away with your tail tucked between your legs.\n")

    @staticmethod
    def encounter3(monster):
        print(f"The ground trembles beneath your feet as a massive, towering shadow blocks the light.\n"
              f"Before you stands the legendary {monster.name} ({monster.damage}dmg), radiating pure malice and crushing power.\n"
              f"Every instinct in your body screams to run, but there is no escape. Prepare for a brutal clash!\n")

    @staticmethod
    def encounter3_win(monster):
        print(f"Against all odds, your blade finds a fatal flaw in the armor of the mighty {monster.name}!\n"
              f"With a final, desperate strike, you pierce its heart. The colossus roars in agony before crashing down,\n"
              f"shattering the earth beneath it. You have achieved an impossible victory. You are a true legend!\n")

    @staticmethod
    def encounter3_loss(monster):
        print(f"The sheer force of the {monster.name}'s attack shatters your guard completely.\n"
              f"You are thrown against the stone wall, gasping for air as your armor cracks to pieces.\n"
              f"Running away like a scared little child, your battle ends in defeat.\n")

    @staticmethod
    def death():
        print("And so does your story come to an end\n"
              "Lying in the forest, forgotten with no one to mourn you")