
def stations_highest_rel_level(stations, N):
    """
    returns the stations with the highest relative water level

    Inputs
    ------
    stations: list of MonitoringStation objects
    N: int, the number of stations to return

    Returns
    ------
    returns the N stations that have the highest relative water level in descending order
    """
    
    station_level_list = stations_level_over_threshold(stations, 0.0)
    return station_level_list[:N]

