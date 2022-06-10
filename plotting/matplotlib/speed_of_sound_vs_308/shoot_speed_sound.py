import pandas as pd

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
