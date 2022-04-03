from src.figure import Figure


class Square(Figure):
    def __init__(self, a):
        if a <= 0:
            raise ValueError("Передан неправильный класс")
        self.name = "Квадрат"
        self.perimeter = a * 4
        self.area = a ** 2
        super().__init__(self.name, self.area, self.perimeter)
