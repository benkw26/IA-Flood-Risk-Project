from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    # Store the coordinates of Cambridge City Centre
    CambCoord = (52.2053, 0.1218)
    #store the radius value
    radius = 10

    near_cambstations = stations_within_radius(stations, CambCoord, radius)
    print(sorted([station.name for station in near_cambstations]))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()