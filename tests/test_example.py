import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.smoke
def test_triangle_name():
    triangle = Triangle(2, 3, 4)
    assert triangle.name == "Треугольник"


@pytest.mark.smoke
def test_triangle_perimeter():
    triangle = Triangle(2, 2, 2)
    assert triangle.perimeter == 6


@pytest.mark.smoke
def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert triangle.area == 6


@pytest.mark.smoke
@pytest.mark.parametrize("figure", [pytest.param(Circle(5), id="Circle"),
                                    pytest.param(Square(2), id="Square"),
                                    pytest.param(Rectangle(3, 3), id="Rectangle"),
                                    pytest.param(Triangle(3, 4, 5), id="Triangle")])
def test_triangle_add_area(figure):
    triangle = Triangle(5, 6, 4)
    assert triangle.add_area(figure) == triangle.area + figure.area


@pytest.mark.regress
@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize("a, b, c", [pytest.param(0, 4, 5, id="a=0"),
                                     pytest.param(3, 0, 5, id="b=0"),
                                     pytest.param(3, 4, 0, id="c=0"),
                                     pytest.param(3, 4, 7, id="a+b=c"),
                                     pytest.param(-3, 2, 9, id="a<0"),
                                     pytest.param(3, -2, 9, id="b<0"),
                                     pytest.param(3, 2, -9, id="c<0"),
                                     pytest.param(3, 1, 1, id="a<b+c")])
def test_triangle_negative(a, b, c):
    Triangle(a, b, c)


@pytest.mark.smoke
def test_square_name():
    square = Square(2)
    assert square.name == "Квадрат"


@pytest.mark.smoke
def test_square_perimeter():
    square = Square(2)
    assert square.perimeter == 8


@pytest.mark.smoke
def test_square_area():
    square = Square(3)
    assert square.area == 9


@pytest.mark.smoke
@pytest.mark.parametrize("figure", [pytest.param(Circle(5), id="Circle"),
                                    pytest.param(Square(2), id="Square"),
                                    pytest.param(Rectangle(3, 3), id="Rectangle"),
                                    pytest.param(Triangle(3, 4, 5), id="Triangle")])
def test_square_add_area(figure):
    square = Square(5)
    assert square.add_area(figure) == square.area + figure.area


@pytest.mark.regress
@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize("a", [pytest.param(0, id="a=0"),
                               pytest.param(-1, id="a=-1")])
def test_square_negative(a):
    Square(a)


@pytest.mark.smoke
def test_rectangle_name():
    rectangle = Rectangle(1, 2)
    assert rectangle.name == "Прямоугольник"


@pytest.mark.smoke
def test_rectangle_perimeter():
    rectangle = Rectangle(2, 3)
    assert rectangle.perimeter == 10


@pytest.mark.smoke
def test_rectangle_area():
    rectangle = Rectangle(3, 3)
    assert rectangle.area == 9


@pytest.mark.smoke
@pytest.mark.parametrize("figure", [pytest.param(Circle(5), id="Circle"),
                                    pytest.param(Square(2), id="Square"),
                                    pytest.param(Rectangle(3, 3), id="Rectangle"),
                                    pytest.param(Triangle(3, 4, 5), id="Triangle")])
def test_rectangle_add_area(figure):
    rectangle = Rectangle(5, 2)
    assert rectangle.add_area(figure) == rectangle.area + figure.area


@pytest.mark.regress
@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize("a, b", [pytest.param(0, 4, id="a=0"),
                                  pytest.param(3, 0, id="b=0"),
                                  pytest.param(-1, 4, id="a<0"),
                                  pytest.param(3, -1, id="b<0")])
def test_rectangle_negative(a, b):
    Rectangle(a, b)


@pytest.mark.smoke
def test_circle_name():
    circle = Circle(2)
    assert circle.name == "Круг"


@pytest.mark.smoke
def test_circle_perimeter():
    circle = Circle(2)
    assert round(circle.perimeter, 2) == 12.57


@pytest.mark.smoke
def test_circle_area():
    circle = Circle(10)
    assert round(circle.area, 2) == 314.16


@pytest.mark.smoke
@pytest.mark.parametrize("figure", [pytest.param(Circle(5), id="Circle"),
                                    pytest.param(Square(2), id="Square"),
                                    pytest.param(Rectangle(3, 3), id="Rectangle"),
                                    pytest.param(Triangle(3, 4, 5), id="Triangle")])
def test_circle_add_area(figure):
    circle = Circle(10)
    assert circle.add_area(figure) == circle.area + figure.area


@pytest.mark.regress
@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize("r", [pytest.param(0, id="r=0"),
                               pytest.param(-1, id="r<0")])
def test_circle_negative(r):
    Circle(r)


