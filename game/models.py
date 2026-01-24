class Player:
    def __init__(self, name: str = "Default User") -> None:
        self.name = name


if __name__ == "__main__":
    player = Player("Alice")
    print(player)  # Output: Alice
