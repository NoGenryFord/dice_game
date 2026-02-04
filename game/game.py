from datetime import datetime

from models import LivePlayer, ComputerPlayer
from score import FileController


class Game:
    __round: int
    __rounds_limit: int

    def __init__(self):
        self.__round = 0

    @property
    def round(self) -> int:
        return self.__round

    @round.setter
    def round(self, value: int):
        self.__round = value

    def setup(self):
        self.live_player = LivePlayer()
        self.computer_player = ComputerPlayer()
        print(f"Welcome {self.live_player.name}!")
        print(f"You are playing against {self.computer_player.name}.")

    def set_round_winner(self):
        if self.live_player.last_roll > self.computer_player.last_roll:
            self.live_player.game_score += (
                self.live_player.last_roll - self.computer_player.last_roll
            )
            print(f"\n{self.live_player.name} wins this round!\n")
        elif self.live_player.last_roll < self.computer_player.last_roll:
            self.computer_player.game_score += (
                self.computer_player.last_roll - self.live_player.last_roll
            )
            print(f"\n{self.computer_player.name} wins this round!\n")
        else:
            print("\nThis round is a tie!\n")

    def game_proccess(self, rounds_limit: int = 5):

        self.setup()

        while True:
            self.round += 1
            print(f"Round {self.round} begins!")

            print(f"{self.live_player.name} is rolling the dice...")
            input("Press Enter to roll the dice...")
            self.live_player.roll_dice()
            print(
                f"\n {self.live_player.name} rolled a {self.live_player.last_roll}. \n"
            )

            print(f"{self.computer_player.name} is rolling the dice...")
            self.computer_player.roll_dice()
            print(
                f"\n {self.computer_player.name} rolled a {self.computer_player.last_roll}. \n"
            )
            self.set_round_winner()
            if self.round > rounds_limit - 1:
                print("Game over!")
                print(
                    f"Final Scores:\n{self.live_player.name}: {self.live_player.game_score}\n{self.computer_player.name}: {self.computer_player.game_score}\n"
                )
                if self.live_player.game_score > self.computer_player.game_score:
                    print(f"{self.live_player.name} wins the game!")
                elif self.live_player.game_score < self.computer_player.game_score:
                    print(f"{self.computer_player.name} wins the game!")

                # Save the game result
                fc = FileController()
                fc.save_result(
                    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    player=self.live_player.name,
                    rounds=self.round,
                    score=self.live_player.game_score,
                )

                input("Press Enter to exit...")
                break

            else:
                print(f"Preparing for round {self.round + 1}...")


def main():
    game = Game()
    game.game_proccess()


if __name__ == "__main__":
    main()
