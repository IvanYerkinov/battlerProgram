import random


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_dmg = max_damage

    def attack(self):
        return random.randint(0, self.max_dmg)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_hp = 100
        self.current_hp = 100

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        atkdmg = 0

        for ab in self.abilities:
            atkdmg += ab.attack()

        return atkdmg

    def defend(self, inc_dmg):
        pass

    def is_alive(self):
        pass

    def fight(self, opp):
        pass


if __name__ == "__main__":
    ability = Ability("Debug", 20)
    armor = Armor("Debug Armor", 20)
    hero = Hero("Test")

    print(ability.name)
    print(ability.attack())

    print(armor.name)
    print(armor.block())

    print(hero.name)
    print(hero.current_hp)

    hero.add_ability(ability)
    print(hero.attack())
