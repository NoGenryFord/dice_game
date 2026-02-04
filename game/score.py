import json
import os


class FileController:

    __ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

    def save_result(self, date: str, player: str, rounds: int, score: int):
        file_path = os.path.join(self.__ROOT_PATH, "..", "scores", "games_result.json")

        if os.path.exists(file_path):
            with open(file=file_path, mode="r", encoding="utf-8") as file:
                data = json.load(file)
        else:
            data = []

        new_result = {
            "Date": date,
            "Player": player,
            "Rounds": rounds,
            "Score": score,
        }
        data.append(new_result)
        with open(file=file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def read_results(self):
        result = []
        file_path = os.path.join(self.__ROOT_PATH, "..", "scores", "games_result.json")

        with open(file=file_path, mode="r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                result.append(
                    (
                        item["Date"],
                        item["Player"],
                        item["Rounds"],
                        item["Score"],
                    )
                )

        return result


if __name__ == "__main__":
    ...
