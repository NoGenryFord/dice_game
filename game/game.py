from datetime import datetime
from dataclasses import dataclass

from .models import LivePlayer, ComputerPlayer
from .score import FileController


@dataclass
class RoundState:
    round: int
    player_roll: int
    computer_roll: int
    player_score: int
    computer_score: int
    round_winner: str | None


class Game:
    __round: int
    __rounds_limit: int

    def __init__(self, rounds_limit: int = 5):
        self.__round = 0
        self.__rounds_limit = rounds_limit
        self.live_player = LivePlayer()
        self.computer_player = ComputerPlayer()

    def roll_round(self) -> RoundState:
        self.round += 1
        self.live_player.roll_dice()
        self.computer_player.roll_dice()

        if self.live_player.last_roll > self.computer_player.last_roll:
            self.live_player.game_score += (
                self.live_player.last_roll - self.computer_player.last_roll
            )
            winner = "player"
        elif self.live_player.last_roll < self.computer_player.last_roll:
            self.live_player.game_score += (
                self.live_player.last_roll - self.computer_player.last_roll
            )
            winner = "computer"
        else:
            winner = None

        return RoundState(
            round=self.round,
            player_roll=self.live_player.last_roll,
            computer_roll=self.computer_player.last_roll,
            player_score=self.live_player.game_score,
            computer_score=self.computer_player.game_score,
            round_winner=winner,
        )

    def is_finished(self) -> bool:
        return self.round >= self.__rounds_limit

    def final_winner(self) -> str | None:
        if self.live_player.game_score > self.computer_player.game_score:
            return "player"
        elif self.live_player.game_score < self.computer_player.game_score:
            return "computer"
        else:
            return None

    def save_result(self):
        fc = FileController()
        fc.save_result(
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            player=self.live_player.name,
            rounds=self.round,
            score=self.live_player.game_score,
        )


def main():
    state = RoundState(
        round=0,
        player_roll=0,
        computer_roll=0,
        player_score=0,
        computer_score=0,
        round_winner=None,
    )
    print(state)


if __name__ == "__main__":
    main()
