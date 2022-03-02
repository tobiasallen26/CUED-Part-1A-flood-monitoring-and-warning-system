from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def test_2C():
    stations = build_station_list()
    update_water_levels(stations)
    length = len(stations_highest_rel_level(stations,15))
    assert length==15
    #assert correct length of returned list
    
    


