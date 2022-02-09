from calendar import c
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    P = (52.2053,0.1218)
    stationlist = stations_within_radius(stations, P, 10)
    Alp = sorted(stationlist)
    print(Alp)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()


    
