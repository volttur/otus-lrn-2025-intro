import math


class Figure:
    __base_figs_perimeters = {
        'Square': lambda sides: 4 * sides[0],
        'Rectangle': lambda sides: 2 * (sides[1] + sides[0]),
        'Triangle': lambda sides: sides[0] + sides[1] + sides[2],
        'Circle': lambda sides: sides[0] * math.pi * 2
    }

    __base_figs_areas = {
        'Square': lambda sides: sides[0] ** 2,
        'Rectangle': lambda sides: sides[0] * sides[1],
        'Triangle': lambda sides: ((sides[0] + sides[1] + sides[2]) * (sides[1] + sides[2] - sides[0]) * (sides[0] + sides[2] - sides[1]) * (sides[0] + sides[1] - sides[2])) ** (1/4),
        'Circle': lambda sides: math.pi * (sides[0] ** 2)
    }

    @property
    def get_perimeter(self) -> float:
        for i in self.__base_figs_perimeters:
            if i == self._get_class_name(self): return self.__base_figs_perimeters[i](list(self.__dict__.values()))

    @property
    def get_area(self) -> float:
        for i in self.__base_figs_areas:
            if i == self._get_class_name(self): return self.__base_figs_areas[i](list(self.__dict__.values()))

    def _get_class_name(self, fig) -> str:
        return fig.__class__.__name__

    def add_area(self, fig) -> float:
        if 'Figure' in list(map(lambda el: el.__name__, fig.__class__.__mro__)):
            return self.get_area + fig.get_area
        else:
            raise ValueError("Функция должна принимать фигуру")

    def info(self) -> str:
        pass
