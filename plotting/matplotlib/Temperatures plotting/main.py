import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from datetime import datetime
import seaborn as sns

df = pd.read_csv("datas.csv", sep=";")
df.columns = df.columns.str.replace(" ", "")

data_24h = df[df["Date"] == df.iloc[-1]["Date"]]
print(data_24h)

start_time = ":".join(data_24h.iloc[0]["Time"].split(":")[:2]).replace(" ", "")
end_time = ":".join(data_24h.iloc[-1]["Time"].split(":")[:2]).replace(" ", "")
plt.figure(figsize=(8,4), dpi=150)

sns.set_style("whitegrid")
# date_format = mpl.dates.DateFormatter("%H:%M")

date_range = pd.date_range(start_time, end_time, freq="H")
date_range2 = []
for date in date_range:
    #removes date
    f = str(date).split(" ")[-1]
    #removes seconds
    f = ":".join(f.split(":")[:1])
    if f.startswith("0"):
        f = f[1:]
    date_range2.append(f)

x_ticks_values = np.arange(0, len(data_24h), len(data_24h)/len(date_range))


plt.plot(data_24h["Time"], data_24h["Temp"], color="#37A2EF", label="outside", linewidth=0.8)

custom_font="Montserrat"

plt.title("Outside temperature in last 24 hours", size=9, fontname=custom_font)
plt.xticks(x_ticks_values, date_range2, size=9, fontname=custom_font)
plt.yticks(fontsize=9, fontname=custom_font)
plt.xlabel("Day hour", size=9, fontname=custom_font)
plt.ylabel("Temperature in °C", size=9, fontname=custom_font)


plt.margins(x=0)
plt.legend()
# plt.gca().xaxis.set_major_formatter(date_format)
# plt.fill_bewtween(data_24h["Time"], 0, data_24h["Temp"], alpha=.3)
plt.savefig("temperature.png", dpi=300)
plt.show()


