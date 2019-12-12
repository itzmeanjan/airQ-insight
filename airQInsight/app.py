#!/usr/bin/python3

from __future__ import annotations
from typing import Tuple
from sys import argv
from os.path import exists, dirname, abspath
from os import mkdir
from .util import parseData, plotData


def _makeDirectoryIfNotExistings(targetPath: str):
    if not exists(targetPath):
        mkdir(targetPath)


def _handleInput() -> Tuple[str, str]:
    return (abspath(argv[1]), abspath(argv[2])) \
        if len(argv) == 3 and argv[1].endswith('.json') and exists(argv[1]) \
        else (None, None)


def main():
    source, sink = _handleInput()
    if not source or not sink:
        return False
    _makeDirectoryIfNotExistings(sink)
    plotData(parseData(source), sink)


if __name__ == '__main__':
    main()
