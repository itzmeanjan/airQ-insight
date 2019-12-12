#!/usr/bin/python3

from __future__ import annotations
from typing import Tuple
from sys import argv
from os.path import exists, dirname, abspath
from os import mkdir
from .util import parseData, plotData


def _makeDirectoryIfNotExistings(targetPath: str):
    '''
        Creates sink directory, if that doesn't already exists
    '''
    if not exists(targetPath):
        mkdir(targetPath)


def _handleInput() -> Tuple[str, str]:
    '''
        Checks whether user provided required
        CMD inputs, while invoking script or not.

        If yes, return those
        else return None, to denote error.
    '''
    return (abspath(argv[1]), abspath(argv[2])) \
        if len(argv) == 3 and argv[1].endswith('.json') and exists(argv[1]) \
        else (None, None)


def main():
    '''
        Entry point of script
    '''
    source, sink = _handleInput()
    if not source or not sink:
        return False
    _makeDirectoryIfNotExistings(sink)
    plotData(parseData(source), sink)
    return


if __name__ == '__main__':
    main()
