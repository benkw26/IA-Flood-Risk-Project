
def stations_highest_rel_level(stations, N):
    station_level_list = stations_level_over_threshold(stations, 0.0)
    return station_level_list[:N]

