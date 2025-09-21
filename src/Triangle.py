from Figure import Figure


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float) -> float:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Сторона должна быть больше 0")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("По данным сторонам треугольник невозможно построить")
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self) -> float:
        return round(self.a + self.b + self.c, 2)

    @property
    def area(self) -> float:
        return round(
            (
                (self.a + self.b + self.c)
                * (self.b + self.c - self.a)
                * (self.a + self.c - self.b)
                * (self.a + self.b - self.c)
            )
            ** (1 / 4),
            2,
        )

    @property
    def info(self):
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")
