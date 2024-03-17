class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


# Client Code
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(f"Are s1 and s2 the same object? {s1 == s2}")
