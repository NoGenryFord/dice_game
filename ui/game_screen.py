from textual import on
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.screen import Screen
from textual.containers import Container, ScrollableContainer
from textual.reactive import reactive

from game.game import Game, RoundState


class GameScreen(Screen):
    """Screen to display game."""

    CSS_PATH = "../styles/game_screen.tcss"

    round_state: reactive[RoundState] = reactive(
        RoundState(
            round=0,
            player_roll=0,
            computer_roll=0,
            player_score=0,
            computer_score=0,
            round_winner=None,
        )
    )

    def on_mount(self) -> None:
        self.game = Game(rounds_limit=5)

    @on(Button.Pressed, "#back-btn")
    def handle_back_button(self) -> None:
        self.app.pop_screen()

    @on(Button.Pressed, "#roll-btn")
    def handle_roll_button(self) -> None:
        if not self.game.is_finished():
            self.round_state = self.game.roll_round()
        if self.game.is_finished():
            # save result when game finishes
            try:
                self.game.save_result()
            except Exception:
                pass
            final_winner = self.game.final_winner()
            if final_winner:
                winner_text = (
                    "Player wins!" if final_winner == "player" else "Computer wins!"
                )
            else:
                winner_text = "It's a tie!"

            self.show_game_over(winner_text)

    def show_game_over(self, winner_text: str) -> None:
        """Update current screen to display final results."""
        self.query_one("#roll-btn", Button).disabled = True

        try:
            self.query_one("#game-header", Static).update("Game Over!")
        except Exception:
            pass

        self.query_one("#round-number", Static).update(f"Rounds: {self.game.rounds}")
        self.query_one("#player-roll", Static).update(
            f"Player Score: {self.game.live_player.game_score}"
        )
        self.query_one("#computer-roll", Static).update(
            f"Computer Score: {self.game.computer_player.game_score}"
        )
        self.query_one("#player-score", Static).update(winner_text)
        self.query_one("#round-winner", Static).update("-")

    def watch_round_state(self, old, new) -> None:
        self.query_one("#round-number", Static).update(f"Round: {new.round}")
        self.query_one("#player-roll", Static).update(f"Player Roll: {new.player_roll}")
        self.query_one("#computer-roll", Static).update(
            f"Computer Roll: {new.computer_roll}"
        )
        self.query_one("#player-score", Static).update(
            f"Player Score: {new.player_score}"
        )
        # self.query_one("#computer-score", Static).update(
        #     f"Computer Score: {new.computer_score}"
        # )
        self.query_one("#round-winner", Static).update(
            f"Round Winner: {new.round_winner or 'Tie'}"
        )

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("Game", id="game-header"),
            Container(
                Static("Round: 0", id="round-number"),
                Static("Player Roll: 0", id="player-roll"),
                Static("Computer Roll: 0", id="computer-roll"),
                Static("Player Score: 0", id="player-score"),
                # Static("Computer Score: 0", id="computer-score"),
                Static("Round Winner: -", id="round-winner"),
                id="game-stats-container",
            ),
            Button("Roll Dice", id="roll-btn", variant="primary"),
            Button("Exit to Main Menu", id="back-btn", variant="primary"),
        )

        yield Footer()
