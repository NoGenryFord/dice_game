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

    def _on_mount(self) -> None:

        self.game = Game(rounds_limit=5)

    @on(Button.Pressed, "#back-btn")
    def handle_back_button(self) -> None:
        self.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("Game", id="game-header"),
            Container(
                Static(f"Round: {self.round_state.round}", id="round-number"),
                Static(
                    f"Player Roll: {self.round_state.player_roll}", id="player-roll"
                ),
                Static(
                    f"Computer Roll: {self.round_state.computer_roll}",
                    id="computer-roll",
                ),
                Static(
                    f"Player Score: {self.round_state.player_score}",
                    id="player-score",
                ),
                Static(
                    f"Computer Score: {self.round_state.computer_score}",
                    id="computer-score",
                ),
                Static(
                    f"Round Winner: {self.round_state.round_winner or 'Tie'}",
                    id="round-winner",
                ),
                id="game-stats-container",
            ),
            Button("Roll Dice", id="roll-btn", variant="primary"),
            Button("Exit to Main Menu", id="back-btn", variant="primary"),
        )

        yield Footer()
