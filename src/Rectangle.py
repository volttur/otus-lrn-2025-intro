from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float) -> float:
        if a <= 0 or b <= 0:
            raise ValueError("Каждая из сторон должна быть больше 0")
        self.a = a
        self.b = b

    @property
    def info(self):
        print(f"a = {self.a}, b = {self.b}")
