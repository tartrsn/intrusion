import random

from constants import REGULAR_CITY_PROFIT, BIT_CITY_PROFIT, CITY_PROFIT_DICE, ARMY_PAY_DICE, FORTRESS_PAY_RATE, \
    FORTRESS_FORTIFY_PAY_RATE


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
    pass

# 1 economy +-

# 2 battle +-

