import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 10000)
pd.set_option('display.expand_frame_repr', False)

# Value in m/s = value in fps × 0.3048

sound_speed_ms = 343

feet_to_meters_factor = 0.3048
yards_to_meters_factor = 0.9144

win_308_speed_fps = 2650

win_308_speed_ms = win_308_speed_fps * feet_to_meters_factor

datas_308 = pd.read_csv("308_chart.csv")

# Add new column velocity (ms)
datas_308["Vélocité (ms)"] = datas_308["Velocity (fps)"] * feet_to_meters_factor

# Add new column range in meters
datas_308["Range (meters)"] = datas_308["Range (yards)"] * yards_to_meters_factor

print(datas_308["Vélocité (ms)"])

print(datas_308)

# https://sciencing.com/what-does-g-force-mean-13710432.html

#
# (C) is the drag coefficient of the bullet,
# (ρ) is the air density,
# (A) is the area of the bullet,
# (t) is the time of flight and
# (m) is the mass of the bullet.
#

drag_coef     = 0.295 #
air_density   = 1.2 # kg/cubic meter at normal pressure and temperature
bullet_area   = 4.8 * 10**-5 # m² cross-sectional area the value for a .308 caliber*
initial_speed = 823
bullet_mass   = 0.016 # kg

def distance_over_time(drag, air_dens, area, init_speed, flight_time, mass_of_bullet, debug=False):
    # Calculate distance x by time
    flight_time = round(flight_time, 2)
    x = (init_speed * flight_time) - (drag * air_dens * area * (init_speed**2) * (flight_time**2)) / (2 * mass_of_bullet)
    if debug:
        print(f'drag : {drag} | '
              f'init_speed : {init_speed} | '
              f'air_density : {air_dens} | '
              f'area : {area} | '
              f'init speed : {init_speed} | '
              f'flight time : {flight_time} | '
              f'mass of bullet : {mass_of_bullet}')
    return x


print(distance_over_time(drag_coef, air_density, bullet_area, 400, 0.452, bullet_mass))

y = list()
x = list()

for time in np.arange(0, 3, 0.01):
    x.append(time)
    y.append(distance_over_time(drag_coef, air_density, bullet_area, 823, time, bullet_mass))

"""
plt.plot(x, y, 'o', label='bullet distance over time')
plt.title('bullet distance over time')
plt.xlabel('temps')
plt.ylabel('distance')
plt.grid(axis = 'both')
plt.legend(loc='upper center')
plt.show()

"""

print(distance_over_time(drag_coef, air_density, bullet_area, 823, time, bullet_mass))


# m, la masse de l'objet ;
# rho, désigne la masse volumique de l'air ;
# s, le maître-couple, section droite perpendiculaire au mouvement ;
# Cx, le coefficient de résistance « aérodynamique »;
# v, la vitesse de l'objet.

# Nous allons d’abord déterminé la force de traînée en Newtons
# Fd = 0.5*m*(v2² - v1²)/d
# v1 la vitesse initiale en m/s,
# v2 la vitesse résiduelle au point du 2 ème chronographe en m/s,
# d  la distance entre les 2 points de mesure en m,
# m le poids de la balle en kg

def calculate_queue(v1, v2, d, m):
    """
    Fd = 0.5*m*(v2² - v1²)/d
    calculate queue in Newton
    :return: fd in N
    """
    return 0.5 * m * (v2**2 - v1**2) / d

# http://ballisticshooters.over-blog.com/2019/09/le-coefficient-balistique.html
#
# Ensuite nous déterminerons le Cx
# Cx = Fd / ½ρv² *A  soit  2*Fd / (A*v²*ρ)
# A la surface de la balle en m² (π r²)
# V la vitesse moyenne entre les 2 points de vitesse en m/s
# ρ (rho) la densité de l’air en kg/m3


# Il va nous falloir déterminer la densité de l’air en kg/m3
# ρ = 1 / (287.06 * (υ + 273.15)) * (p - 230.617 *  φ * exp [(17.5043 * υ) / (241.2 + υ)]
#
# φ l’humidité relative en %
# υ la température en °C
# p la pression en Pa

# Prenons une balle de 7 mm  de 180 grains
# Conditions du tir : 25°C, 916 Hpa et 50% d’humidité relative
# V1 = 985 m/s à la bouche, v2 = 784 m/s à 500 m


mass =
rho =
maitre_couple =
drag_coef =
speed_object =

def simple_speed_through_time():
