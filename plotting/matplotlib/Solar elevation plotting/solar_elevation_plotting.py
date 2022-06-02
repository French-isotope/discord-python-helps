

import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta


def cos_d(degrees):
    """ To save us converting to radians all the time """
    return np.cos(np.radians(degrees))


def sin_d(degrees):
    """ To save us converting to radians all the time """
    return np.sin(np.radians(degrees))


def asin_d(n):
    """ Returns the degrees sucht sin(degrees) == n
    This is also know as the inverse sin function or arcsin.
    The stanard asin function returns the value in radians.
    This function converts the result to degrees
    """
    return np.degrees(np.arcsin(n))


def times_across_day(number_of_times):
    """return a numpy array of evenly spaced times"""
    return np.linspace(0 , 24, number_of_times)


def nice_date_str(day_num):
    """ Returns a human readable date string for the date that is
    day_num days after 1 Jan 2022. For example,
    day 0 -> 01 Jan
    day 364 -> 31 Dec
    The day number should be between 0 and 364, inclusive.
    Values greater than 364 will roll over into subsequent years!
    Don't worry too much about how this works.
    """
    print(day_num)
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
    beta = 360/365 * (n + 10)
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


def plot_noon_elevations_over_year(latitude):
    """writing a function which will give a graph of the solar elevations
       at a given latitude and date
    """
    axes = plt.axes()
    axes.grid(True)
    x = np.linspace(0,365)
    y = solar_elevation(latitude,x,12)
    axes.plot(x, y, linestyle="-",marker="None",color="orange")

    xticks_range = range(0,364,30)
    yticks = range(-90,100,10)

    xticks = []
    for day in xticks_range:
        nice_day = nice_date_str(day)
        xticks.append(nice_day)

    axes.set_yticks(yticks)

    # We need to correlate exactly the scale with the number of ticks with set_xticks(range())
    axes.set_xticks(range(0, (len(xticks) *30 ), 30))
    axes.set_xticklabels(xticks, fontdict=None, minor=False, rotation=70)

    axes.set_xlabel("Day")
    axes.set_ylabel("Noon solar elevation (degrees)")

    axes.set_title(f"Daily noon solar elevations at latitude={latitude:.2f}")
    plt.tight_layout()
    plt.show()

plot_noon_elevations_over_year(49.417)

