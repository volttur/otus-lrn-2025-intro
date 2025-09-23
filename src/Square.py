from src.Figure import Figure


class Square(Figure):
    def __init__(self, a: float) -> float:
        if type(a) is not float and type(a) is not int:
            raise TypeError("Сторона может быть представлена только числом")
        if a <= 0:
            raise ValueError("Сторона должна быть больше чем 0")
        self.a = a

    @property
    def perimeter(self) -> float:
        return round(4 * self.a, 2)

    @property
    def area(self) -> float:
        return round(self.a**2, 2)

    @property
    def info(self):
        print(f"a = {self.a}")
