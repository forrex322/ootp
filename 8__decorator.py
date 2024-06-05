from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod 
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Проста кава"

class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee):
        self._decorated_coffee = decorated_coffee

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._decorated_coffee.cost() + 2

    def description(self):
        return self._decorated_coffee.description() + ", молоко"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._decorated_coffee.cost() + 1

    def description(self):
        return self._decorated_coffee.description() + ", цукор"

class VanillaDecorator(CoffeeDecorator):
    def cost(self):
        return self._decorated_coffee.cost() + 3

    def description(self):
        return self._decorated_coffee.description() + ", ваніль"

coffee = SimpleCoffee()
print(f"{coffee.description()} коштує {coffee.cost()} грн")

coffee = MilkDecorator(coffee)
print(f"{coffee.description()} коштує {coffee.cost()} грн")

coffee = SugarDecorator(coffee)
print(f"{coffee.description()} коштує {coffee.cost()} грн")

coffee = VanillaDecorator(coffee)
print(f"{coffee.description()} коштує {coffee.cost()} грн")
