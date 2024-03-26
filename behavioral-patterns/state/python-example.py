from abc import ABC, abstractmethod
from typing import Optional


class State(ABC):
    @abstractmethod
    def handle(self) -> None:
        pass


class Context(ABC):
    def __init__(self):
        self._state: Optional[State] = None

    @property
    def state(self) -> Optional[State]:
        return self._state

    @state.setter
    def state(self, state: State) -> None:
        self._state = state

    def request(self) -> None:
        self._state.handle()


class ConcreteStateA(State):
    def handle(self) -> None:
        print("Handling request in State A")


class ConcreteStateB(State):
    def handle(self) -> None:
        print("Handling request in State B")


if __name__ == "__main__":
    context = Context()

    state_a = ConcreteStateA()
    context.state = state_a
    context.request()

    state_b = ConcreteStateB()
    context.state = state_b
    context.request()
