from typing import Any


class Memento:
    def __init__(self, state: Any) -> None:
        self._state = state

    def get_state(self) -> Any:
        return self._state


class Originator:
    def __init__(self, state: Any) -> None:
        self._state = state

    def create_memento(self) -> Memento:
        return Memento(self._state)

    def restore_from_memento(self, memento: Memento) -> None:
        self._state = memento.get_state()


class Caretaker:
    def __init__(self) -> None:
        self._mementos = []

    def add_memento(self, memento: Memento) -> None:
        self._mementos.append(memento)

    def get_memento(self, index: int) -> Memento:
        return self._mementos[index]


if __name__ == "__main__":
    # Originator creates and restores its state using mementos
    originator = Originator("State 1")
    caretaker = Caretaker()
    caretaker.add_memento(originator.create_memento())

    originator.restore_from_memento(caretaker.get_memento(0))
    print(f"Restored state: {originator._state}")
