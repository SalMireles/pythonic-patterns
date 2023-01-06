import importlib


def load_plugins(plugins: list[str]) -> None:
    for plugin in plugins:
        importlib.import_module(plugin)
