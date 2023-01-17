#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

missions = pd.read_csv(r"../space_shuttle_missions.csv")
print(missions.head())

shuttle = missions['Shuttle']
year = missions['Year']
colors = ['green', 'yellow', 'blue', 'red']

seaborn.set()
plt.scatter(shuttle, year, cmap='viridis', alpha=0.5)
plt.xlabel('Shittle Name')
plt.ylabel('Year')
plt.clim(0, 7)


plt.show()

