"""Unit test for the flood module"""
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

def test_stations_highest_rel_level():
    "Unit test for Task 2C"
    stations = build_station_list()
    N = 5
    for i in range(N):
        assert stations_highest_rel_level(stations, N)[i][1] >= stations_highest_rel_level(stations, N)[i+1][1]

