from abc import ABC, abstractmethod
import os


# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> str:
        pass


# Concrete Products
class WinButton(Button):
    def paint(self) -> str:
        return "Windows Button"


class MacButton(Button):
    def paint(self) -> str:
        return "Mac Button"


class WinCheckbox(Checkbox):
    def paint(self) -> str:
        return "Windows Checkbox"


class MacCheckbox(Checkbox):
    def paint(self) -> str:
        return "Mac Checkbox"


# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# Concrete Factories
class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# Client
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        print(self.button.paint())
        print(self.checkbox.paint())


if __name__ == "__main__":
    if os.name == "nt":
        factory = WinFactory()
    elif os.name == "posix":
        factory = MacFactory()
    else:
        raise ValueError("Unknown OS")

    app = Application(factory)
    app.create_ui()
    app.paint()
