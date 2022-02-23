from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
import datetime


def run():
    """Demonstration task for 2E"""
    stations = build_station_list()
    update_water_levels(stations)

    stations = stations_level_over_threshold(stations, -1000)

    dt = datetime.timedelta(days=10)
    
    best = [(0, None) for i in range(5)]
    for s in stations:
        if s[0].relative_water_level() > best[-1][0]:
            best[-1] = (s[0].relative_water_level(), s[0])
            best = sorted_by_key(best, 0, reverse=True)
    print(best)

    for station in best:
        dates, levels = fetch_measure_levels(station[1].measure_id, dt)
        plot_water_levels(station[1], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()