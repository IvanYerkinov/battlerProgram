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

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

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

            hero1 = self.heros[random.randint(0, len(self.heros) - 1)]
            while hero1.is_alive() is False:
                hero1 = self.heros[random.randint(0, len(self.heros) - 1)]
            hero2 = other_team.heros[random.randint(0, len(other_team.heros) - 1)]
            while hero2.is_alive() is False:
                hero2 = other_team.heros[random.randint(0, len(other_team.heros) - 1)]

            hero1.fight(hero2)

    def revive_heroes(self, health=100):
        for entity in self.heros:
            entity.current_hp = health
            if entity.current_hp > entity.starting_hp:
                entity.current_hp = entity.starting_hp

    def stats(self):
        for entity in self.heros:
            print(entity.name + ": K/D: " + str(entity.kills) + "/" + str(entity.deaths))

    def is_teamlive(self):
        check = len(self.heros)
        num = 0

        for en in self.heros:
            if en.is_alive() is False:
                num = num+1

        if num == check:
            return False
        return True


class Arena:
    def __init__(self):
        team_one = None
        team_two = None

    def create_ability(self):
        name = input("Please enter an ability name: \n")

        mxdmg = None
        while not type(mxdmg) == int:
            mxdmg = input("Please enter this abilities max damage: \n")
            mxdmg = int(mxdmg)

        return Ability(name, mxdmg)

    def create_weapon(self):
        name = input("Please enter a weapon name: \n")

        mxdmg = None
        while not type(mxdmg) == int:
            mxdmg = input("Please enter this weapons max damage: \n")
            mxdmg = int(mxdmg)

        return Weapon(name, mxdmg)

    def create_armor(self):
        name = input("Please enter an armor name: \n")

        mxdmg = None
        while not type(mxdmg) == int:
            mxdmg = input("Please enter this armors max defence: \n")
            mxdmg = int(mxdmg)

        return Armor(name, mxdmg)

    def create_hero(self):
        name = input("Please enter this hero's name: \n")
        ability = None
        weapon = None
        armor = None

        print("Do you want to give this hero an ability?")
        ch = input("y/n? \n")
        if ch == "y":
            ability = self.create_ability()
        else:
            ability = Ability("None", 0)

        print("Do you want to give this hero a weapon?")
        ch = input("y/n? \n")
        if ch == "y":
            weapon = self.create_weapon()
        else:
            weapon = Weapon("None", 0)

        print("Do you want to give this hero some armor?")
        ch = input("y/n \n")
        if ch == "y":
            armor = self.create_armor()
        else:
            armor = Armor("None", 0)

        hero = Hero(name)
        hero.add_ability(ability)
        hero.add_weapon(weapon)
        hero.add_armor(armor)

        return hero

    def build_team_one(self):
        name = input("Please name Team One: \n")
        team1 = Team(name)

        num = int(input("How many heros do you want on Team One?: \n"))

        if type(num) != int:
            num = 3

        for i in range(0, num):
            team1.add_hero(self.create_hero())

        self.team_one = team1

    def build_team_two(self):
        name = input("Please name Team Two: \n")
        team2 = Team(name)

        num = int(input("How many heros do you want on Team Two?: \n"))

        if type(num) != int:
            num = 3

        for i in range(0, num):
            team2.add_hero(self.create_hero())

        self.team_two = team2

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("===Team One Stats===")
        self.team_one.stats()
        print()
        print("===Team Two Stats===")
        self.team_two.stats()


f __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
