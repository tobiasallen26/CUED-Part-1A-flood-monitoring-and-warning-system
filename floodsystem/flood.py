from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """ this returns a list of tuples where the relative water level is over tol"""
    over_threshold_list = []
    for s in stations:
        rwl = s.relative_water_level()
        if rwl is not None and rwl > tol:
            over_threshold_list.append((s, rwl))
    return sorted_by_key(over_threshold_list, 1, reverse=True)
