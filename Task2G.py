import datetime
from matplotlib.dates import date2num

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.station import consistent_typical_range_stations
from Flood_Map_Display import generate_dataframe

def run():
    """Requirements for Task 2G"""

    stations = build_station_list()
    stations = consistent_typical_range_stations(stations)
    update_water_levels(stations)

    for station in stations:
        dt, p = 2, 4
        try:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            t = date2num(dates)
            poly, d0 = polyfit(dates, levels, p)
            tmr = datetime.date.today() + datetime.timedelta(days=1)
            tmr_num = date2num(tmr)
            pred_rel_water_level = poly(tmr_num - d0)
        except:
            continue
        if pred_rel_water_level > 3:
            station.risk_level = "Severe"
        elif pred_rel_water_level >1:
            station.risk_level = "High"
        elif pred_rel_water_level > 0:
            station.risk_level = "Moderate"
        else:
            station.risk_level = "Low"

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
