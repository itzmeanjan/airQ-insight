#!/usr/bin/python3

from os import listdir, mkdir
from os.path import dirname, join, abspath, isdir, isfile
from shutil import rmtree
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

    Now we've another new module, `plot`, which will help us is plotting time vs. pollutant stat dataset
    for a certain place.

    We pass dataset for a certain place, which does all classification jobs,
    i.e. categorizing dataset as per their `pollutantId`, and plotting using matplotlib,
    which will be eventually exported to a `./data/*.svg` file, for futher usage
'''


def app(source_path=abspath(join(dirname(__file__), '../airQ/data')), sink_path=abspath(join(dirname(__file__), 'data'))):
    def __objectify__():
        return list(filter(lambda e: e is not None, map(lambda e:
                                                        buildObject(
                                                            join(source_path, e)),
                                                        filter(lambda e: isfile(join(source_path, e)) and e.endswith(
                                                            'json'), listdir(path=source_path)))))

    def __getStations__(object):
        return reduce(lambda acc, cur: cur if acc is None else acc if len(
            acc.records) > len(cur.records) else cur, object, None).records

    try:
        # creates directory if not present
        if(not isdir(sink_path)):
            mkdir(sink_path)
        # first emptying already existing one
        # then recreates it
        else:
            rmtree(sink_path, ignore_errors=True)
            mkdir(sink_path)
        tmpObject = __objectify__()
        return all(map(lambda e: plotIt(e, sink_path), None if(not isdir(source_path)) else buildIt(__getStations__(tmpObject), tmpObject)))
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    try:
        code = 0 if app() else 1
        print('success' if(code == 0) else 'failure')
    except KeyboardInterrupt:
        code = 1
        print('\n[!]Terminated')
    finally:
        exit(code)
