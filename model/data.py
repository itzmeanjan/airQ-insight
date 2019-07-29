#!/usr/bin/python3

'''
    
'''


class Pollutant:
    def __init__(self, pollutantId: str, pollutantUnit: str, pollutantMin: float, pollutantMax: float, pollutantAvg: float):
        self.pollutantId = pollutantId
        self.pollutantUnit = pollutantUnit
        self.pollutantMin = pollutantMin
        self.pollutantMax = pollutantMax
        self.pollutantAvg = pollutantAvg

    @staticmethod
    def fromJSON(jsonObject):
        return Pollutant(jsonObject.get('pollutantId'), jsonObject.get('pollutantUnit'), jsonObject.get('pollutantMin'), jsonObject.get('pollutantMax'), jsonObject.get('pollutantAvg'))


class Record:
    def __init__(self, station: str, city: str, state: str, country: str, pollutants):
        self.station = station
        self.city = city
        self.state = state
        self.country = country
        self.pollutants = pollutants

    @staticmethod
    def fromJSON(jsonObject):
        return Record(jsonObject.get("station"), jsonObject.get("city"), jsonObject.get("state"), jsonObject.get("country"), list(map(lambda e: Pollutant.fromJSON(e), jsonObject.get("pollutants"))))


class DataSet:
    def __init__(self, indexName: str, created: int, updated: int, title: str, description: str, dataCount: int, limit: int, total: int, offset: int, records):
        self.indexName = indexName
        self.created = created
        self.updated = updated
        self.title = title
        self.description = description
        self.dataCount = dataCount
        self.limit = limit
        self.total = total
        self.offset = offset
        self.records = records

    def findAStation(self, station, city, state):
        target_result = None
        try:
            target_result = list(filter(lambda e: e.station == station and e.city ==
                                        city and e.state == state, self.records))[0]
        except IndexError:
            target_result = None
        except Exception:
            target_result = None
        finally:
            return target_result

    @staticmethod
    def fromJSON(jsonObject):
        return DataSet(jsonObject.get('indexName'), jsonObject.get('created'), jsonObject.get('updated'), jsonObject.get('title'), jsonObject.get('description'), jsonObject.get('count'), jsonObject.get('limit'), jsonObject.get('total'), jsonObject.get('offset'), list(map(lambda e: Record.fromJSON(e), jsonObject.get('records').get('all'))))


if __name__ == "__main__":
    print('[!]This module is expected to be used as a backend handler')
