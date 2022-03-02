from floodsystem.analysis import plot_water_level_with_fit
from floodsystem.analysis import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.analysis import polyfit
import matplotlib.pyplot as plt
import matplotlib as pt
import datetime

stations = build_station_list()
update_water_levels(stations) 
#updating the water levels to most recent water levels.


