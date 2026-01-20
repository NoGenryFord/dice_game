from textual import on
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import ScrollableContainer, Container
from textual.screen import Screen


class ScoreScreen(Screen):
    """Screen to display scores."""

    CSS_PATH = "../styles/score_screen.tcss"

    @on(Button.Pressed, "#back-btn")
    def handle_back_button(self) -> None:
        self.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("Scores Table", id="scores-header"),
            ScrollableContainer(id="scores-table"),
            Button("Back to Main Menu", id="back-btn", variant="primary"),
            id="score-container",
        )
        yield Footer()
