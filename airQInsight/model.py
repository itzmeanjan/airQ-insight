#!/usr/bin/python3

from __future__ import annotations


class DataRange(object):
    '''
        Holds range of data to be plotted at a certain iteration.

        Range denoted by index.

        Calling update() method, ensures `frm` and `to`,
        these two properties get updated properly, so that
        data to plotted in this frame, gets selected how it's
        supposed to be selected. 
    '''

    def __init__(self, frm: int, to: int):
        self.frm = frm
        self.to = to

    def update(self):
        self.to += 1
        if self.to - self.frm > 24:
            self.frm += 1


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
    exit(0)
