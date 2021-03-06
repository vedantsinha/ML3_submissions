# -*- coding: utf-8 -*-
"""142934.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o_ALMdr8KuxsCh2yaT3DVFwi5S1_WRZO
"""

!pip install gmplot
#!pip install gmplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as path
import gmplot
# feature 1: Path finder
# Car Owner: He can track the path and later on can choose
# short path to reach destination
# importing xlsx file
DF = pd.read_excel(r'City Drive 2.xlsx')
# extracting latitude and longitude
LATITUDE = DF[' Latitude']
LONGITUDE = DF[' Longitude']
# plotting the latitude and longitude on google map
LAT = np.array(DF[' Latitude'])
LONGI = np.array(DF[' Longitude'])
GMAP = gmplot.GoogleMapPlotter(DF[' Latitude'].mean(),
                               DF[' Longitude'].mean(), 14)
# plotting on map
GMAP.scatter(
    list([LAT[0]]), list([LONGI[0]]), '#00FF00', size=45, marker=False)
GMAP.scatter(list([LAT[-1]]), list([LONGI[-1]]), '#00FF00', size=45,
             marker=False)
GMAP.plot(LAT, LONGI, 'blue', edge_width=3.0)
# right click on .html file in Files to see the plot in google map
GMAP.draw("googlemaps.html")

# feature 2: Rash Driving information
# Government agency: To track if driver is doing rash driving
path.subplot(811)
ENGINE_RPM = DF['Engine RPM(rpm)']
TIME = list(range(2576))
# plotting time against engine rpm
path.plot(TIME, ENGINE_RPM, 'r-')
path.xlabel('time')
path.ylabel('rpm')
# finding the points on which the RPM decreases suddenly
for i in range(1, 2575):
    if ENGINE_RPM[i] > ENGINE_RPM[i+1]:
        i = i+1

path.subplot(813)
OBD_SPEED = DF['Speed (OBD)(km/h)']
# plotting time against obd speed
path.plot(TIME, OBD_SPEED)
path.xlabel('time')
path.ylabel('speed')
# finding the points on which the obd speed decreases suddenly
for j in range(1, 2575):
    if OBD_SPEED[j] > OBD_SPEED[j+1]:
        j = j+1
COUNT = 0
# frequency of rash driving
if i == j:
    COUNT = COUNT + 1
print('frequency of rash driving :', COUNT)

# feature 3: Gear shift used by the driver
# Fleet owner: This information will help in determining engine condition
COUNTER_RPM_LOWER = 0
COUNTER_RPM_UPPER = 0
GEAR = list(range(2576))
# finding the apropriate gear for given speed and rpm
for x in range(2576):
    GEAR[x] = 0
    if ENGINE_RPM[x] > 0 and OBD_SPEED[x] > 0:
        if ENGINE_RPM[x] > 600 and ENGINE_RPM[x] < 2000:
            if OBD_SPEED[x] < 20:
                GEAR[x] = 1
            elif OBD_SPEED[x] < 30 and OBD_SPEED[x] >= 20:
                GEAR[x] = 2
            elif OBD_SPEED[x] < 40 and OBD_SPEED[x] >= 30:
                GEAR[x] = 3
            elif OBD_SPEED[x] < 50 and OBD_SPEED[x] >= 40:
                GEAR[x] = 4
            else:
                GEAR[x] = 5
    elif ENGINE_RPM[x] <= 600:
        COUNTER_RPM_LOWER = COUNTER_RPM_LOWER + 1
    elif ENGINE_RPM[x] >= 2000:
        COUNTER_RPM_UPPER = COUNTER_RPM_UPPER + 1
# number of time GEARmismatched with rpm and speed
print('Number of times the driver needs to decrease')
print('the gear due to and rpm mismatch:', COUNTER_RPM_LOWER)
print('Number of times the driver needs to increase')
print('the gear due to gear and rpm mismatch:', COUNTER_RPM_UPPER)
path.subplot(815)
# plotting gear against time
path.plot(TIME, GEAR)
path.xlabel('time')
path.ylabel('gear')

# Feature 4:Eco drive mode
# Car Owner:Number of time person has driven in ecomode that gives good milaege
COUNTER_ECODRIVE = 0
ECO_DRIVE = list(range(2576))
for y in range(2576):
    ECO_DRIVE[y] = 0
    if GEAR[y] == 0:
        pass
    if ENGINE_RPM[y] > 0 and ENGINE_RPM[y] < 2000 and GEAR[y] == 1 and OBD_SPEED[y] < 30:
        ECO_DRIVE[y] = 1
    if ENGINE_RPM[y] > 600 and ENGINE_RPM[y] < 2500 and GEAR[y] == 2 and OBD_SPEED[y] < 40:
        ECO_DRIVE[y] = 1
    if ENGINE_RPM[y] > 600 and ENGINE_RPM[y] < 3000 and GEAR[y] == 3 and OBD_SPEED[y] < 50:
        ECO_DRIVE[y] = 1
    if ENGINE_RPM[y] > 600 and ENGINE_RPM[y] < 3500 and GEAR[y] == 4 and OBD_SPEED[y] < 60:
        ECO_DRIVE[y] = 1
    if ENGINE_RPM[y] > 600 and ENGINE_RPM[y] < 4000 and GEAR[y] == 5 and OBD_SPEED[y] < 70:
        ECO_DRIVE[y] = 1
# Number of times person has driven in ecodrive mode
    if ECO_DRIVE[y] == 1:
        COUNTER_ECODRIVE = COUNTER_ECODRIVE + 1
print('Number of times the person driven in ecodrive mode :', COUNTER_ECODRIVE)
# plotting ecodrive mode with respect to time
path.subplot(817)
path.plot(TIME, ECO_DRIVE)
path.xlabel('time')
path.ylabel('ecodrive level')

"""# New Section

# New Section

# New Section
"""