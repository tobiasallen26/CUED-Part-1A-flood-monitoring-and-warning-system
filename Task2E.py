from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.utils import sorted_by_key
import datetime


def run():
    """Demonstration task for 2E"""
    # builds and updates a list of stations
    stations = build_station_list()
    update_water_levels(stations)
    # gets the stations with the 5 highest water levels
    stations = stations_highest_rel_level(stations, 5)

    dt = datetime.timedelta(days=10)
    # plots the water levels and typical range 
    for station in stations:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt)
        plot_water_levels(station[0], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()