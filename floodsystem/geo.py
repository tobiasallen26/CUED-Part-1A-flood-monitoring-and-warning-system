# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    station_distance = []
    for s in stations:
        station_distance.append((s, haversine(s.coord, p)))
    
    station_distance = sorted_by_key(station_distance, 1)
    return station_distance

def rivers_with_stations(stations):
    rivers = []
    for s in stations:
        if s.river not in rivers:
            rivers.append(s.river)
    return rivers
