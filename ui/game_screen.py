from textual import on
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.screen import Screen


class GameScreen(Screen):
    """Screen to display game."""

    CSS_PATH = "../styles/main.tcss"

    @on(Button.Pressed, "#back-btn")
    def handle_back_button(self) -> None:
        self.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("Game will be displayed here.", id="game-message")
        yield Button("Back to Main Menu", id="back-btn", variant="primary")
        yield Footer()
