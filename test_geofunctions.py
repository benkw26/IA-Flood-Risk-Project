from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine

def test_distance_sort():
    """Unit test for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    # Store the coordinates of Cambridge City Centre
    CambCoord = (52.2053, 0.1218)

    distance_list = stations_by_distance(stations, CambCoord)
    assert distance_list[0][0].town == "Cambridge"

def test_radius_sort():
    "Unit Test for Task 1C"

    # Build list of stations
    stations = build_station_list()
    # Store the coordinates of Cambridge City Centre
    CambCoord = (52.2053, 0.1218)
    close_stations = stations_within_radius(stations, CambCoord, 10)

    assert haversine(close_stations[0].coord, CambCoord) <= 10

