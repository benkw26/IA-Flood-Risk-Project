import plotly.express as px
import pandas as pd
from floodsystem.stationdata import build_station_list

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
    station_list = build_station_list()

    for station in station_list:
        station_name_list.append(station.name)
        station_id_list.append(station.station_id)
        measure_id_list.append(station.measure_id)
        lat_list.append(station.coord[0])
        lon_list.append(station.coord[1])
        river_list.append(station.river)
        town_list.append(station.town)

    return pd.DataFrame(list(zip(station_name_list,station_id_list,measure_id_list,lat_list,lon_list,river_list,town_list)),
    columns = ["Station Name", "Station Id", "Measure Id", "Latitude", "Longtitude", "River", "Town"])

def run():
    """Requirements for Optional Task 1.1"""
    station_data  = generate_dataframe()
    fig = px.scatter_mapbox(station_data, lat = "Latitude", lon="Longtitude", hover_name = "Station Name",
    hover_data = ["Latitude", "Longtitude", "River", "Town"], color_discrete_sequence=["fuchsia"], zoom = 3, height = 300)
    fig.update_layout(mapbox_style = "dark", mapbox_accesstoken = mapbox_token)
    fig.update_layout(margin = {"r":0,"t":0,"l":0,"b":0})
    fig.show()

if __name__ == "__main__":
    print("*** Optional Task 1.1: CUED Part IA Flood Warning System ***")
    run()