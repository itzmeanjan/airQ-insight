#!/usr/bin/python3

from functools import reduce
try:
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import numpy as np
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def plotIt(dataObject) -> bool:
    '''
    label: str = '{}_{}_{}'.format(
        dataObject.name, dataObject.city, dataObject.state)
    '''
    for _, v in dict(reduce(lambda acc, cur: reduce(lambda accInner, curInner: dict([(i, j) for i, j in accInner.items()] + [(curInner.pollutantId, accInner.get(curInner.pollutantId, []) + [(cur[0], curInner.pollutantMin, curInner.pollutantMax, curInner.pollutantAvg)])]),
                                                    cur[1], acc), dataObject.pollutionStat, {})).items():
        print(sorted(v, key=lambda e: e[0], reverse=True))


if __name__ == "__main__":
    print('[!]This method is expected to be used as a backend handler')
