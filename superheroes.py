import random


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_dmg = max_damage

    def attack(self):
        return random.randint(0, self.max_dmg)


class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.max_dmg // 2)


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
        self.starting_hp = starting_health
        self.current_hp = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        atkdmg = 0

        for ab in self.abilities:
            atkdmg += ab.attack()

        return atkdmg

    def defend(self, inc_dmg):
        defdmg = 0

        for ar in self.armors:
            defdmg += ar.block()

        return defdmg

    def take_damage(self, damage):
        dmg = damage - self.defend(damage)

        if(dmg <= 0):
            dmg = 1

        self.current_hp -= dmg

    def is_alive(self):
        if self.current_hp <= 0:
            return False
        return True

    def fight(self, opp):
        while True:
            opp.take_damage(self.attack())
            if opp.is_alive() is False:
                print(self.name + " won!")
                return
            self.take_damage(opp.attack())
            if self.is_alive() is False:
                print(opp.name + " won!")
                return


class Team:
    def __init__(self, name):
        self.name = name
        self.heros = []

    def remove_hero(self, name):
        for i in range(0, len(self.heros)):
            if self.heros[i].name == name:
                self.heros.pop(i)
                return
        return 0

    def view_all_heros(self):
        for i in self.heros:
            print(i.name)

    def add_hero(self, hero):
        self.heros.append(hero)


if __name__ == "__main__":
    ability = Ability("Debug", 20)
    armor = Armor("Debug Armor", 20)
    hero = Hero("Test")

    ability2 = Ability("Ability2", 20)
    armor2 = Armor("Armor2", 20)
    hero2 = Hero("Test2")

    hero.fight(hero2)
