import math


class Figure:
    base_figs_perimeters = {
        'Square': lambda *sides: 4 * sides[0],
        'Rectangle': lambda *sides: 2 * (sides[1] + sides[b]),
        'Triangle': lambda a, b, c: a + b + c,
        'Circle': lambda r: r * math.pi * 2
    }
    
    base_figs_areas = {
        'Square': lambda *sides: sides[0] ** 2,
        'Rectangle': lambda *sides: sides[0] * sides[1],
        'Triangle': lambda a, b, c: ((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c)) ** (1/4),
        'Circle': lambda r: math.pi * (r ** 2)
    }
    
    def get_perimeter(self) -> float:
        for i in self.base_figs_perimeters:
            if i == self._get_class_name(): return self.base_figs_perimeters[i](self.a, self.b, self.c)

    def get_square(self) -> float:
        for i in self.base_figs_areas:
            if i == self._get_class_name(): return self.base_figs_areas[i](self.a, self.b=None, self.c=None)
 
    def _get_class_name(self) -> str:
        return self.__class__.__name__
