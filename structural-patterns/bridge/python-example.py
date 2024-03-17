from abc import ABC, abstractmethod


# Implementor Interface
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float) -> None:
        pass


# Concrete Implementor A
class VectorRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"Drawing a circle of radius {radius} using VectorRenderer"


# Concrete Implementor B
class RasterRenderer(Renderer):
    def render_circle(self, radius: float) -> str:
        return f"Drawing a circle of radius {radius} using RasterRenderer"


# Abstraction
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        pass


# Refined Abstraction
class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> str:
        return self.renderer.render_circle(self.radius)


if __name__ == "__main__":
    circle = Circle(VectorRenderer(), 5)
    print(circle.draw())

    circle = Circle(RasterRenderer(), 10)
    print(circle.draw())
