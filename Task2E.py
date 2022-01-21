import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task2E"""

    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)

    stat = stations_highest_rel_level(stations,5)
    for station in stat:
        dt = 10
        print(station.measure_id)
        dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
