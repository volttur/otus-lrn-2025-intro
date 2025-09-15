from Figure import Figure

class Rectangle(Figure):
    def __init__(self, a: float, b: float) -> float:
        self.a = a
        self.b = b
        
    def info(self):
        print(f'a = {self.a}, b = {self.b}')
        
        
r = Rectangle(5, 10)
r.info()
print(r.get_perimeter())
print(r.get_square())
