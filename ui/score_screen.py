from textual import on
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Static, Button, DataTable
from textual.containers import ScrollableContainer, Container
from textual.screen import Screen


from game.score import FileController


class ScoreScreen(Screen):
    """Screen to display scores."""

    CSS_PATH = "../styles/score_screen.tcss"

    file_controller = FileController()
    score_parser = file_controller.read_results()

    @on(Button.Pressed, "#back-btn")
    def handle_back_button(self) -> None:
        self.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("Scores Table", id="scores-header"),
            ScrollableContainer(
                DataTable(id="scores-table"), id="scores-table-container"
            ),
            Button("Back to Main Menu", id="back-btn", variant="primary"),
            id="score-container",
        )
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("#", "Date", "Player", "Rounds", "Score")
        for i, row in enumerate(self.score_parser, start=1):
            table.add_row(i, *row)
