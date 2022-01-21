import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import generalised_plot_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task2E"""

    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)

    stat = stations_highest_rel_level(stations,5)
    date_list = []
    level_list = []
    for station in stat:
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=dt))
        date_list.append(dates)
        level_list.append(levels)
    generalised_plot_water_levels(stat, date_list, level_list)


if __name__ == "__main__":
    print("*** Task 2E (Optional Task 2): CUED Part IA Flood Warning System ***")
    run()