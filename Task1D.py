from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # Print number of rivers with stations along with the list of rivers
    index = 10 # Optional parameter
    rivers_with_station(stations, index) 

    # Returns a list of stations corresponding to each river in the list
    station_testlist = ["River Aire", "River Cam", "River Thames"] # Optional parameter
    stations_by_river(stations, station_testlist)
    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()