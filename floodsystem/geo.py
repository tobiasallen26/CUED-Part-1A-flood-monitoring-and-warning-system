# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """This returns a list of tuples in the form (station, distance) where the distance is the 
    haversine distance of the station from a location p"""
    station_distance = []
    for s in stations:
        station_distance.append((s, haversine(s.coord, p)))
    
    station_distance = sorted_by_key(station_distance, 1)
    return station_distance

def rivers_with_stations(stations):
    """This returns a list of all the rivers which have monitoring stations on them"""
    rivers = []
    for s in stations:
        if s.river not in rivers:
            rivers.append(s.river)
    return rivers

def stations_by_river(stations):
    """This returns a dictionary which holds lists of all the different stations on a river"""
    rivers_to_stations = {}
    for s in stations:
        if s.river not in rivers_to_stations:
            rivers_to_stations[s.river] = [s.name]
        else:
            rivers_to_stations[s.river].append(s.name)
    return rivers_to_stations
