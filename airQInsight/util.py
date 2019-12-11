#!/usr/bin/python3

from __future__ import annotations
from airQ.util import parse
from airQ.model.data import Data
from typing import List, Tuple
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter


def parseData(targetPath: str) -> Data:
    return parse(targetPath)


def _plotDataForStation(station: str, pollutantID: str, pollutants: List[Tuple[int, int, int, datetime]]):
    _x = map(lambda e: e[-1], pollutants)
    _y1 = map(lambda e: e[0], pollutants)
    _y2 = map(lambda e: e[1], pollutants)
    _y3 = map(lambda e: e[2], pollutants)


def plotData(data: Data) -> bool:
    for i in data.getStationNames:
        station = data.get(i)
        for j in station.getAvailablePollutants:
            _plotDataForStation(
                station.name,
                j,
                [(k._min, k._max, k._avg, datetime.fromtimestamp(k._timestamp))
                    for k in station.getPollutantStatByID(j)]
            )


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
