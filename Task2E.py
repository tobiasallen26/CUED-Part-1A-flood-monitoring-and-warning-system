from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_level_over_threshold
import datetime


def run():
    """Demonstration task for 2E"""
    stations = build_station_list()
    update_water_levels(stations)

    stations = stations_level_over_threshold(stations, -1000)

    dt = datetime.timedelta(days=10)
    dates, levels = fetch_measure_levels(stations[1][0].measure_id, dt)
    
    plot_water_levels(stations[1][0], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()