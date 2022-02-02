from floodsystem.geo import rivers_with_stations
from floodsystem.stationdata import build_station_list

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