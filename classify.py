#!/usr/bin/python3

from functools import reduce
try:
    from model.categorizedData import Station
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def buildIt(allStationHolderObject, dataObject):
    return map(lambda e: Station.fromObject(e), reduce(lambda acc, cur: acc + [reduce(lambda innerAcc, innerCur: dict([(k, v) for k, v in innerAcc.items()] + [(innerCur.updated, innerCur.findAStation(cur.station, cur.city, cur.state))]),
                                                                                      dataObject, {})], allStationHolderObject, []))


if __name__ == "__main__":
    print('[!]This module is expected to be used as a backend handler')
