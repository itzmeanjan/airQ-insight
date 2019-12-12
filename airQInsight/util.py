#!/usr/bin/python3

from __future__ import annotations
from airQ.util import parse
from airQ.model.data import Data
from typing import List, Tuple
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter, MinuteLocator
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
        axes.xaxis.set_minor_locator(MinuteLocator())
        axes.tick_params(axis='x', which='major', labelsize=10,
                         labelrotation=75, labelcolor='black')
        axes.tick_params(axis='y', which='major', labelsize=10,
                         labelcolor='black')
        axes.set_title(
            'Air Quality Indicator for {}'.format(station), pad=8)
        axes.legend(
            axes.plot(
                _x[dataRange.frm:dataRange.to], _y1[dataRange.frm:dataRange.to], 'co-',
                lw=1.2, markersize=4
            ) +
            axes.plot(
                _x[dataRange.frm:dataRange.to], _y2[dataRange.frm:dataRange.to], 'mo-',
                lw=1.2, markersize=4
            ) +
            axes.plot(
                _x[dataRange.frm:dataRange.to], _y3[dataRange.frm:dataRange.to], ls='--', marker='o',
                color='tomato', lw=3, markersize=10, markerfacecolor='red'
            ),
            [
                'Minimum Reading',
                'Maximum Reading',
                'Average Reading'
            ],
            loc=0,
            fancybox=True,
            shadow=True,
            fontsize='medium',
            borderpad=1
        )
        plt.tight_layout(pad=3)
        dataRange.update()

    _x = [e[-1] for e in pollutants]
    _y1, _y2, _y3 = ([e[0] for e in pollutants],
                     [e[1] for e in pollutants],
                     [e[2] for e in pollutants])
    dataRange = DataRange(0, 1)
    with plt.style.context('Solarize_Light2'):
        fig = plt.figure(figsize=(16, 9), dpi=200)
        axes = fig.add_subplot(1, 1, 1)
        anim = FuncAnimation(fig, animate, interval=3600,
                             frames=len(_x))
        anim.save(targetPath, dpi=200, writer='imagemagick_file')
        plt.close(fig=fig)


def plotData(data: Data, targetPath: str) -> bool:
    for i in data.getStationNames:
        station = data.get(i)
        for j in station.getAvailablePollutants:
            _plotDataForStation(
                str(station),
                j,
                [(k._min, k._max, k._avg, k.timeStamp)
                    for k in station.getPollutantStatByID(j)],
                join(targetPath, 'airQuality{}.gif'.format(
                    '_'.join(str(station).split())))
            )
            break
        break


if __name__ == '__main__':
    print('[!]This module is designed to be used as a backend handler')
