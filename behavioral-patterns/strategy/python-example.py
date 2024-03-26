from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class ConcreteStrategyA(Strategy):
    def execute(self) -> None:
        print("Executing strategy A")


class ConcreteStrategyB(Strategy):
    def execute(self) -> None:
        print("Executing strategy B")


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self) -> None:
        self.strategy.execute()


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    context.execute_strategy()

    context.strategy = ConcreteStrategyB()
    context.execute_strategy()
