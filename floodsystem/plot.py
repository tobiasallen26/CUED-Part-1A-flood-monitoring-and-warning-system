from turtle import window_height, window_width
import matplotlib.pyplot as plt
import numpy as np
from floodsystem.analysis import polyfit
import matplotlib

def plot_water_levels(station, dates, levels, fit=False):
    """ plots a graph of water level against dates for a station"""
    if len(levels) == 0:
        print("NO DATA FOR THIS STATION")

    plt.figure(figsize=(8, 3))

    # plots the typical range if typical range is available
    if station.typical_range_consistent():
        high_range = np.linspace(station.typical_range[1], station.typical_range[1], len(dates))
        low_range = np.linspace(station.typical_range[0], station.typical_range[0], len(dates))
        plt.plot(dates, high_range)
        plt.plot(dates, low_range)

    # plots the dates and levels and adds labels and title
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    print(station.name)
    if not fit:
        plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """ plots a graph of water level against dates for a with polynomial"""
    if len(levels) == 0:
        print("NO DATA FOR THIS STATION")

    # uses plot_water_levels but runs it so that the plot isn't shown until
    #  the polynomial has also be calculated and ploted
    plot_water_levels(station, dates, levels, fit=True)
    polynomial, offset = polyfit(dates, levels, p)
    x = np.array(matplotlib.dates.date2num(dates))
    plt.plot(x, polynomial(x-offset))
    plt.show()