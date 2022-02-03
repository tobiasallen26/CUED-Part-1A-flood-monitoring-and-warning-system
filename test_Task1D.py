from floodsystem.geo import rivers_with_stations, stations_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def test_rivers_with_stations():
    """tests requirements of station_by_distance"""
    stations = build_station_list()
    r_with_s = rivers_with_stations(stations)
    # checks the type of object returned
    assert type(r_with_s) == list
    # checks type of object in r_with_s
    assert type(r_with_s[0]) == str
    # checks that there are no duplicates in the list
    for river in r_with_s:
        assert r_with_s.count(river) == 1

def test_stations_by_river():
    """tests requirements of stations_by_river"""
    stations = build_station_list()
    s_by_r = stations_by_river(stations)
    # checks the type of object returned
    assert type(s_by_r) == dict
    # checks type of object in s_by_r
    assert type(list(s_by_r.values())[0]) == list
    # checks the type of object in the lists of stations
    assert type(list(s_by_r.values())[0][0]) == MonitoringStation
