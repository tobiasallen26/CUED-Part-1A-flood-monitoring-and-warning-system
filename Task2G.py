from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
import matplotlib
import datetime

def run():
    """Demonstration task for 2G"""
    stations = build_station_list()
    update_water_levels(stations)
    stations = stations_level_over_threshold(stations, 1.3)
    for station, relative_water_level in stations[:5]:
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=5))
        if len(levels) == 0:
            print("NO DATA FOR THIS STATION")
            continue
        plot_water_level_with_fit(station, dates, levels, 10)
        print(relative_water_level)
        polynomial, offset = polyfit(dates, levels, 10)
        for _ in range(72):
            dates.append(dates[-1]+datetime.timedelta(hours=1))
            levels.append(polynomial(matplotlib.dates.date2num(dates[-1])-offset))
        print(dates)
        plot_water_levels(station, dates, levels)


    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()