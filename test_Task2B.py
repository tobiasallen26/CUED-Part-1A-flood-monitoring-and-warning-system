from sqlalchemy import over
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def test_relative_water_level():
    """ tests requiremnts of relative water level"""
    station  = MonitoringStation(None, None, None, None, (1, 2), None, None)
    # tests for no data
    assert station.relative_water_level() == None
    # tests for data in the range
    station.latest_level = 1.5
    assert station.relative_water_level() == 0.5
    # tests for data outside of the range
    station.latest_level = 2.5
    assert station.relative_water_level() == 1.5
    station.latest_level = 0.5
    assert station.relative_water_level() == -0.5
    # tests for inconsistent data
    station.latest_level = 'a'
    assert station.relative_water_level() == None


def test_stations_level_over_threshold():
    """tests requirements of stations level over threshold"""
    # creates a list of stations
    stations = []
    for level in [1, None, 2, 3, 'b', 5, 6, 7]:
        x = MonitoringStation(None, None, None, None, (1, 3), None, None)
        x.latest_level = level
        stations.append(x)
    stations[-1].typical_range = (3, 1)
    over_threshold = stations_level_over_threshold(stations, 1)
    # checks for the expected length of the list returned
    assert len(over_threshold) == 2
    # checks the ordering of list
    assert over_threshold[0][1] == 2
    assert over_threshold[1][1], 2 == 2.5
