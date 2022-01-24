from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()

    for s in stations:
        print(s.typical_range_consistent())

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
