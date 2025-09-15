from Figure import Figure

class Square(Figure):
    def __init__(self, a: float) -> float:
        self.a = a
        
    def info(self):
        print(f'a = {self.a}')
        
        
s = Square(5)
s.info()
print(s.get_perimeter())
print(s.get_square())
