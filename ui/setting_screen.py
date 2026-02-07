from textual import on
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Static, Button, DataTable
from textual.containers import ScrollableContainer, Container
from textual.screen import Screen

import json
import os


class SettingsScreen(Screen):
    """Screen to display game settings."""

    CSS_PATH = "../styles/settings_screen.tcss"

    @on(Button.Pressed, "#back-btn")
    def handle_back_button(self) -> None:
        self.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("Game Settings", id="settings-header"),
            ScrollableContainer(
                DataTable(id="settings-table"), id="settings-table-container"
            ),
            Button("Back to Main Menu", id="back-btn", variant="primary"),
            id="settings-container",
        )
        yield Footer()

    def on_mount(self) -> None:
        settings = self.read_settings()

        table = self.query_one(DataTable)
        table.add_columns("#", "Name", "Rounds")
        for i, setting in enumerate(settings, start=1):
            table.add_row(i, setting["name"], setting["rounds"])

    def read_settings(self):
        settings_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "..", "settings.json"
        )
        with open(settings_path, "r", encoding="utf-8") as file:
            return json.load(file)
