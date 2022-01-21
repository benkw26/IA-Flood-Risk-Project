"""Unit test for the flood module"""
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    "Unit test for Task 2B"

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    assert stations_level_over_threshold(stations, 0.8)[0][1] > 0.8

def test_stations_highest_rel_level():
    "Unit test for Task 2C"
    stations = build_station_list()
    update_water_levels(stations)

    N = 10
    for i in range(N-1):
        print(stations_highest_rel_level(stations, N)[i][1],stations_highest_rel_level(stations, N)[i+1][1])