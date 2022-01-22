# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town, catchment = None):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        self.catchment = catchment

        self.latest_level = None
        self.risk_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   catchment name: {}".format(self.catchment)
        return d

    def relative_water_level(self):
        """
        Returns the latest water level as a fraction of the typical range.

        Inputs
        ------

        Returns
        -------
        float, fraction of the typical range of water level (None if no relevant data)
        """
        if self.typical_range_consistent() and self.latest_level != None:
            low, high = self.typical_range
            return (self.latest_level- low)/(high-low)
        else:
            return None


    def typical_range_consistent(self):
        """This method checks whether the typical range exists and is consistent"""

        if self.typical_range is None:
            return False
        elif self.typical_range[0] < self.typical_range[1]:
            return True
        else:
            return False
    
def inconsistent_typical_range_stations(stations):
    """
    returns the stations that have missing or inconsistent typical range data

    Inputs
    ------
    stations: list of MonitoringStation objects

    Returns
    ------
    a list of stations that have missing or inconsistent typical range data
    """

    inconsistent_station_list = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_station_list.append(station)
    return inconsistent_station_list

def consistent_typical_range_stations(stations):
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    for station in inconsistent_stations:
        stations.remove(station)
    return stations