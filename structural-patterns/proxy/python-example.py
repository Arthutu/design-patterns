from abc import ABC, abstractmethod


class ServiceInterface(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class Service(ServiceInterface):
    def request(self) -> None:
        print("Service: Handling request.")


class Proxy(ServiceInterface):
    def __init__(self, service: Service) -> None:
        self._service = service

    def request(self) -> None:
        if self.check_access():
            self._service.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


if __name__ == "__main__":
    service = Service()
    proxy = Proxy(service)

    # Client interacts with the Proxy
    proxy.request()
