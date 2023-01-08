#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

missions = pd.read_csv(r"space_shuttle_missions.csv")
print(missions.head())

shuttle = missions['Shuttle']
year = missions['Year']
colors = np.array([x for x in range(0, 100, 11)])

seaborn.set()
plt.scatter(shuttle, year, c='red', cmap='viridis')
plt.xlabel('Shittle Name')
plt.ylabel('Year')
plt.clim(0, 7)

# for shuttle in [1, 2, 3]:
#     plt.scatter([], [], c='red')
plt.show()

