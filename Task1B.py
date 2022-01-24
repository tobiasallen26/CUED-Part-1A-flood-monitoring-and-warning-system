from floodsystem.geo import stations_by_distance

from floodsystem.stationdata import build_station_list

CAM_COORDS = (52.2053, 0.1218)

def run():
    stations = build_station_list()

    stations_by_distance(stations, CAM_COORDS)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
