from floodsystem.geo import rivers_with_stations
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    print(rivers_with_stations(stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()