import plotly.express as px
import pandas as pd
from floodsystem.stationdata import build_station_list, update_water_levels

mapbox_token = "pk.eyJ1IjoiaWRlYWxpc3RtYXR0aGV3IiwiYSI6ImNreW5lc2FpajA2dTAyb295bTRuOGN6ajIifQ.iTd3Hrq_zVhXe6taDSGnlw"
# px.set_mapbox_access_token(mapbox_token)

def generate_dataframe():
    """
    Generates a pandas Dataframe Object from the station data given.

    Inputs
    ------

    Returns
    -------
    Dataframe object with information of stations
    """
    station_name_list = []
    station_id_list = []
    measure_id_list = []
    lat_list = []
    lon_list = []
    river_list = []
    town_list = []
    water_level_list = []
    level_situation = []
    station_list = build_station_list()
    update_water_levels(station_list)

    for station in station_list:
        station_name_list.append(station.name)
        station_id_list.append(station.station_id)
        measure_id_list.append(station.measure_id)
        lat_list.append(station.coord[0])
        lon_list.append(station.coord[1])
        river_list.append(station.river)
        town_list.append(station.town)
        water_level = station.relative_water_level()
        water_level_list.append(water_level)

        if water_level == None:
            level_situation.append("No Data")
        else:
            level_situation.append(station.risk_level)


    return pd.DataFrame(list(zip(station_name_list,water_level_list,level_situation, station_id_list,measure_id_list,lat_list,lon_list,river_list,town_list)),
    columns = ["Station Name", "Relative Water Level", "Water Level Situation", "Station Id", "Measure Id", "Latitude", "Longtitude", "River", "Town"])