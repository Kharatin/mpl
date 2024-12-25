from random import randint

class Die:
    """ Класс представляет один кубик. """

    def __init__(self, num_sides=6):
        """ пределить кубик с шестью гранями. """
        self.num_sides = num_sides

    def roll(self):
        """ Вернуть случайное значение от 1 до 6. """
        return  randint(1, self.num_sides)