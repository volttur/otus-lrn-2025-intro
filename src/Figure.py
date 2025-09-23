from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def info(self) -> str:
        pass

    def add_area(self, fig) -> float:
        if "Figure" in list(map(lambda el: el.__name__, fig.__class__.__mro__)):
            return round(self.area + fig.area, 2)
        else:
            raise TypeError("Функция должна принимать фигуру")
