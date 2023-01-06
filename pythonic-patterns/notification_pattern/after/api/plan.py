from event.core import post_event
from lib.db import find_user


def upgrade_plan(email: str) -> None:
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    # post an event
    post_event("user_upgrade_plan", user)
