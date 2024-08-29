import json
from typing import Protocol

from tasks import Pulse, Recalibrate, Reinforce


class Task(Protocol):
    def run(self) -> None:
        ...


def main() -> None:
    with open("./tasks.json", encoding="utf-8") as file:
        data = json.load(file)

        tasks: list[Task] = []

        for item in data["tasks"]:
            if item["type"] == "pulse":
                tasks.append(Pulse(item["strength"]))
            elif item["type"] == "recalibrate":
                tasks.append(Recalibrate(item["target"]))
            elif item["type"] == "reinforce":
                tasks.append(Reinforce(item["plating_type"], item["target"]))

        # run the tasks
        for task in tasks:
            task.run()


if __name__ == "__main__":
    main()
