from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_distance_sort():
    """Unit test for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    # Store the coordinates of Cambridge City Centre
    CambCoord = (52.2053, 0.1218)

    distance_list = stations_by_distance(stations, CambCoord)
    assert distance_list[0][0].town == "Cambridge"