from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation
import datetime

def test_plot_water_levels():
    """ tests requirements for plot water levels"""
    station = MonitoringStation(None, None, 'Test Plot', None, None, None, None)

    dates = [datetime.datetime.utcnow() + datetime.timedelta(days=i) for i in range(10)]
    levels = [i for i in range(10)]
    plot_water_levels(station, dates, levels)