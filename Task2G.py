from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
import matplotlib
import datetime

CHECK_FOR_FLOOD_THRESHOLD = 1.2
POLYNOMIAL_ORDER = 5
AVG_CHANGE_SAMPLE_SIZE = 30
FLOODED_THRESHOLD = 2
POLYNOMIAL_FLOOD_WARNING_THRESHOLD = 1.8
FLOOD_WARNING_SAMPLE_GRADIENT_THRESHOLD = 0

def run():
    """Demonstration task for 2G"""
    stations = build_station_list()
    update_water_levels(stations)
    stations = stations_level_over_threshold(stations, CHECK_FOR_FLOOD_THRESHOLD)
    for station, relative_water_level in stations:
        original_dates, original_levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=5))
        if len(original_levels) == 0:
            print("NO DATA FOR THIS STATION: {}".format(station.name))
            continue
        # plot_water_level_with_fit(station, original_dates, original_levels, POLYNOMIAL_ORDER)
        # print(relative_water_level)
        
        dates, levels = original_dates, original_levels
        avg_change = 0
        for i in range(len(levels[:AVG_CHANGE_SAMPLE_SIZE])-1):
            avg_change += levels[i] - levels[i+1]
        avg_sample_gradient = avg_change/AVG_CHANGE_SAMPLE_SIZE

        for _ in range(12):
            dates = [dates[0] + datetime.timedelta(hours=1)] + dates
            levels = [levels[0] + avg_change/AVG_CHANGE_SAMPLE_SIZE] + levels
        # plot_water_levels(station, dates, levels)
        # plot_water_level_with_fit(station, dates, levels, POLYNOMIAL_ORDER)
        
        polynomial, offset = polyfit(dates, levels, POLYNOMIAL_ORDER)
        polynomial_final_height = polynomial(matplotlib.dates.date2num(dates[0])-offset)
        polynomial_final_relative_height = (polynomial_final_height - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])

        current_flood_status = 'NOT FLOODED'
        if relative_water_level > FLOODED_THRESHOLD:
            current_flood_status = 'FLOODED'
        flood_warning_outcomes = ['NO WARNING', 'LOW LEVEL WARNING', 'HIGH LEVEL WARNING']
        n = [polynomial_final_relative_height > POLYNOMIAL_FLOOD_WARNING_THRESHOLD,
            avg_sample_gradient > FLOOD_WARNING_SAMPLE_GRADIENT_THRESHOLD].count(True)
        current_flood_warning_status = flood_warning_outcomes[n]

        print(station, '\n',
        'CURRENT FLOOD STATUS: {}\n'.format(current_flood_status),
        'CURRENT FLOOD WANRING STATUS: {}\n'.format(current_flood_warning_status))
        plot_water_level_with_fit(station, original_dates, original_levels, POLYNOMIAL_ORDER)


    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()