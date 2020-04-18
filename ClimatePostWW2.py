#import all necessary functions
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#pull in the US Temperatures CSV
state_temps = pd.read_csv('GlobalLandTemperaturesByCountry.csv')

state_temps = state_temps[['dt', 'Country','AverageTemperature']]

state_temps = state_temps[state_temps['Country'].str.contains("United States")]

state_temps = state_temps.iloc[2127:, :]

#We now should have monthly temps in the US from 1946-2013
print(state_temps)

#This will make the list only the month of June
dt_list = state_temps['dt'].values.tolist()
i=6
summer_list = []

while i < 814:
    summer_list.append(dt_list[i])
    i = i+12
                

#This list will be the temperatures for just the month of June
avgtemp_list = state_temps['AverageTemperature'].values.tolist()
i=6
newtemp_list = []

while i < 814:
    newtemp_list.append(avgtemp_list[i])
    i = i+12

#Add Labels
plt.ylabel('Temperature (Celsius)')
plt.title('Change In Temperature in the US After WW2')

#Create a Default List
newlist = [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
           31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,
           59,60,61,62,63,64,65,66,67,68]

#Make our list into an Array for Numpy
array1 = np.array(newlist)
array2 = np.array(newtemp_list)

m, b = np.polyfit(array1, array2, 1)

#Plot the two lines giving it a better look
plt.plot(summer_list, newtemp_list,"blue", linewidth=5, alpha=0.3)
plt.plot(summer_list, newtemp_list,"orange", linewidth=1)

#This plots the Line of Best Fit
plt.plot(array1, m*array1 + b)

#Specific Tick Values on the x-axis
tick_val = [15, 35, 55]
tick_lab = ['June 1960', 'June 1980', 'June 2000']
plt.xticks(tick_val, tick_lab)

#Print Graph
plt.show()
