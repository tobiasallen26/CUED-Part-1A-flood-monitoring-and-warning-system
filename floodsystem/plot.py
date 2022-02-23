from turtle import window_height, window_width
import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    """ plots a graph of water level against dates for a station"""

    plt.figure(figsize=(8, 3))

    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    print(station.name)
    plt.show()