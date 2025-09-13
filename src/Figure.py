class Figure:
    def get_area(a: float, b: float = 1) -> float:
        return a * b if a > 0 and b > 0

    def get_perimeter(a: float, b: float = 0) -> float:
        return (a + b) * 2
