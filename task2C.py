
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

stations = build_station_list()
update_water_levels(stations)
def run():
    print(stations_highest_rel_level(stations , 5))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()