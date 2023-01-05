from api.plan import upgrade_plan
from api.user import password_forgotten, register_new_user


def main() -> None:
    # register a new user
    register_new_user("Arjan", "BestPasswordEva", "hi@arjancodes.com")

    # send a password reset message
    password_forgotten("hi@arjancodes.com")

    # upgrade the plan
    upgrade_plan("hi@arjancodes.com")


if __name__ == "__main__":
    main()
