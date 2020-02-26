import sys
import os
import multiprocessing as mp

# ref. https://qiita.com/taigamikami/items/2713856b9f3c3b90f6fd

lock = mp.Lock()


def disable_stderr_output(func):
    def wrapper(*args, **kwargs):
        with lock:
            tmp_stderr = sys.stderr
            f = open(os.devnull, 'w')
            sys.stderr = f
            func(*args, **kwargs)
            sys.stderr = tmp_stderr
            f.close()
    return wrapper
