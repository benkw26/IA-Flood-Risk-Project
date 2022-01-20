from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    # Store the coordinates of Cambridge City Centre
    CambCoord = (52.2053, 0.1218)

    # sort the stations by distance
    distance_list = stations_by_distance(stations, CambCoord)
    # get closest and furthest stations
    closest_list = distance_list[:9]
    furthest_list = distance_list[-10:]

    # initialise lists to be returned
    formatted_closest_list = []
    formatted_furthest_list = []

    # formatting the closest and furthest list
    for station, distance in closest_list:
        formatted_closest_list.append((station.name, station.town, distance))
    
    for station, distance in furthest_list:
        formatted_furthest_list.append((station.name, station.town, distance))

    #  Printing out the deliverables
    print("The following is the 10 closest stations from  Cambridge City Centre")
    print(formatted_closest_list)
    print("The following is the 10 furthest stations from  Cambridge City Centre")
    print(formatted_furthest_list)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()