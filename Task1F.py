from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()

    inconsistent_stations = inconsistent_typical_range_stations(stations)
    inconsistent_station_names = []
    for s in inconsistent_stations:
        inconsistent_station_names.append(s.name)
    inconsistent_station_names.sort()
    print(inconsistent_station_names)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
