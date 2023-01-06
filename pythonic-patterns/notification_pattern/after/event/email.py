from lib.db import User
from lib.email import send_email

from event.core import subscribe


def handle_user_registered_event(user: User) -> None:
    # send a welcome email
    send_email(
        user.name,
        user.email,
        "Welcome",
        f"Thanks for registering, {user.name}!\nRegards, The team",
    )


def handle_user_password_forgotten_event(user: User) -> None:
    # send a password reset message
    send_email(
        user.name,
        user.email,
        "Reset your password",
        f"To reset your password, use this code: {user.reset_code}.\nRegards, The team",
    )


def handle_user_upgrade_plan_event(user: User) -> None:
    # send a thank you email
    send_email(
        user.name,
        user.email,
        "Thank you",
        f"Thanks for upgrading, {user.name}! You're gonna love it. \nRegards, The team",
    )


def setup_email_event_handlers() -> None:
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)
