import matplotlib.pyplot as plt
from datetime import date, timedelta
import numpy as np


def cos_d(degrees):
    """ To save us converting to radians all the time """
    return np.cos(np.radians(degrees))


def sin_d(degrees):
    """ To save us converting to radians all the time """
    return np.sin(np.radians(degrees))


def asin_d(n):
    """ Returns the degrees such that sin(degrees) == n
    This is also know as the inverse sin function or arcsin.
    The stanard asin function returns the value in radians.
    This function converts the result to degrees
    """
    return np.degrees(np.arcsin(n))


def times_across_day(number_of_times):
    """returns a numpy array of evenly spaced times between 0 and 24 inclusive. There should be number_of_times values in the array."""
    return (np.linspace(0, 24, number_of_times))


def nice_date_str(day_num):
    """ Returns a human-readable date string for the date that is
    day_num days after 1 Jan 2022. For example,
    day 0 -> 01 Jan
    day 364 -> 31 Dec
    The day number should be between 0 and 364, inclusive.
    Values greater than 364 will roll over into subsequent years!
    Don't worry too much about how this works.
    """
    day_num = int(day_num)  # deals with numpy ints, etc.
    base_date = date(2022, 1, 1)
    delta = timedelta(days=day_num)
    the_date = base_date + delta
    return the_date.strftime('%d %b')


def solar_declination(day_num, solar_hour):
    """ Returns the angle of the sun's rays and the
    plane of the earth's equator, for the given day
    number and solar hour.
    """
    n = day_num + solar_hour / 24
    beta = 360 /365 * (n + 10)
    return -23.44 * cos_d(beta)


def solar_hour_angle(solar_hour):
    """ This function returns the angle implied by
    a given hourly time, relative to the solar noon.
    For hours before noon (12) the angle should be
    negative and for hours after noon it should be
    positive.
    """
    return 15 * (solar_hour - 12)


def solar_elevation(latitude, day_num, solar_hour):
    """ Returns the elevation of the sun relative to the ground """
    hour_angle = solar_hour_angle(solar_hour)
    declination = solar_declination(day_num, solar_hour)
    elevation = asin_d(sin_d(latitude) * sin_d(declination) +
                       cos_d(latitude) * cos_d(hour_angle) * cos_d(declination))
    return elevation


def plot_elevations_over_day(latitude, day_num, number_of_points):
    """Plots the elevation of the sun over a given day at a given latitude."""

    sun_elevation_date = nice_date_str(day_num)

    axes = plt.axes()
    axes.grid(True)

    x_values = times_across_day(number_of_points)
    y_values = solar_elevation(latitude, day_num, x_values)
    axes.plot(x_values, y_values, linestyle = "", marker = "o" ,markersize = "16", color = "orange")

    axes.set_xlabel("Solar hour")
    axes.set_ylabel("Solar elevation (degrees)")
    axes.set_title(f"Solar elevations for day = {sun_elevation_date}, latitude = {latitude:.2f}")

    x_ticks_values = range(0 ,25 ,1)
    y_ticks_values = range(-90 ,93 ,10)
    axes.set_yticks(y_ticks_values)
    axes.set_xticks(x_ticks_values)

    plt.show()

def plot_noon_elevations_over_year(latitude):
    """writing a function which will give a graph of the solar elevations
       at a given latitude and date
    """
    axes = plt.axes()
    axes.grid(True)
    x = np.linspace(0 ,365)
    y = solar_elevation(latitude ,x ,12)
    axes.plot(x, y, linestyle="-" ,marker="None" ,color="orange")

    xticks = range(0 ,364 ,30)
    yticks = range(-90 ,100 ,10)
    axes.set_yticks(yticks)
#    axes.set_xticks(nice_date_str(xticks))
    axes.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

#    axes.set_xlabels("Day")
#    axes.set_yticklabels("Noon solar elevation (degrees)")
    axes.set_title(f"Daily noon solar elevations at latitude={latitude:.2f}")
    plt.tight_layout()
    plt.show()

#plot_noon_elevations_over_year(-43.52565)
plot_noon_elevations_over_year(90.52565)

