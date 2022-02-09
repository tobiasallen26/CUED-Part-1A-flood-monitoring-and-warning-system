from unicodedata import name
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def Testing_code1C():
    name =[]
    stations = build_station_list()
    for station in stations:
        name.append(station.name)
        