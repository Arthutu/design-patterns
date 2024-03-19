class SubsystemA:
    def operation_1(self) -> str:
        return "SubsystemA: Ready!"

    def operation_n(self) -> str:
        return "SubsystemA: Go!"


class SubsystemB:
    def operation_1(self) -> str:
        return "SubsystemB: Fire!"

    def operation_n(self) -> str:
        return "SubsystemB: Boom!"


class Facade:
    def __init__(self, subsystem_a: SubsystemA, subsystem_b: SubsystemB) -> None:
        self._subsystem_a = subsystem_a
        self._subsystem_b = subsystem_b

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem_a.operation_1())
        results.append(self._subsystem_b.operation_1())
        results.append("Facade triggers operations:")
        results.append(self._subsystem_a.operation_n())
        results.append(self._subsystem_b.operation_n())
        return "\n".join(results)


if __name__ == "__main__":
    subsystem_a = SubsystemA()
    subsystem_b = SubsystemB()
    facade = Facade(subsystem_a, subsystem_b)
    print(facade.operation())
