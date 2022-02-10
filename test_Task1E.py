from floodsystem.geo import Rivers_by_Station_number
from floodsystem.station import MonitoringStation

def Test_code_rivers_by_station_number():
    Testlist = Rivers_by_Station_number(MonitoringStation, 11)
    assert Testlist[10][1] == Testlist[-1][1]
    "Checking if last river same as Nth river (11)"
    
