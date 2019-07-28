#!/usr/bin/python3


class Station:
    def __init__(self, name: str, city: str, state: str, country: str, pollutionStat):
        self.name = name
        self.city = city
        self.state = state
        self.country = country
        self.pollutionStat = pollutionStat

    @staticmethod
    def fromObject(dataObject):
        tmpObject = list(dataObject.values())[0]
        return Station(tmpObject.station, tmpObject.city, tmpObject.state, tmpObject.country, map(lambda e: (e[0], e[1].pollutants), filter(lambda e: e[1] is not None, dataObject.items())))


if __name__ == "__main__":
    print('[!]This module is expected to be used as a backend handler')
