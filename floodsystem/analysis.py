import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    x = np.array(matplotlib.dates.date2num(dates))
    p_coeff = np.polyfit(x-x[0], levels, p)
    # x-x[0] for the gregorian calendar
    poly = np.poly1d(p_coeff)

    return (poly, x[0])
    
