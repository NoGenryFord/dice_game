import random


class Player:
    _last_roll: int = 0
    _game_score: int = 0

    def __init__(self): ...

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def roll_dice(self):
        self._last_roll = random.randint(1, 6)
        return self._last_roll

    @property
    def last_roll(self) -> int:
        return self._last_roll

    @property
    def game_score(self) -> int:
        return self._game_score

    @game_score.setter
    def game_score(self, value: int):
        self._game_score = value


class LivePlayer(Player):
    def __init__(self, name: str = "Player"):
        super().__init__()
        self._name = name


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self._name = "Computer"
