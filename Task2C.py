from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    N = 10
    for station in stations_highest_rel_level(stations, N):
        print(f"{station.name} {station.relative_water_level()}")

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()