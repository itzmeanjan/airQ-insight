#!/usr/bin/python3


class Pollutant:
    def __init__(self, pollutantId: str, pollutantUnit: str, pollutantMin: float, pollutantMax: float, pollutantAvg: float, timeStamp: int):
        self.pollutantId = pollutantId
        self.pollutantUnit = pollutantUnit
        self.pollutantMin = pollutantMin
        self.pollutantMax = pollutantMax
        self.pollutantAvg = pollutantAvg
        self.timeStamp = timeStamp

    @staticmethod
    def getInstance(fromObject):
        pass


class Station:
    def __init__(self, name: str, city: str, state: str, country: str, pollutantStat):
        self.name = name
        self.city = city
        self.state = state
        self.country = country
        self.pollutantStat = pollutantStat

    @staticmethod
    def getInstance(fromObject):
        pass


if __name__ == "__main__":
    print('[!]This module is expected to be used as a backend handler')
