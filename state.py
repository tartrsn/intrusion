import random

from constants import REGULAR_CITY_PROFIT, BIT_CITY_PROFIT, CITY_PROFIT_DICE, ARMY_PAY_DICE, FORTRESS_PAY_RATE, \
    FORTRESS_FORTIFY_PAY_RATE, STATE_INITIAL_MONEY


class Map:
    pass


class MapObject:
    pass


class City:

    def __init__(self, profit):
        self.profit = profit

    def generate_profit(self):
        return self.profit * random.randint(1, CITY_PROFIT_DICE)


class RegularCity(City):

    def __init__(self):
        super().__init__(REGULAR_CITY_PROFIT)


class BigCity(City):

    def __init__(self):
        super().__init__(BIT_CITY_PROFIT)


class Fortress:

    def __init__(self, fortified: bool):
        self.fortified = fortified
        self.fortification_step = 0

    def payday(self):
        if self.fortified:
            return FORTRESS_PAY_RATE
        else:
            return 0

    def fortify(self):
        self.fortification_step += 1
        return FORTRESS_FORTIFY_PAY_RATE


class Army:

    def __init__(self, size):
        self.size = size

    def payday(self):
        return self.size * random.randint(1, ARMY_PAY_DICE)


class State:

    def __init__(self, cities=None, fortifications=None, armies=None, money=STATE_INITIAL_MONEY):
        if armies is None:
            armies = list()
        if fortifications is None:
            fortifications = list()
        if cities is None:
            cities = list()
        self.cities = cities
        self.fortifications = fortifications
        self.armies = armies
        self.money = money

    def add_city(self, city):
        self.cities.append(city)

    def add_fortification(self, fortification):
        self.fortifications.append(fortification)

    def add_army(self, army):
        self.armies.append(army)

    def payday(self):
        for army in self.armies:
            self.money -= army.payday()
        for fortification in self.fortifications:
            self.money -= fortification.payday()

    def generate_profit(self):
        for city in self.cities:
            self.money += city.generate_profit()


class PlayerState(State):

    def input_commands(self):
        while True:
            command = input()
            if command == "end":
                break
            elif command == "info":
                print(f"State money: {self.money}")


class NeutralState(State):
    pass


class ComputerState(State):
    pass


class World:

    def __init__(self, states):
        self.states = states

    def next_day(self):
        for state in self.states:
            if isinstance(state, PlayerState):
                state.generate_profit()
                state.payday()
                state.input_commands()
            elif isinstance(state, ComputerState):
                pass

    def start_game(self):
        while True:
            self.next_day()

# 1 economy +-

# 2 battle +-

