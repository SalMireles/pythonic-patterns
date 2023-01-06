from api.plan import upgrade_plan
from api.user import password_forgotten, register_new_user
from event.email import setup_email_event_handlers
from event.log import setup_log_event_handlers
from event.slack import setup_slack_event_handlers


def main() -> None:
    # initialize the event structure
    setup_slack_event_handlers()
    setup_log_event_handlers()
    setup_email_event_handlers()

    # register a new user
    register_new_user("Arjan", "BestPasswordEva", "hi@arjancodes.com")

    # send a password reset message
    password_forgotten("hi@arjancodes.com")

    # upgrade the plan
    upgrade_plan("hi@arjancodes.com")


if __name__ == "__main__":
    main()
