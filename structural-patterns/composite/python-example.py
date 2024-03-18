from abc import ABC, abstractmethod
from typing import List


# Component Interface
class Graphic(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass


# Leaf
class Line(Graphic):
    def draw(self) -> None:
        print("Drawing a line")


# Composite
class Picture(Graphic):
    def __init__(self) -> None:
        self.graphics: List[Graphic] = []

    def draw(self) -> None:
        print("Drawing a picture")
        for graphic in self.graphics:
            graphic.draw()

    def add(self, graphic: Graphic) -> None:
        self.graphics.append(graphic)

    def remove(self, graphic: Graphic) -> None:
        self.graphics.remove(graphic)


if __name__ == "__main__":
    line1 = Line()
    line2 = Line()
    line3 = Line()

    picture = Picture()
    picture.add(line1)
    picture.add(line2)
    picture.add(line3)

    picture.draw()
