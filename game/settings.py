from pathlib import Path
import json

DEFAULT_USER_SETTINGS = {"player_name": "Player", "rounds": 5}
USER_SETTINGS_PATH = Path(__file__).resolve().parent.parent / "user_settings.json"


def load_user_settings() -> dict:
    if not USER_SETTINGS_PATH.exists():
        save_user_settings(DEFAULT_USER_SETTINGS)
        return DEFAULT_USER_SETTINGS.copy()

    with USER_SETTINGS_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    player_name = str(
        data.get("player_name", DEFAULT_USER_SETTINGS["player_name"])
    ).strip()
    if not player_name:
        player_name = DEFAULT_USER_SETTINGS["player_name"]

    rounds = int(data.get("rounds", DEFAULT_USER_SETTINGS["rounds"]))
    if rounds <= 0:
        rounds = DEFAULT_USER_SETTINGS["rounds"]

    return {"player_name": player_name, "rounds": rounds}


def save_user_settings(settings: dict) -> None:
    USER_SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with USER_SETTINGS_PATH.open("w", encoding="utf-8") as file:
        json.dump(settings, file, ensure_ascii=False, indent=4)
