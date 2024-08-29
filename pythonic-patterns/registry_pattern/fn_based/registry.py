from typing import Any, Callable

task_functions: dict[str, Callable[..., None]] = {}


def register(task_type: str, task_fn: Callable[..., None]) -> None:
    task_functions[task_type] = task_fn


def unregister(task_type: str) -> None:
    task_functions.pop(task_type, None)


def run(arguments: dict[str, Any]) -> None:
    args_copy = arguments.copy()
    task_type = args_copy.pop("type")
    task_functions[task_type](**args_copy)
