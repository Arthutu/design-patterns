from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: "Colleague", event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        self._colleagues = []

    def add_colleague(self, colleague: "Colleague") -> None:
        self._colleagues.append(colleague)

    def notify(self, sender: "Colleague", event: str) -> None:
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(event)


class Colleague(ABC):
    def __init__(self, mediator: Mediator):
        self._mediator = mediator

    def send(self, event: str) -> None:
        print(f"Sending event: {event}")
        self._mediator.notify(self, event)

    @abstractmethod
    def receive(self, event: str) -> None:
        pass


class ConcreteColleague(Colleague):
    def receive(self, event: str) -> None:
        print(f"Received event: {event}")


if __name__ == "__main__":
    mediator = ConcreteMediator()
    colleague1 = ConcreteColleague(mediator)
    colleague2 = ConcreteColleague(mediator)

    mediator.add_colleague(colleague1)
    mediator.add_colleague(colleague2)

    colleague1.send("Hello from colleague 1")
    colleague2.send("Hello from colleague 2")
