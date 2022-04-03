from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        if a == 0 or b == 0:
            raise ValueError("Передан неправильный класс")
        self.name = "Прямоугольник"
        self.perimeter = 2 * (a + b)
        self.area = a * b
        super().__init__(self.name, self.area, self.perimeter)
