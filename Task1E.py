from floodsystem.geo import rivers_with_stations 

from floodsystem.geo import stations_by_river

from floodsystem.stationdata import build_station_list

from floodsystem.geo import Rivers_by_Station_number

stations = build_station_list()

rivernames = rivers_with_stations(stations)

 

print("*** CUED Task 1E Flood Warning System ***")

print(Rivers_by_Station_number(stations, 9))

