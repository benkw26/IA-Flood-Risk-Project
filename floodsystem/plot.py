import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
from .analysis import polyfit
from matplotlib.dates import date2num

def plot_water_levels(station, dates, levels, use_plt = True):
    """
    Plot a graph of the variation of the relative water levels with dates.

    Inputs
    -------
    station: MonitoringStation Object
    dates: a list of datetime objects
    levels: a list of water levels corresponding to the dates
    use_plt: True if using matplotlib and False if using plotly (web-based plotter)

    Returns
    -------
    """
    if use_plt:

        plt.plot(dates, levels)

        plt.xlabel("Date")
        plt.ylabel("Relative Water Level")
        plt.xlim(dates[-1], dates[0])
        plt.xticks(rotation = 45)
        plt.title(station.name)

        plt.tight_layout()
    
    else:
        df = pd.DataFrame(list(zip(dates, levels)), columns = ["Dates", "Levels"]) 
        fig = px.line(df, x = "Dates", y = "Levels", title = station.name)
        fig.show()

def generalised_plot_water_levels(station_list, dates, levels):
    """
    Generalised function to plot variation of relative water levels at multiple stations with dates.

    Inputs
    ------
    station_list: a list of MonitoringStation Objects
    dates: a list of datetime objects
    levels: a list of water levels corresponding to the dates

    Returns
    -------    
    """
    fig, axes = plt.subplots(len(station_list), figsize = (10,15))
    for ax, station, date, level in zip(axes, station_list, dates, levels):
        ax.plot(date, level)
        ax.set_title(station.name)
    axes[-1].set_xlabel("Date")
    axes[0].set_ylabel("Relative Water Level")
    plt.tight_layout(pad = 0, w_pad = 0.3, h_pad = 2.0)
    plt.show()
    
def plot_water_level_with_fit(station, dates, levels, p):
    """
    Plots variation of relative water levels with dates, along with an pth order polynomial best fit line.

    Inputs
    ------
    station: MonitoringStation Object
    dates: a list of datetime objects
    levels: a list of water levels corresponding to the dates
    p: int, the order of best-fit polynomial

    Returns
    -------    
    """

    x = date2num(dates)
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates, poly(x-d0))

    plt.xlabel("Date")
    plt.ylabel("Relative Water Level")
    plt.xlim(dates[-1], dates[0])
    plt.xticks(rotation = 45)
    plt.title(station.name)
