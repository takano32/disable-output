import sys
import os
import threading

# ref. https://qiita.com/taigamikami/items/2713856b9f3c3b90f6fd

lock = threading.Lock()

class DisableStderr(object):
    def __enter__(self):
        self.tmp_stderr = sys.stderr
        self.f = open(os.devnull, 'w')
        sys.stderr = self.f

    def __exit__(self, *arg, **kwargs):
        sys.stderr = self.tmp_stderr
        self.f.close()


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
