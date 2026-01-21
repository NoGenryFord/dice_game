import json
import os


class FileController:

    __ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

    def save_result(self, name: str, round: int, score: int): ...

    def read_results(self):
        result = []
        file_path = os.path.join(self.__ROOT_PATH, "..", "scores", "games_result.json")

        with open(file=file_path, mode="r", encoding="utf-8") as file:
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
