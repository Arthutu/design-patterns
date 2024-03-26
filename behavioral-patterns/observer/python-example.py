from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)


class ConcreteObserver(Observer):
    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, message: str) -> None:
        print(f"{self._name} received message: {message}")


if __name__ == "__main__":
    subject = Subject()
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    subject.attach(observer1)
    subject.attach(observer2)

    subject.notify("Hello from the subject!")
