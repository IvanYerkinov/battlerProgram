import random


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_dmg = max_damage

    def attack(self):
        return random.randint(0, self.max_dmg)


class Armor:
    def __init__(self, name, max_block):
        pass

    def block(self):
        pass


class Hero:
    def __init__(self, name, starting_health=100):
        pass

    def add_ability(self, ability):
        pass

    def attack(self):
        pass

    def defend(self, inc_dmg):
        pass

    def is_alive(self):
        pass

    def fight(self, opp):
        pass


if __name__ == "__main__":
    ability = Ability("Debug", 20)
    print(ability.name)
    print(ability.attack())
