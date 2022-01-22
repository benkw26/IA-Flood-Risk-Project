from floodsystem.station import consistent_typical_range_stations

from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
stations = consistent_typical_range_stations(stations)
update_water_levels(stations)
