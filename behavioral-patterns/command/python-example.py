from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class Receiver:
    def action(self) -> None:
        print("Receiver is doing something")


class ConcreteCommand(Command):
    def __init__(self, receiver: Receiver) -> None:
        self._receiver = receiver

    def execute(self) -> None:
        self._receiver.action()


class Invoker:
    def __init__(self) -> None:
        self._command = None

    def set_command(self, command: Command) -> None:
        self._command = command

    def execute_command(self) -> None:
        if self._command is not None:
            print("Invoker: Asking command to carry out the request")
            self._command.execute()


if __name__ == "__main__":
    receiver = Receiver()
    command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.set_command(command)
    invoker.execute_command()
