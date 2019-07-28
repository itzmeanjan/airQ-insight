#!/usr/bin/python3

from os import listdir
from os.path import dirname, join, abspath, isdir, isfile
from objectify import buildObject


def app(target_path: str = abspath(join(dirname(__file__), '../airQ/data'))) -> bool:
    target_result = False
    try:
        if(not isdir(target_path)):
            raise("invalid datadir")
        print(list(filter(lambda e: e is not None, map(lambda e:
                                                       buildObject(join(target_path, e)), filter(lambda e: isfile(join(target_path, e)) and e.endswith(
                                                           'json'), listdir(path=target_path))))))
        target_result = True
    except Exception:
        target_result = False
    finally:
        return target_result


if __name__ == '__main__':
    try:
        print("success" if app() else "failure")
    except KeyboardInterrupt:
        print('\n[!]Terminated')
    finally:
        exit(0)
