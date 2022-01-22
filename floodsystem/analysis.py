import datetime
import numpy as np
from matplotlib.dates import date2num

from floodsystem.datafetcher import fetch_measure_levels

def polyfit(dates, levels, p):

    x = np.array(date2num(dates))
    y = levels

    d0 = x[0]

    p_coeff = np.polyfit(x - d0, y, p)

    poly = np.poly1d(p_coeff)

    return poly, d0
