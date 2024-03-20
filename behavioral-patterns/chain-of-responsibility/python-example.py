from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler) -> None:
        pass

    @abstractmethod
    def handle(self, request) -> None:
        pass


class ConcreteHandler(Handler):
    def __init__(self, name) -> None:
        self._name = name
        self._next_handler = None

    def set_next(self, handler: Handler) -> None:
        self._next_handler = handler

    def handle(self, request: str) -> None:
        if request == self._name:
            print(f"{self._name} handled the request")
        elif self._next_handler is not None:
            print(f"{self._name} passed the request to {self._next_handler._name}")
            self._next_handler.handle(request)
        else:
            print(f"{self._name} could not handle the request")


if __name__ == "__main__":
    handler1 = ConcreteHandler("Handler 1")
    handler2 = ConcreteHandler("Handler 2")
    handler3 = ConcreteHandler("Handler 3")

    handler1.set_next(handler2)
    handler2.set_next(handler3)

    handler1.handle("Handler 3")
    handler1.handle("Handler 1")
    handler1.handle("Handler 2")
    handler1.handle("Handler 4")
