#!/usr/bin/python3

from __future__ import annotations
from airQ.util import parse
from airQ.model.data import Data
from typing import List, Tuple
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter, MinuteLocator
from matplotlib.ticker import MultipleLocator, NullFormatter, StrMethodFormatter
from matplotlib.animation import FuncAnimation
from os.path import join
from .model import DataRange


def parseData(targetPath: str) -> Data:
    '''
        Simply returns an instance of airQ.model.data.Data,
        which is holding airQ collected data ( prior to this run )
    '''
    return parse(targetPath)


def _plotDataForStation(station: str, pollutantID: str, pollutants: List[Tuple[int, int, int, datetime]], targetPath: str):
    def animate(i: int):
        axes.clear()
        axes.xaxis.set_major_locator(HourLocator())
        axes.xaxis.set_major_formatter(DateFormatter('%d %b, %Y %I:%M %p'))
        # axes.xaxis.set_minor_locator(MinuteLocator(interval=15))
        axes.yaxis.set_major_locator(MultipleLocator(10))
        axes.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))
        axes.yaxis.set_minor_locator(MultipleLocator(5))
        axes.yaxis.set_minor_formatter(NullFormatter())
        axes.set_ylim((bottom, top))
        axes.tick_params(axis='x', which='major', labelsize=10,
                         labelrotation=75, labelcolor='black')
        axes.tick_params(axis='y', which='major', labelsize=10,
                         labelcolor='black')
        axes.set_title(
            'Air Quality ( {} ) Indicator for {}'.format(pollutantID, station), pad=8)
        axes.legend(
            axes.plot(
                _x[dataRange.frm:dataRange.to], _y2[dataRange.frm:dataRange.to], 'mo-',
                lw=1.2, markersize=4
            ) +
            axes.plot(
                _x[dataRange.frm:dataRange.to], _y3[dataRange.frm:dataRange.to], ls='--', marker='o',
                color='tomato', lw=3, markersize=10, markerfacecolor='red'
            ) +
            axes.plot(
                _x[dataRange.frm:dataRange.to], _y1[dataRange.frm:dataRange.to], 'co-',
                lw=1.2, markersize=4
            ),
            [
                'Maximum Reading',
                'Average Reading',
                'Minimum Reading'
            ],
            loc=0,
            fancybox=True,
            shadow=True,
            fontsize='medium',
            borderpad=1
        )
        plt.tight_layout(pad=2)
        dataRange.update()

    _x = [e[-1] for e in pollutants]
    _y1, _y2, _y3 = ([e[0] for e in pollutants],
                     [e[1] for e in pollutants],
                     [e[2] for e in pollutants])
    bottom = min(min(_y1), min(_y2), min(_y3)) - 5
    top = max(max(_y1), max(_y2), max(_y3)) + 5
    dataRange = DataRange(0, 1)
    with plt.style.context('Solarize_Light2'):
        fig = plt.figure(figsize=(16, 9), dpi=100)
        axes = fig.add_subplot(1, 1, 1)
        anim = FuncAnimation(fig, animate, interval=2000,
                             frames=len(_x))
        anim.save(targetPath, dpi=100, writer='imagemagick_file')
        plt.close(fig=fig)


def plotData(data: Data, targetPath: str) -> bool:
    try:
        for i in data.getStationNames:
            station = data.get(i)
            for j in station.getAvailablePollutants:
                _plotDataForStation(
                    str(station),
                    j,
                    [(k._min, k._max, k._avg, k.timeStamp)
                     for k in station.getPollutantStatByID(j)],
                    join(targetPath, 'airQuality{}_{}_.gif'.format(
                        ''.join(str(station).split()), j))
                )
        return True
    except Exception:
        return False


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
