import sys
import os

# ref. https://qiita.com/taigamikami/items/2713856b9f3c3b90f6fd
def disable_stderr_output(func):
    def wrapper(*args, **kwargs):
        tmp_stderr = sys.stderr
        f = open(os.devnull, 'w')
        sys.stderr = f
        func(*args, **kwargs)
        sys.stderr = tmp_stderr
        f.close()
        # print('args: {}, kwargs: {}'.format(args, kwargs))
    return wrapper


