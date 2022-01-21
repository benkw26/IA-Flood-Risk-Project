from .utils import sorted_by_key  

def stations_level_over_threshold(stations, tol):
    """
    Function that returns a list of (station, tol) tuples  with stations 
    at which the latest relative water level is over tol.

    Inputs
    ------
    stations: list of MonitoringStation objects
    tol     : float

    Returns
    ---------
    list of (station, tol) tuples  with stations 
    at which the latest relative water level is over tol sorted in descending order
    """
    exceeded_list = []
    for station in stations:
        water_lvl = station.relative_water_level()
        if water_lvl != None:
            if water_lvl > tol:
                exceeded_list.append((station, water_lvl))
    return sorted_by_key(exceeded_list,1, reverse = True)