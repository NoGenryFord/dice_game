class Player:
    __name: str
    __score: int
    __turn: int

    def __init__(self, name: str = "Default User") -> None:
        self.__name = name

    def __str__(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name


if __name__ == "__main__":
    player = Player("Alice")
    print(player)  # Output: Alice
