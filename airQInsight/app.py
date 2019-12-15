#!/usr/bin/python3

from __future__ import annotations
from typing import Tuple
from sys import argv
from os.path import exists, dirname, abspath
from os import mkdir
from .util import parseData, plotData
from subprocess import run


def _usage():
    print('\t$ airQInsight `path-to-data-file_( *.json )_` `path-to-sink-directory`\n')


def _displayBanner():
    run('clear')
    print(
        '\x1b[1;6;35;50mairQInsight - Air Quality Data Visualization System\x1b[0m\n')


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
    try:
        _displayBanner()
        source, sink = _handleInput()
        if not source or not sink:
            _usage()
            print('Bad Input')
        else:
            print('Working ...')
            _makeDirectoryIfNotExistings(sink)
            print('\x1b[1;37;42mSuccess\x1b[0m' if plotData(
                parseData(source), sink) else '\x1b[1;37;41mFailed\x1b[0m')
    except KeyboardInterrupt:
        print('\n\x1b[1;37;41mTerminated\x1b[0m')
    finally:
        return


if __name__ == '__main__':
    main()
