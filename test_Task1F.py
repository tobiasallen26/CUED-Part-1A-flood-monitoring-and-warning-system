from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def test_typical_range_consistent():
    """tests requirements of MonitoringStation.typical_range_consistent"""
    station = MonitoringStation(None, None, None, None, None, None, None)
    # tests for when there is no typical range
    assert not station.typical_range_consistent()
    station.typical_range = (0, 1)
    # tests for when the typical range is consistent
    assert station.typical_range_consistent()
    station.typical_range = (1, 0)
    # tests for when the typical range is inconsistent
    assert not station.typical_range_consistent()

def test_inconsistent_typical_range_stations():
    """tests requirements of inconsistent_typical_range_stations"""
    # defines a list of monitoring stations where 3 have consistent data
    # and 2 have inconsistent data
    stations = [
        MonitoringStation(None, None, None, None, (0, 1), None, None),
        MonitoringStation(None, None, None, None, (0, 1), None, None),
        MonitoringStation(None, None, None, None, (0, 1), None, None),
        MonitoringStation(None, None, None, None, None, None, None),
        MonitoringStation(None, None, None, None, None, None, None)]
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    # checks the type of inconsistent_stations
    assert type(inconsistent_stations) == list
    # checks the type of objects in inconsistent_stations
    assert type(inconsistent_stations[0]) == MonitoringStation
    # checks that the length of inconsistent stations is 2
    assert len(inconsistent_stations) == 2
