import random
import string
from dataclasses import dataclass
from hashlib import blake2b


class InvalidResetCodeError(Exception):
    pass


def get_password_reset_code(length: int = 8) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def encode_password(password: str) -> str:
    return blake2b(password.encode("UTF-8")).hexdigest()


@dataclass
class User:
    name: str
    password: str
    email: str
    plan: str = "basic"
    reset_code: str = ""

    def init_reset_password(self) -> str:
        self.reset_code = get_password_reset_code()
        return self.reset_code

    def reset_password(self, code: str, new_password: str):
        if code != self.reset_code:
            raise InvalidResetCodeError("Invalid password reset code.")
        self.password = encode_password(new_password)


# the 'database' of users
USERS: dict[str, User] = {}


def create_user(name: str, password: str, email: str) -> User:
    print(f"DB: creating user database entry for {name} ({email}).")
    USERS[email] = User(name, password, email)
    return USERS[email]


def find_user(email: str) -> User:
    return USERS[email]
