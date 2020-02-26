#!/usr/bin/env python

import sys
import output_decorator

def output_stderr(s):
    print(s, file=sys.stderr)

@output_decorator.disable_stderr_output
def disable_output_stderr(s):
    print(s, file=sys.stderr)

def main():
    output_stderr("this is enable stderr.")
    disable_output_stderr("this is disable stderr.")
    output_stderr("this is enable stderr.")
    with output_decorator.DisableStderr():
        output_stderr("this is enable stderr.")
    sys.exit(0)

if __name__ == '__main__':
    main()

