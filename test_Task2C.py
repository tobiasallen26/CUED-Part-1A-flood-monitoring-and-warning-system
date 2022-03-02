from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels


def test_2C():
    assert len(stations_highest_rel_level)==15
    #assert correct length of returned list
    
    


