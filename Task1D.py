from floodsystem.geo import rivers_with_stations, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Demonstration task for 1D"""
    stations = build_station_list()

    r_with_s = rivers_with_stations(stations)
    print('{} stations. First 10 - {}'.format(len(r_with_s), r_with_s[:10]))
    
    s_by_r = stations_by_river(stations)
    s_by_r2 = []
    for r, s in s_by_r.items():
        if r in ['River Aire', 'River Cam', 'River Thames']:
            s.sort()
            print(r, s, '\n')

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()