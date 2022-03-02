
from floodsystem.flood import stations_highest_rel_level

def test_2C():
    stations = []
    length = stations_highest_rel_level(stations,15)
    assert len(length)==15
    #assert correct length of returned list
    
    


