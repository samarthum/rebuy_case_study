import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import os
from pathlib import Path

plt.style.use('fivethirtyeight')

from src import config

def read_data(fname):
    """
    Reads in the dataset from the /data folder

    Parameters
    ----------
    fname : str
        Name of the csv file.

    Returns
    -------
    data: DataFrame

    """
    data = pd.read_csv(config.DATA_PATH / fname)
    data.columns = [col.lower() for col in data.columns]
    
    return data


def time_aggregate_data(ts_data):
    """
    Aggregates the given time series data w.r.t. day, week, month and quarter.
    Expects a datetime column 'date' using which aggregation is performed.

    Parameters
    ----------
    ts_data : DataFrame
        Timeseries dataframe with datetime index.

    Returns
    -------
    daily, weekly, monthly, quarterly aggregations

    """
    ts_data = ts_data.copy()
    daily = ts_data.resample('D').sum()
    weekly = ts_data.resample('W').sum()
    monthly = ts_data.resample('M').sum()
    quarterly = ts_data.resample('Q').sum()
    
    return daily, weekly, monthly, quarterly


def plot_ts_data(ts_data):
    """
    Time series plot of data at multiple levels:
        daily, daily with MA, weekly, monthly and quarterly

    Parameters
    ----------
    ts_data : DataFrame
        Timeseries data with datetime index.
    """
    plot_params = {'linewidth': config.lw, 'figsize': config.FIGSIZE}
    daily, weekly, monthly, quarterly = time_aggregate_data(ts_data)

    daily.plot(**plot_params)
    plt.title('Daily')
    plt.show();

    daily.rolling(7).mean().plot(**plot_params)
    plt.title('Daily (7-day MA)')
    plt.show();

    weekly.plot(**plot_params)
    plt.title('Weekly')
    plt.show();

    monthly.plot(**plot_params)
    plt.title('Monthly')
    plt.show();

    quarterly.plot(**plot_params)
    plt.title('Quarterly')
    plt.show();
    
    
def plot_decomposed(ts_data):
    """
    Plots the seasonal decomposition of the given timeseries data.

    Parameters
    ----------
    ts_data : DataFrame
        Timeseries data with a datetime index.
    """
    decomposed = sm.tsa.seasonal_decompose(ts_data)
    figure = decomposed.plot()
    figure.set_figheight(13)
    figure.set_figwidth(15)
    figure.tight_layout()
    for ax in figure.axes:
        for line in ax.lines:
            line.set_linewidth(config.lw)
    plt.show();
    
    
def plot_by_day_of_week(ts_data, title=None, xlabel=None, ylabel=None):
    """
    Plots a barplot for the given daily timeseries data, aggregated by the day of the
    week.

    Parameters
    ----------
    ts_data : DataFrame
        Timeseries data with a datetime index.
    """
    ts_data['day_of_week'] = ts_data.index.dayofweek
    ts_data.groupby('day_of_week')['quantity'].mean().plot(kind='bar')
    
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    
    plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6],
               labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 
               rotation=0);