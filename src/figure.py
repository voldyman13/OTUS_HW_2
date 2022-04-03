class Figure:
    def __init__(self, name, area, perimeter):
        assert name in ["Треугольник", "Прямоугольник", "Квадрат", "Круг"]
        self.name = name
        self.perimeter = perimeter
        self.area = area

    def add_area(self, figure):
        return self.area + figure.area
