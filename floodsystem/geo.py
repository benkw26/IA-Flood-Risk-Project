# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa



def rivers_with_station(stations, index = 10):
    """Given a list of stations, returns a tuple of (river, monitoring station).
    Optional parameter index: Returns the first 'index' number(s) of rivers in alphabetical order"""

    river_list = list(set([station.river for station in stations]))
    river_sortedlist = sorted(river_list)
    river_station_list = [(station.river, station.name) for station in stations]
    no_of_rivers = len(river_sortedlist)
    if index > no_of_rivers:
        index = 10
    river_displaylist = river_sortedlist[0:index]
    print(f"{no_of_rivers} stations. The first {index} - {river_displaylist}\n")
    return river_station_list

    
def stations_by_river(stations, station_testlist = ["River Aire", "River Cam", "River Thames"]):
    """Given a list of station, returns a dictionary that maps the river names to a list of station objects on the corresponding river.
    Optional parameter station_testlist: Prints a list of stations at a river for each river in the list"""
    
    river_list = list(set([station.river for station in stations]))
    river_dict = {}
    for river in river_list:
        station_list = []
        for station in stations:
            if station.river == river:
                station_list.append(station.name)
        river_dict[river] = station_list
    for i in station_testlist:
        print(f"{river_dict[i]}\n")
    return river_dict
            