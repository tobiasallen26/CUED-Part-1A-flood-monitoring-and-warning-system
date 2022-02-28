
from unittest.util import sorted_list_difference


from floodsystem.station import MonitoringStation


def stations_highest_rel_level(stations, N):
    water_level_relative = []
    "create empty list"
    for station in stations:
        if MonitoringStation.relative_water_level(station)== None:
            "If there is nothing there, don't add it to the list"
            pass
        else:
            stations_highest_rel_level.append((station,MonitoringStation.relative_water_level(station)))
            "add it to the list"
    SortedList = sorted_list_difference(stations_highest_rel_level,reverse=True)
    "For descending order"

    a = SortedList[:N]
    b = []
    for X in a:
        b.append(X[0])
    return b

    
    
    

