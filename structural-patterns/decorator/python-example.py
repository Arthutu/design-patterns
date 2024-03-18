from abc import ABC, abstractmethod


# Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 1.0

    def description(self) -> str:
        return "Simple Coffee"


# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()


# Concrete Decorators
class Milk(CoffeeDecorator):
    def __init__(self, coffee: Coffee):
        super().__init__(coffee)

    def cost(self) -> float:
        return super().cost() + 0.5

    def description(self) -> str:
        return super().description() + ", Milk"


class Sugar(CoffeeDecorator):
    def __init__(self, coffee: Coffee):
        super().__init__(coffee)

    def cost(self) -> float:
        return super().cost() + 0.7

    def description(self) -> str:
        return super().description() + ", Sugar"


if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"{coffee.description()}: ${coffee.cost()}")

    coffee_with_milk = Milk(coffee)
    print(f"{coffee_with_milk.description()}: ${coffee_with_milk.cost()}")

    coffee_with_sugar = Sugar(coffee_with_milk)
    print(f"{coffee_with_sugar.description()}: ${coffee_with_sugar.cost()}")
