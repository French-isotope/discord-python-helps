import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Value in m/s = value in fps × 0.3048

sound_speed_ms = 343

feet_to_meters_factor = 0.3048

win_308_speed_fps = 2650

win_308_speed_ms = win_308_speed_fps * feet_to_meters_factor

datas_308 = pd.read_csv("308_chart.csv")

velocity_in_ms = datas_308["Velocity (fps)"] * feet_to_meters_factor

# Add new column velocity (ms)
datas_308["Vélocité (ms)"] = velocity_in_ms


print(datas_308["Vélocité (ms)"])

print(datas_308)
