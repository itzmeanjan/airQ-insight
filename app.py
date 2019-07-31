#!/usr/bin/python3

from os import listdir, mkdir
from os.path import dirname, join, abspath, isdir, isfile
from functools import reduce
try:
    from objectify import buildObject
    from classify import buildIt
    from plot import plotIt
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)


'''
    This function does a lot of works, but in lazy fashion

    - Lazy ?
    - Yup, it's a bit lazy

    Cause I've tried using a lot of functional constructs ( recently added into Python ) in this project,
    which simply doesn't immediately compute results as soon as executed, until and unless
    you ask it to do so, it won't.

    What we'll simply do here is, we'll head over to collected data holder directory,
    and start iterating over them, and using some utility function we'll get instance of `DataSet` class,
    which will keep all data collected from all monitoring stations over India, for a certain time period
'''


def app(source_path: str = abspath(join(dirname(__file__), '../airQ/data')), sink_path: str = abspath(join(dirname(__file__), 'data'))) -> bool:
    try:
        if(not isdir(sink_path)):
            mkdir(sink_path)
        plotIt(None if(not isdir(source_path)) else next(buildIt(reduce(lambda acc, cur: (cur if(len(cur.records) > len(acc.records)) else acc) if(acc is not None) else cur, filter(lambda e: e is not None, map(lambda e:
                                                                                                                                                                                                                  buildObject(join(source_path, e)), filter(lambda e: isfile(join(source_path, e)) and e.endswith(
                                                                                                                                                                                                                      'json'), listdir(path=source_path)))), None).records, filter(lambda e: e is not None, map(lambda e:
                                                                                                                                                                                                                                                                                                                buildObject(join(source_path, e)), filter(lambda e: isfile(join(source_path, e)) and e.endswith(
                                                                                                                                                                                                                                                                                                                    'json'), listdir(path=source_path)))))), sink_path)
        return True
    except Exception:
        return False


if __name__ == '__main__':
    try:
        print('success' if app() else 'failure')
    except KeyboardInterrupt:
        print('\n[!]Terminated')
    finally:
        exit(0)
