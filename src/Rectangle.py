from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float) -> float:
        if (type(a) is not float and type(a) is not int) or (
            type(b) is not float and type(b) is not int
        ):
            raise TypeError("Сторона может быть представлена только числом")
        if a <= 0 or b <= 0:
            raise ValueError("Каждая из сторон должна быть больше 0")
        self.a = a
        self.b = b

    @property
    def perimeter(self) -> float:
        return round(2 * (self.a + self.b), 2)

    @property
    def area(self) -> float:
        return round(self.a * self.b, 2)

    @property
    def info(self):
        print(f"a = {self.a}, b = {self.b}")
