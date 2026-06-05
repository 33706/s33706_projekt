def cast_spell(mana_cost: int):
    def decorator(function):
        def wrapper(player, *args, **kwargs):
            if player.mana <= mana_cost:
                print("Not enough mana to cast")
                return False

            player.mana -= mana_cost
            return function(player, *args, **kwargs)
        return wrapper
    return decorator