from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, r: float):
        if type(r) != float and type(r) != int: raise TypeError("Радиус может быть представлен только числом")
        if r <= 0:
            raise ValueError("Радиус должен быть больше 0")
        self.r = r

    @property
    def perimeter(self) -> float:
        return round(2 * math.pi * self.r, 2)

    @property
    def area(self) -> float:
        return round(math.pi * (self.r**2), 2)

    @property
    def info(self):
        print(f"r = {self.r}")
