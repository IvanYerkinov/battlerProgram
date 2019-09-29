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
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_kill(self, num_kill):
        self.kills += num_kill

    def add_death(self, num_death):
        self.deaths += num_death

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
                self.add_kill(1)
                opp.add_death(1)
                print(self.name + " won!")
                return
            self.take_damage(opp.attack())
            if self.is_alive() is False:
                opp.add_kill(1)
                self.add_death(1)
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

    def attack(self, other_team):
        while True:

            if self.is_teamlive() is False or other_team.is_teamlive() is False:
                return

            hero1 = self.heros[random.randint(0, len(self.heros))]
            while hero1.is_alive() is False:
                hero1 = self.heros[random.randint(0, len(self.heros))]
            hero2 = other_team.heros[random.randint(0, len(other_team.heros))]
            while hero2.is_alive() is False:
                hero2 = other_team.heros[random.randint(0, len(other_team.heros))]

            hero1.fight(hero2)

    def revive_heroes(self, health=100):
        for entity in self.heros:
            entity.current_hp = health
            if entity.current_hp > entity.starting_hp:
                entity.current_hp = entity.starting_hp

    def stats(self):
        for entity in self.heros:
            print(entity.name + ": K/D: " + entity.kills + "/" + entity.deaths)

    def is_teamlive(self):
        check = len(self.heros)
        num = 0

        for en in self.heros:
            if en.is_alive() is False:
                num = num+1

        if num == check:
            return False
        return True


if __name__ == "__main__":
    ability = Ability("Debug", 20)
    armor = Armor("Debug Armor", 20)
    hero = Hero("Test")

    ability2 = Ability("Ability2", 20)
    armor2 = Armor("Armor2", 20)
    hero2 = Hero("Test2")

    hero.fight(hero2)
