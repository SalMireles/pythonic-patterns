import json

from registry import TaskRegistry
from tasks import PulseFactory, RecalibrateFactory, ReinforceFactory


def main() -> None:

    # register a couple of tasks
    task_registry = TaskRegistry()
    task_registry.register("pulse", PulseFactory())
    task_registry.register("recalibrate", RecalibrateFactory())
    task_registry.register("reinforce", ReinforceFactory())

    # read data from a JSON file
    with open("./tasks.json", encoding="utf-8") as file:
        data = json.load(file)

        # create the tasks
        tasks = [task_registry.create(item) for item in data["tasks"]]

        # run the tasks
        for task in tasks:
            task.run()


if __name__ == "__main__":
    main()
