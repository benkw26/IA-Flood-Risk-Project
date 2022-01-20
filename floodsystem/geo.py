# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa



def rivers_with_station(stations):
    """Given a list of stations, returns a tuple of (river, monitoring station).
    Optional parameter index: Returns the first 'index' number(s) of rivers in alphabetical order"""
    river_station_list = [(station.river, station.name) for station in stations]
    return river_station_list

    
def stations_by_river(stations):
    "Given a list of station, returns a dictionary that maps the river names to a list of station objects on the corresponding river."
    
    river_list = list(set([station.river for station in stations]))
    river_dict = {}
    for river in river_list:
        station_list = []
        for station in stations: 
            if station.river == river:
                station_list.append(station.name)
        river_dict[river] = station_list
    return river_dict
            