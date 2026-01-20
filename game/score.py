import json
import os


class FileController:

    __BASE_PATH = os.path.dirname("/scores/game_results.json")

    def save_result(self, name: str, round: int, score: int): ...

    def read_results(self):
        result = []

        with open(
            file="./scores/game_results.json", mode="r", encoding="utf-8"
        ) as file:
            data = json.load(file)
            for item in data:
                result.append(
                    (
                        item["Дата"],
                        item["Игрок"],
                        item["Количество раундов"],
                        item["Итоговый счет"],
                    )
                )

        return result


if __name__ == "__main__":
    fc = FileController()

    print(fc.read_results())
