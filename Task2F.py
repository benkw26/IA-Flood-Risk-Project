import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
import numpy as np
import matplotlib.pyplot as plt

def run():
    """Requirements for Task2F"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    p = 4

    stat = stations_highest_rel_level(stations,5)
    for station in stat: 
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)
        plot_water_level_with_fit(station, dates, levels, p)
        if station.typical_range:
            y_low, y_high = station.typical_range[0], station.typical_range[1]
            plt.plot(dates, y_low*np.ones(len(dates)))
            plt.plot(dates, y_high*np.ones(len(dates)))
            plt.legend(["Actual", "Predicted", "Typical Low", "Typical High"])
        else:
            plt.legend(["Actual", "Predicted"])
        plt.show()

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
