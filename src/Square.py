from Figure import Figure

class Square(Figure):
    def __init__(self, a: float) -> float:
        if a <= 0: raise ValueError("Сторона должна быть больше чем 0")
        self.a = a

    @property
    def info(self):
        print(f'a = {self.a}')


