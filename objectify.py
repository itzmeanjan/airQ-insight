#!/usr/bin/python3

from os.path import isfile
from json import load
try:
    from model.data import DataSet
except ImportError as e:
    print('[!]Module Unavailable : {}'.format(str(e)))
    exit(1)

'''
    Reads JSON data from a certain file, whose path is supplied as parameter,
    objectifies data ( collected by all monitoring stations present all over India ) & returns an instance of `DataSet` class
'''

def buildObject(target_file: str):
    target_result = None
    try:
        if(not isfile(target_file)):
            raise('invalid target path')
        with open(target_file, 'r') as fd:
            target_result = DataSet.fromJSON(load(fd))
    except Exception:
        target_result = None
    finally:
        return target_result


if __name__ == "__main__":
    print('[!]This module is expected to be used as a backend handler')
