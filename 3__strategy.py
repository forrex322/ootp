import abc
from math import pi


class ShapeStrategy(abc.ABC):
    __slots__ = ("_type",)

    @abc.abstractmethod
    def calculate_area(self, data):
        raise NotImplementedError()

    @property
    def type(self):
        return self._type


class CircleStrategy(ShapeStrategy):
    __slots__ = ("_type",)

    def __init__(self):
        self._type = "Circle"

    def calculate_area(self, data):
        print(f"The area of the {self.type} is equal to: {pi * data.get('radius', 0.0)}")


class SquareStrategy(ShapeStrategy):
    __slots__ = ("_type",)

    def __init__(self):
        self._type = "Square"

    def calculate_area(self, data):
        print(f"The area of the {self.type} is equal to: {data.get('side', 0.0) ** 2}")


class ShapeHelper:
    __slots__ = ("_strategy", "shape")

    def __init__(self, type_):
        self._strategy = self._get_strategy(type_=type_)

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, type_):
        self._strategy = self._get_strategy(type_=type_)

    def _get_strategy(self, type_):
        if type_ == "Circle":
            return CircleStrategy()
        elif type_ == "Square":
            return SquareStrategy()
        else:
            raise NotImplementedError()

    def calculate_area(self, data):
        self.strategy.calculate_area(data=data)


if __name__ == "__main__":
    shape_helper = ShapeHelper(type_="Circle")
    shape_helper.calculate_area(data={"radius": 5.25})

    shape_helper.strategy = "Square"
    shape_helper.calculate_area(data={"side": 4.75})
