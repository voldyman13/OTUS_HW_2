import math

from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a >= b + c or b >= c + a or c >= a + b:
            raise ValueError("Передан неправильный класс")
        self.name = "Треугольник"
        self.perimeter = a + b + c
        p = self.perimeter / 2
        self.area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        super().__init__(self.name, self.area, self.perimeter)
