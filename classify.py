#!/usr/bin/python3

from functools import reduce
try:
    from model.categorizedData import Station
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)

'''
    Takes two arguments i.e. a List[Record], holding max # of monitoring station data,
    and an iterator of `DataSet` object(s), and classifies all data collected over a time period
    of last 24 hours by their corresponding collecting stations, returns a Python `map` object ( where each of them is `Station` object,
    holding all data collected by that certain monitoring station for a time period of last 24 hours )
'''


def buildIt(allStationHolderObject, dataObject):
    return map(lambda e: Station.fromObject(dict(
        filter(lambda eInner: eInner[1] is not None, e.items()))), reduce(lambda acc, cur: acc + [reduce(lambda innerAcc, innerCur: dict([(k, v) for k, v in innerAcc.items()] + [(innerCur.updated, innerCur.findAStation(cur.station, cur.city, cur.state))]),
                                                                                                         dataObject, {})], allStationHolderObject, []))


if __name__ == "__main__":
    print('[!]This module is expected to be used as a backend handler')
