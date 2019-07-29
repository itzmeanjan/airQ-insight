#!/usr/bin/python3

from os import listdir
from os.path import dirname, join, abspath, isdir, isfile
from functools import reduce
try:
    from objectify import buildObject
    from classify import buildIt
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


def app(target_path: str = abspath(join(dirname(__file__), '../airQ/data'))):
    return None if(not isdir(target_path)) else buildIt(reduce(lambda acc, cur: (cur if(len(cur.records) > len(acc.records)) else acc) if(acc is not None) else cur, filter(lambda e: e is not None, map(lambda e:
                                                                                                                                                                                                         buildObject(join(target_path, e)), filter(lambda e: isfile(join(target_path, e)) and e.endswith(
                                                                                                                                                                                                             'json'), listdir(path=target_path)))), None).records, filter(lambda e: e is not None, map(lambda e:
                                                                                                                                                                                                                                                                                                       buildObject(join(target_path, e)), filter(lambda e: isfile(join(target_path, e)) and e.endswith(
                                                                                                                                                                                                                                                                                                           'json'), listdir(path=target_path)))))


if __name__ == '__main__':
    try:
        print("success" if app() else "failure")
    except KeyboardInterrupt:
        print('\n[!]Terminated')
    finally:
        exit(0)
