from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import ScrollableContainer


class MainMenu(Static):
    """Main menu widget."""

    @on(Button.Pressed, "#quit-btn")
    def handle_exit_button(self) -> None:
        self.app.exit()

    @on(Button.Pressed, "#view-scores-btn")
    def handle_view_scores_button(self) -> None: ...

    def compose(self) -> ComposeResult:
        yield Button("Start Game", id="start-game-btn", variant="primary")
        yield Button("View Scores", id="view-scores-btn", variant="primary")
        yield Button("Exit Game", id="quit-btn", variant="error")


class DiceGame(App):
    """A dice game application."""

    CSS_PATH = "./styles/main.tcss"

    BINDINGS = [("d", "toggle_dark", "Theme"), ("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield ScrollableContainer(
            Static("Welcome to the Dice Game!", id="welcome-message"),
            MainMenu(id="main-menu"),
        )
        yield Footer()


if __name__ == "__main__":
    app = DiceGame()
    app.run()
