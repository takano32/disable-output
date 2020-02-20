import sys
import os

def disable_stderr_output(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

        print('args: {}, kwargs: {}'.format(args, kwargs))
    return wrapper


