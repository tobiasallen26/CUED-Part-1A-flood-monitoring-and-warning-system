import matplotlib
from sympy import poly
from floodsystem.analysis import polyfit
import datetime

def test_polyfit():
    """ tests requirements for plot water levels"""
    # builds a set of levels and data for the polynomial 2x^2
    levels = [2*i**2 for i in range(100)]
    dates = [datetime.datetime(year = 2000, month = 1, day=1) + datetime.timedelta(days=i) for i in range(100)]
    polynomial, offset = polyfit(dates, levels, 2)
    # checks the the first coefficient is 2
    assert round(polynomial.c[0], 5) == 2
    # checks for the correct offset
    assert offset == matplotlib.dates.date2num(dates[0])
