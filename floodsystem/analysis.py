import numpy as np
from matplotlib.dates import date2num

def polyfit(dates, levels, p):
    """
    Returns a np.poly1d object that best fits the dates and relative water levels

    INPUTS
    ------
    dates: a list of datetime objects
    levels: a list of water levels corresponding to the dates
    p: int, the order of best-fit polynomial
    
    RETURNS
    ------
    poly: np.poly1d object, a pth order order polynomial that best fits the dates and relative water levels
    d0: float, the number of days since the year 0001 
    """


    x = np.array(date2num(dates))
    y = levels

    d0 = x[0]

    p_coeff = np.polyfit(x - d0, y, p)
    poly = np.poly1d(p_coeff)

    return poly, d0
