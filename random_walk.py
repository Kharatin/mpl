from random import choice

class RandomWalk:
    """ Класс который генерирует случайные блуждания. """

    def __init__(self, num_points=5000):
        """ Инициировать атрибуты блуждания. """
        self.num_points = num_points

        # Все блуждания начинаются с (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Вычислить все точки блуждания. """

        # Продолжать делать шаги пока блуждание не достигнет определённой
        # длины.
        while len(self.x_values) < self.num_points:

            # Решить в каком направлении двигатся и как долго
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Откинуть шаги которые никуда не двигаются.
            if x_step == 0 and y_step == 0:
                continue

            # Расчитать новую позицию.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)




