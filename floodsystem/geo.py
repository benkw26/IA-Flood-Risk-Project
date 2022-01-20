# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

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

