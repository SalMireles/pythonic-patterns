from event.core import post_event
from lib.db import create_user, find_user


def register_new_user(name: str, password: str, email: str) -> None:
    # create an entry in the database
    user = create_user(name, password, email)

    # post an event
    post_event("user_registered", user)


def password_forgotten(email: str) -> None:
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.init_reset_password()

    # post an event
    post_event("user_password_forgotten", user)


def reset_password(code: str, email: str, password: str) -> None:

    # retrieve the user
    user = find_user(email)

    # reset the password
    user.reset_password(code, password)
