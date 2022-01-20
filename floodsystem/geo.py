# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa



def rivers_with_station(stations, index = 10):
    """Given a list of stations, returns a tuple of (river, monitoring station).
    Optional parameter index returns the first 'index' number of rivers in alphabetical order"""

    river_list = list(set([station.river for station in stations]))
    river_sortedlist = sorted(river_list)
    no_of_rivers = len(river_sortedlist)
    if index > no_of_rivers:
        index = 10
    river_displaylist = river_sortedlist[0:index]
    print(f"{no_of_rivers} stations. The first {index} - {river_displaylist}")
    return river_sortedlist

    
def stations_by_river(stations):
    "Given a list of station, returns a dictionary that maps the river names to a list of station objects on the corresponding river"
    
    for station in stations:
        [].append(station)