#!/usr/bin/python3

from __future__ import annotations
from typing import Tuple
from airQ.util import parse
from sys import argv


def _handleInput() -> Tuple[str, str]:
    return (argv[0], argv[1]) if len(argv) == 3 and argv[0].endswith('.json') else (None, None)


def main():
    source, sink = _handleInput()
    if not source or not sink:
        return False


if __name__ == '__main__':
    main()
