from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


class ConcreteIterator(Iterator):
    def __init__(self, collection: list):
        self._collection = collection
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration()


class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._collection = []

    def add_item(self, item):
        self._collection.append(item)

    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self._collection)


if __name__ == "__main__":
    aggregate = ConcreteAggregate()
    aggregate.add_item("Item 1")
    aggregate.add_item("Item 2")
    aggregate.add_item("Item 3")

    iterator = aggregate.create_iterator()

    while iterator.has_next():
        print(iterator.next())
