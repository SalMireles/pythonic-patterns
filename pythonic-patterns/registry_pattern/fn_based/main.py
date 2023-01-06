import json

from loader import load_plugins
from registry import register, run


def send_pulse(strength: int) -> None:
    print(
        f"Sending a subspace pulse of {strength} microPicards to the converter assembly."
    )


def recalibrate(target: str) -> None:
    print(f"Recalibrating the {target}.")


def reinforce(plating_type: str, target: str) -> None:
    print(f"Reinforcing {plating_type} plating of {target}.")


def main() -> None:

    # register a couple of tasks
    register("pulse", send_pulse)
    register("recalibrate", recalibrate)
    register("reinforce", reinforce)

    # read data from a JSON file
    with open("./tasks.json", encoding="utf-8") as file:
        data = json.load(file)

        # load the plugins
        load_plugins(data["plugins"])

        # run the tasks
        for task in data["tasks"]:
            run(task)


if __name__ == "__main__":
    main()
