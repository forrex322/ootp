from copy import copy


class Prototype:
    __slots__ = ("_type", "_value")

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        return self._value

    def clone(self):
        raise NotImplementedError()


class Bicycle(Prototype):
    def __init__(self, wheels_quantity):
        self._type = self.__class__.__name__
        self._value = wheels_quantity

    def clone(self):
        return copy(x=self)


class Car(Prototype):
    def __init__(self, wheels_quantity):
        self._type = self.__class__.__name__
        self._value = wheels_quantity

    def clone(self):
        return copy(x=self)


class VehicleFactory:
    def __init__(self):
        self.__bicycle = Bicycle(wheels_quantity=2)
        self.__car = Car(wheels_quantity=4)

    def get_bicycle(self):
        return self.__bicycle.clone()

    def get_car(self):
        return self.__car.clone()


if __name__ == "__main__":
    vehicle_factory = VehicleFactory()

    bicycle = vehicle_factory.get_bicycle()
    print("Instance 1 type = " + bicycle.type + ", value = " + str(bicycle.value))

    car = vehicle_factory.get_car()
    print("Instance 2 type = " + car.type + ", value = " + str(car.value))
