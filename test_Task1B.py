from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    """tests requirements of station_by_distance"""
    CAM_COORDS = (52.2053, 0.1218)
    stations = build_station_list()
    station_distance = stations_by_distance(stations, CAM_COORDS)
    # checks the type of the objects in the list
    assert type(station_distance[0][0]) == MonitoringStation
    assert type(station_distance[0][1]) == float
    # checks the order of the list
