import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Передан неправильный класс")
        self.name = "Круг"
        pi = math.pi
        self.perimeter = 2 * pi * r
        self.area = pi * r ** 2
        super().__init__(self.name, self.area, self.perimeter)
