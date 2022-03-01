from turtle import window_height, window_width
import matplotlib.pyplot as plt
import numpy as np

def plot_water_levels(station, dates, levels):
    """ plots a graph of water level against dates for a station"""

    plt.figure(figsize=(8, 3))

    if station.typical_range_consistent():
        high_range = np.linspace(station.typical_range[1], station.typical_range[1], len(dates))
        low_range = np.linspace(station.typical_range[0], station.typical_range[0], len(dates))
        plt.plot(dates, high_range)
        plt.plot(dates, low_range)

    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    print(station.name)
    plt.show()