from floodsystem.geo import stations_by_distance

from floodsystem.stationdata import build_station_list

CAM_COORDS = (52.2053, 0.1218)

def run():
    stations = build_station_list()

    station_distance = stations_by_distance(stations, CAM_COORDS)
    
    s_d_print_format = []
    for s, d in station_distance:
        s_d_print_format.append((s.name, s.town, d))

    print("The 10 closest are {} \n".format(s_d_print_format[:10]))
    print("The 10 fruthest are {} \n".format(s_d_print_format[-10:]))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
