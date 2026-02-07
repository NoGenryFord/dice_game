from textual import on
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Static, Button, DataTable, Input, Select
from textual.containers import ScrollableContainer, Container
from textual.screen import Screen

from game.settings import load_user_settings, save_user_settings

import json
import os


class SettingsScreen(Screen):
    """Screen to display game settings."""

    CSS_PATH = "../styles/settings_screen.tcss"

    @on(Button.Pressed, "#save-btn")
    def handle_save(self) -> None:
        name = self.query_one("#name-input", Input).value.strip()
        rounds = int(self.query_one("#rounds-select", Select).value)
        save_user_settings({"player_name": name or "Player", "rounds": rounds})

    @on(Button.Pressed, "#back-btn")
    def handle_back_button(self) -> None:
        self.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            Static("Game Settings", id="settings-header"),
            # ScrollableContainer(
            #     DataTable(id="settings-table"), id="settings-table-container"
            # ),
            Input(placeholder="Your name", id="name-input"),
            Select(
                options=[("Short (5)", "5"), ("Medium (8)", "8"), ("Long (10)", "10")],
                id="rounds-select",
            ),
            Button("Save Settings", id="save-btn", variant="primary"),
            Button("Back to Main Menu", id="back-btn", variant="primary"),
            id="settings-container",
        )
        yield Footer()

    def on_mount(self) -> None:
        user_settings = load_user_settings()

        name_input = self.query_one("#name-input", Input)
        name_input.value = user_settings["player_name"]

        rounds_select = self.query_one("#rounds-select", Select)
        rounds_select.value = str(user_settings["rounds"])

    def read_settings(self):
        settings_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "..", "settings.json"
        )
        with open(settings_path, "r", encoding="utf-8") as file:
            return json.load(file)
