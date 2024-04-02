import abc


class Car(metaclass=abc.ABCMeta):
    __slots__ = ("_model",)

    @property
    def model(self):
        return self._model

    @abc.abstractmethod
    def detail(self):
        raise NotImplementedError


class Mustang(Car):
    def __init__(self):
        self._model = "Shelby GT500"

    def detail(self):
        print(f"Model of {self.__class__.__name__} is {self.model}")


class BMW(Car):
    def __init__(self):
        self._model = "X7"

    def detail(self):
        print(f"Model of {self.__class__.__name__} is {self.model}")


class Audi(Car):
    def __init__(self):
        self._model = "RS7"

    def detail(self):
        print(f"Model of {self.__class__.__name__} is: {self.model}")


class CarFactory:
    @staticmethod
    def create(model_name):
        if model_name == "Mustang":
            return Mustang()
        elif model_name == "BMW":
            return BMW()
        elif model_name == "Audi":
            return Audi()
        else:
            raise Exception("The car with that name does not exist.")


if __name__ == "__main__":
    for car_model in ("Mustang", "BMW", "Audi"):
        car = CarFactory.create(model_name=car_model)
        car.detail()
