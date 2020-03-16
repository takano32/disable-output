#!/usr/bin/env python

import sys
import concurrent.futures

from output_decorator import disable_stderr_output
from output_decorator import DisableStderr

def output_stderr(s):
    print(s, file=sys.stderr)
    # sys.stderr.write(s)

@disable_stderr_output
def disable_output_stderr(s):
    print(s, file=sys.stderr)
    # sys.stderr.write(s)


def enable_output():
    output_stderr("this is enable stderr.")

def disable_output():
    disable_output_stderr("this is disable stderr.")

def output():
    enable_output()
    disable_output()
    enable_output()
    with DisableStderr():
        enable_output()

def main():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(output)
    executor.submit(output)
    executor.submit(output)
    executor.submit(output)
    executor.submit(output)
    executor.submit(output)
    output()
    sys.exit(0)

if __name__ == '__main__':
    main()

