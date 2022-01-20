from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    # Print number of rivers with stations along with the list of rivers
    #index = 10 # Optional parameter
    #rivers_with_station(stations, index) 
    river_list = list(set(rivers_with_station(stations)[i][0] for i in range(len(stations))))
    no_of_rivers = len(river_list)
    river_sortedlist = sorted(river_list)
    river_displaylist = river_sortedlist[0:10]
    print(f"{no_of_rivers} stations. The first 10 - {river_displaylist}\n")

    # Returns a list of stations corresponding to each river in the list
    station_testlist = ["River Aire", "River Cam", "River Thames"]
    for i in station_testlist:
        print(f"{stations_by_river(stations)[i]}\n")
    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()