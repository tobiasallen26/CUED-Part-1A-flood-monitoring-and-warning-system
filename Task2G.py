from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
import matplotlib
import datetime

# constants which affect issuing warning
CHECK_FOR_FLOOD_THRESHOLD = 1.0
POLYNOMIAL_ORDER = 5
AVG_CHANGE_SAMPLE_SIZE = 30
FLOODED_THRESHOLD = 1.6
RELATIVE_WATERLEVEL_WARNING_THRESHOLD = 1.2
POLYNOMIAL_FLOOD_WARNING_THRESHOLD = 1.4
FLOOD_WARNING_SAMPLE_GRADIENT_THRESHOLD = 0.0

def run():
    """Demonstration task for 2G"""
    # builds and updates a list of stations
    stations = build_station_list()
    update_water_levels(stations)
    # narrows the list of stations to those with a relative water level over a set threshold
    stations = stations_level_over_threshold(stations, CHECK_FOR_FLOOD_THRESHOLD)
    stations_at_risk = {'LOW':[], 'MODERATE':[], 'HIGH':[], 'SEVERE':[]}
    # iterates through the stations
    for station, relative_water_level in stations:
        # gets past data and ends check for station if there is no historic data
        original_dates, original_levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=5))
        if len(original_levels) == 0:
            print("NO DATA FOR THIS STATION: {}".format(station.name))
            continue
        
        # calculates the average change of the water level for the most recent set of data
        dates, levels = original_dates, original_levels
        avg_change = 0
        for i in range(len(levels[:AVG_CHANGE_SAMPLE_SIZE])-1):
            avg_change += levels[i] - levels[i+1]
        avg_sample_gradient = avg_change/AVG_CHANGE_SAMPLE_SIZE

        # adds a linear region to the end of the graph of water level which goes 12 hours ahead
        # of the most recent data. this means that the polynomial can be used to predict water 
        # level for ahead of the most recent time as it will not go to extreme values due to the 
        # polynomial only being calculated to fit the data in the known region
        for _ in range(24):
            dates = [dates[0] + datetime.timedelta(hours=0.5)] + dates
            levels = [levels[0] + avg_change/AVG_CHANGE_SAMPLE_SIZE] + levels
        
        # calculates the polynomial and the 12 hours ahead relative water level
        polynomial, offset = polyfit(dates, levels, POLYNOMIAL_ORDER)
        polynomial_final_height = polynomial(matplotlib.dates.date2num(dates[0])-offset)
        polynomial_final_relative_height = (polynomial_final_height - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])

        # works out the current flood status and what the flood warning will be
        current_flood_status = 'NOT FLOODED'
        if relative_water_level > FLOODED_THRESHOLD:
            current_flood_status = 'FLOODED'
        # flood warning is worked out by which how many of the indicators are true
        flood_warning_outcomes = ['LOW', 'MODERATE', 'HIGH', 'SEVERE']
        n = [relative_water_level > RELATIVE_WATERLEVEL_WARNING_THRESHOLD, 
        polynomial_final_relative_height > POLYNOMIAL_FLOOD_WARNING_THRESHOLD,
        avg_sample_gradient > FLOOD_WARNING_SAMPLE_GRADIENT_THRESHOLD, 
        relative_water_level > FLOODED_THRESHOLD].count(True)
        if n-1 < 0:
            n = 1
        current_flood_warning_status = flood_warning_outcomes[n-1]

        # adds the station to the risk dictionary
        stations_at_risk[current_flood_warning_status].append(station)
        print(station, '\n',
        'CURRENT FLOOD STATUS: {}\n'.format(current_flood_status),
        'CURRENT FLOOD WANRING STATUS: {}\n'.format(current_flood_warning_status))
        # plot_water_level_with_fit(station, original_dates, original_levels, POLYNOMIAL_ORDER)

    # displays towns at risk by taking the towns of each of the stations
    for key, value in stations_at_risk.items():
        print('The towns with a {} flood warning are: {}'.format(key, 
        [station.town for station in value]))

    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()