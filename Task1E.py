from floodsystem.geo import rivers_with_station

from floodsystem.geo import stations_by_river

from floodsystem.stationdata import build_station_list

from floodsystem.geo import rivers_by_station_number

stations = build_station_list()

rivernames = rivers_with_station(stations)

 

print("*** Task 1E: CUED Part IA Flood Warning System ***")

print(rivers_by_station_number(stations, 9))