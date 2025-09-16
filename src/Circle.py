from Figure import Figure

class Circle(Figure):
    def __init__(self, r: float) -> float:
        if r <= 0: raise ValueError("Радиус должен быть больше 0")
        self.r = r

    @property
    def info(self):
        print(f'r = {self.r}')


