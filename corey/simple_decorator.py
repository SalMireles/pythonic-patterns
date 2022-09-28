import time

from decorators import my_simple_decorator, timeit


@my_simple_decorator
def say_whee():
    print("whee! - function output")


@timeit
def slow_func(seconds):
    time.sleep(seconds)


if __name__ == "__main__":
    say_whee()
    slow_func(3)
