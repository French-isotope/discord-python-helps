import pandas as pd

# Value in m/s = value in fps × 0.3048

sound_speed_ms = 343

win_308_speed_fps = 2650

win_308_speed_ms = win_308_speed_fps * 0.3048

datas_308 = pd.read_csv("308_chart.csv")

print(datas_308)

