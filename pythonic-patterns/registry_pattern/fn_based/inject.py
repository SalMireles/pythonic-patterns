from registry import register


def inject(material: str, target: str) -> None:
    print(f"Injecting {material} into {target}.")


register("inject", inject)
