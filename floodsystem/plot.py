import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

def plot_water_levels(station, dates, levels, use_plt = True):
    """
    Plot a graph of the variation of the water levels with dates.

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
        plt.ylabel("Water Level (m)")
        plt.xticks(rotation = 45)
        plt.title(station.name)

        plt.tight_layout()
        plt.show()
    
    else:
        df = pd.DataFrame(list(zip(dates, levels)), columns = ["Dates", "Levels"]) 
        fig = px.line(df, x = "Dates", y = "Levels", title = station.name)
        fig.show()

def generalised_plot_water_levels(station_list, dates, levels):
    """
    Generalised function to plot variation of water levels at multiple stations with dates.

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
    axes[0].set_ylabel("Water Level (m)")
    plt.tight_layout(pad = 0, w_pad = 0.3, h_pad = 2.0)
    plt.show()
    
    
