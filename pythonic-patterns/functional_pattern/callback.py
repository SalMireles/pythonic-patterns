from dataclasses import dataclass


@dataclass
class Button:
    label: str

    def click(self) -> None:
        print(f"Clicked on [{self.label}].")


def main() -> None:
    my_button = Button(label="Do Something")
    my_button.click()


if __name__ == "__main__":
    main()
