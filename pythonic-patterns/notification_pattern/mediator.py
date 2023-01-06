from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: Component):
        """Notify all components that a change has occurred."""


@dataclass
class Component(ABC):
    mediator: Optional[Mediator] = None


@dataclass
class Button(Component):
    name: str = "login"

    def click(self):
        if self.mediator:
            self.mediator.notify(self)


@dataclass
class TextField(Component):
    name: str = "email"
    value: str = ""
    disabled: bool = False


@dataclass
class LoginPage(Mediator):
    text_field: TextField
    button: Button

    def __post_init__(self):
        self.text_field.mediator = self
        self.button.mediator = self

    def notify(self, sender: Component):
        if sender == self.button:
            self.start_login()

    def start_login(self):
        print("Disabling text field.")
        self.text_field.disabled = True
        print(f"Starting login process with email address {self.text_field.value}.")


def main() -> None:
    text_field = TextField(name="email", disabled=False)
    button = Button(name="login")

    # create the login page
    _ = LoginPage(text_field=text_field, button=button)

    text_field.value = "hi@arjancodes.com"
    button.click()
    print(f"Text field disabled: {text_field.disabled}")


if __name__ == "__main__":
    main()
