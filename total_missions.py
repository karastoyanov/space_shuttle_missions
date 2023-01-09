#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn


missions = pd.read_csv(r"space_shuttle_missions.csv")
print(missions.head())

xdata = [x for x in missions['Shuttle']]
ydata = [x for x in missions['Year']]
colors = 'blue'

plt.bar(xdata,ydata)
plt.title("Space Shuttle Missions")
plt.show()