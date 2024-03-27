from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operation()
        self.base_operation2()
        self.hook()
        self.base_operation3()

    def base_operation1(self) -> None:
        print("Abstract says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("Abstract says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("Abstract says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operation(self) -> None:
        pass

    def hook(self) -> None:
        pass


class ConcreteClassA(AbstractClass):
    def required_operation(self) -> None:
        print("ConcreteClassA: Executing required operation 1")


class ConcreteClassB(AbstractClass):
    def required_operation(self) -> None:
        print("ConcreteClassB: Executing required operation 1")

    def hook(self) -> None:
        print("ConcreteClassB: Executing hook operation")


if __name__ == "__main__":
    print("Using ConcreteClassA:")
    concrete_class_a = ConcreteClassA()
    concrete_class_a.template_method()

    print("\nUsing ConcreteClassB:")
    concrete_class_b = ConcreteClassB()
    concrete_class_b.template_method()
