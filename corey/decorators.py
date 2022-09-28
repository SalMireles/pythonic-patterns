import functools
import time


def my_simple_decorator(func):
    @functools.wraps(func)  # fixes original function introspection
    def wrapper(*args, **kwargs):
        print("ran first")
        something = func(*args, **kwargs)
        print("ran after the function")
        return something  # in case funciton has a return

    return wrapper


def timeit(func):
    @functools.wraps(func)
    def time_eval(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        total_time = time.perf_counter() - start_time
        return total_time
        print(f"Finished {func.__name__!r} in {total_time:.2f} seconds")

    return time_eval
