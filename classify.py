#!/usr/bin/python3

from functools import reduce


def buildIt(dataObject):
    target_result = None
    try:
        reduce(lambda acc, cur: acc + [reduce(lambda innerAcc, innerCur: dict([(k, v) for k, v in innerAcc.items()] + [(innerAcc.updated, innerCur.findAStation(cur.station, cur.city, cur.state))]),
                                              dataObject, {})], reduce(
            lambda acc, cur: (cur if(len(cur.records) > len(acc.records)) else acc) if(acc is not None) else cur, dataObject, None).records, [])
    except Exception:
        target_result = None
    finally:
        return target_result


if __name__ == "__main__":
    print('[!]This module is expected to be used as a backend handler')
