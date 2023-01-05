from typing import Callable

from lib.db import User

EventHandler = Callable[[User], None]

subscribers: dict[str, list[EventHandler]] = {}


def subscribe(event_type: str, handler: EventHandler) -> None:
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(handler)


def post_event(event_type: str, user: User) -> None:
    if event_type not in subscribers:
        return
    for handler in subscribers[event_type]:
        handler(user)
