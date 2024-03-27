from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element: "ConcreteElementA") -> None:
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element: "ConcreteElementB") -> None:
        pass


# ConcreteVisitor
class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element: "ConcreteElementA") -> None:
        print("ConcreteVisitor visits ConcreteElementA")

    def visit_concrete_element_b(self, element: "ConcreteElementB") -> None:
        print("ConcreteVisitor visits ConcreteElementB")


class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteElementA(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_element_a(self)


class ConcreteElementB(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_element_b(self)


class ObjectStructure:
    def __init__(self) -> None:
        self._elements = []

    def attach(self, element: Element) -> None:
        self._elements.append(element)

    def detach(self, element: Element) -> None:
        self._elements.remove(element)

    def accept(self, visitor: Visitor) -> None:
        for element in self._elements:
            element.accept(visitor)


if __name__ == "__main__":
    concrete_element_a = ConcreteElementA()
    concrete_element_b = ConcreteElementB()

    object_structure = ObjectStructure()
    object_structure.attach(concrete_element_a)
    object_structure.attach(concrete_element_b)

    concrete_visitor = ConcreteVisitor()
    object_structure.accept(concrete_visitor)
