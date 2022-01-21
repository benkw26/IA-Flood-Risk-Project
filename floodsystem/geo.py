# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""
This module contains a collection of functions related to
geographical data.
"""

import rlcompleter
from haversine import haversine, Unit
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    """
    Sorts stations by distance from closest to furthest from a coordinate p.

    Inputs
    ------
    stations: list of MonitoringStation objects
    p       : tuple of floats for the coordinate p

    Returns
    -------
    a list of (station, distance) tuples, where distance (float) is the distance
    of the station (MonitoringStation) from coordinate p. This list is sorted by distance
    """
    # Initialise a list to store answer
    station_distance_list = []
    # loop through all of the stations
    for station in stations:
        # calculate the distance between the stations and p
        dist = haversine(station.coord, p)
        # store the station and distance in the answer list
        station_distance_list.append((station, dist))
    # sort the list by distance and return the list
    return sorted_by_key(station_distance_list, 1)

def stations_within_radius(stations, centre, r):
    """
    returns stations within a certain radius r from the centre coordinate given

    Inputs
    ------
    stations: list of MonitoringStation objects
    centre  : tuple of floats for the coordinate p
    r       : float, radius of circle enveloping required stations

    Returns
    -------
    a list of stations (MonitoringStation) within a radius r of a geographic coordinate x
    """
    # Initialise list to store stations within a certain radius of centre
    within_list = []
    # loop through all the stations in the list
    for station in stations:
        # determine if the distance between station and the centre is less than the radius
        if haversine(station.coord, centre) <= r:
            within_list.append(station)
    
    return within_list

def rivers_with_station(stations):
    """
    returns a river-station pair

    Inputs
    ------
    stations: list of MonitoringStation objects

    Returns
    ------
    a list of of tuples in the form (river, station)
    """
    river_station_list = [(station.river, station.name) for station in stations]
    return river_station_list

    
def stations_by_river(stations):
    """
    returns a river and its corresponding rivers

    Inputs
    ------
    stations: list of MonitoringStation objects

    Returns
    ------
    a dictionary in the form {river : list of stations corresponding to the river}
    """
    
    river_list = list(set([station.river for station in stations]))
    river_dict = {}
    for river in river_list:
        station_list = []
        for station in stations: 
            if station.river == river:
                station_list.append(station.name)
        river_dict[river] = station_list
    return river_dict

def rivers_by_station_number(stations, N):
    """
    returns the rivers with the greatest number of stations

    Inputs
    ------
    stations: list of MonitoringStation objects
    N: int, the number of tuples to output
    *If there are more than 1 river that has the same number of stations as the Nth entry, the other stations are also included

    Returns
    ------
    a list of N* tuples of (river, number of stations) that has the greatest number of stations
    """

    river_dict = stations_by_river(stations)
    river_dict_keys = list(river_dict.keys())
    counter = 0

    number_river_tuple_list = [(river_dict_keys[i], len(river_dict[river_dict_keys[i]])) for i in range(len(river_dict))]
    sorted_list = sorted(number_river_tuple_list, key=lambda x: x[1], reverse=True)
    min_no_stations = sorted_list[N-1][1]

    for tuple in sorted_list:
        if tuple[1] >= min_no_stations:
            counter += 1
    
    return sorted_list[0:counter]

    
    