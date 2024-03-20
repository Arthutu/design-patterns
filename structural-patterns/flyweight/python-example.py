from typing import Dict


class Flyweight:
    def __init__(self, intrinsic_state: int) -> None:
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state: int) -> None:
        print(
            f"Flyweight: Intrinsic state: {self._intrinsic_state}, Extrinsic state: {extrinsic_state}"
        )


class FlyweightFactory:
    _flyweights: Dict[int, Flyweight] = {}

    def get_flyweight(self, key: str) -> Flyweight:
        if key not in FlyweightFactory._flyweights:
            FlyweightFactory._flyweights[key] = Flyweight(key)

        return FlyweightFactory._flyweights[key]


if __name__ == "__main__":
    flyweight_factory = FlyweightFactory()
    flyweight1 = flyweight_factory.get_flyweight("shared")
    flyweight2 = flyweight_factory.get_flyweight("shared")

    flyweight1.operation("state1")
    flyweight2.operation("state2")
