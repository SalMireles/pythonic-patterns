import logging

from lib.db import find_user
from lib.email import send_email
from lib.slack import post_slack_message


def upgrade_plan(email: str) -> None:
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    # post a Slack message to sales department
    post_slack_message("sales", f"{user.name} has upgraded their plan.")

    # send a thank you email
    send_email(
        user.name,
        user.email,
        "Thank you",
        f"Thanks for upgrading, {user.name}! You're gonna love it. \nRegards, The DevNotes team",
    )

    # write server log
    logging.debug(f"User with email address {user.email} has upgraded their plan")
