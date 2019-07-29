#!/usr/bin/python3

'''
    Holds reading of a certain pollutant, identified by its unique id,
    which is generally collected from a certain monitoring station
'''


class Pollutant:
    def __init__(self, pollutantId: str, pollutantUnit: str, pollutantMin: float, pollutantMax: float, pollutantAvg: float):
        self.pollutantId = pollutantId
        self.pollutantUnit = pollutantUnit
        self.pollutantMin = pollutantMin
        self.pollutantMax = pollutantMax
        self.pollutantAvg = pollutantAvg

    '''
        Gets you an instance of this class, where you supply a Dict{String, Any} object,
        and after picking values from proper fields, a new instance of this class is returned
    '''
    @staticmethod
    def fromJSON(jsonObject):
        return Pollutant(jsonObject.get('pollutantId'), jsonObject.get('pollutantUnit'), jsonObject.get('pollutantMin'), jsonObject.get('pollutantMax'), jsonObject.get('pollutantAvg'))


'''
    Keeps track of all readings of pollutants for a certain monitoring station
'''


class Record:
    def __init__(self, station: str, city: str, state: str, country: str, pollutants):
        self.station = station
        self.city = city
        self.state = state
        self.country = country
        self.pollutants = pollutants

    '''
        Gets you an instance of this class, where you supply a Dict[String, Any] object,
        and after picking values from proper fields, a new instance of this class is returned
    '''
    @staticmethod
    def fromJSON(jsonObject):
        return Record(jsonObject.get("station"), jsonObject.get("city"), jsonObject.get("state"), jsonObject.get("country"), list(map(lambda e: Pollutant.fromJSON(e), jsonObject.get("pollutants"))))


'''
    Holds pollutant data collected from all monitoring stations all over India,
    for a certain period of time

    Well the time period is 1 hour generally, but in this object we'll hold
    a timeStamp in `updated` field, which will give us idea of time period
'''


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

    '''
        Given a certain monitoring station name, its city & state,
        we can simply find an object, holding all data collected by that station,
        which is nothing but a `Record` object
    '''

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

    '''
        Returns an instance of this class, where data is passed as Dict[String, Any] object
    '''

    @staticmethod
    def fromJSON(jsonObject):
        return DataSet(jsonObject.get('indexName'), jsonObject.get('created'), jsonObject.get('updated'), jsonObject.get('title'), jsonObject.get('description'), jsonObject.get('count'), jsonObject.get('limit'), jsonObject.get('total'), jsonObject.get('offset'), list(map(lambda e: Record.fromJSON(e), jsonObject.get('records').get('all'))))


if __name__ == "__main__":
    print('[!]This module is expected to be used as a backend handler')
