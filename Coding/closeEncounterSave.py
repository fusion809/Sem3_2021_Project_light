#!/usr/bin/env python
import re, rebound, requests
import pandas as pd
import numpy as np
from astroquery.jplhorizons import Horizons

# Extract asteroid IDs
filename = '416_svea.tab'
data = pd.read_csv(filename, sep = '\s', header=None)
IDs = data.iloc[:, 0]
count = 1

# close encounters
closeFile = "closeEncounters.csv"
closeDat = pd.read_csv(closeFile)
astNo = closeDat["asteroid"]
clonNo = closeDat["clone"]
t0 = closeDat["t0"]
tf = closeDat["t1"]
newIDs = IDs[astNo]
count = 0

Noutputs = 10000

def addAsteroid(coordsVec, coordsUncertVec, velVec, coefs, sim):
   sim.add(m=0, 
           x=coordsVec[0] + coefs[0] * coordsUncertVec[0],
           y=coordsVec[1] + coefs[1] * coordsUncertVec[1], 
           z=coordsVec[2] + coefs[2] * coordsUncertVec[2], 
           vx=velVec[0], vy=velVec[1], vz=velVec[2])
   return sim

coordsMat = np.array([[0, 0, 0],
[1,  -1, -1],
[-1,  1, -1],
[1,  -1,  1],
[-1,  1,  1],
[-1, -1, 1],
[1,   1, -1],
[1,   1,  1],
[-1, -1, -1]])

def findIndex(t0, Noutputs, asteroidNo, cloneNo):
    t = pd.read_csv("output/ordinary/coords_and_vel_" + str(asteroidNo) + ".csv")["t"]
    counter = 0
    for i in t == t0:
        if i and counter >= 7 * Noutputs + cloneNo:
            return counter

def getEphemeres(t0, Noutputs, asteroidNo, cloneNo):
    index = findIndex(t0, Noutputs, asteroidNo, cloneNo)
    ephData = pd.read_csv("output/ordinary/coords_and_vel_" + str(asteroidNo) + ".csv")
    x = ephData["x"]
    y = ephData["y"]
    z = ephData["z"]
    vx = ephData["vx"]
    vy = ephData["vy"]
    vz = ephData["vz"]
    return x[index], y[index], z[index], vx[index], vy[index], vz[index]

def getEphemeresOther(t0, Noutputs, asteroidNo, cloneNo, objNo):
    index = findIndex(t0, Noutputs, asteroidNo, cloneNo)
    ephData = pd.read_csv("output/ordinary/coords_and_vel_" + str(asteroidNo) + ".csv")
    x = ephData["x"]
    y = ephData["y"]
    z = ephData["z"]
    vx = ephData["vx"]
    vy = ephData["vy"]
    vz = ephData["vz"]
    newIndex = objNo * Noutputs + (index - 7000 - cloneNo*Noutputs)
    return x[newIndex], y[newIndex], z[newIndex], vx[newIndex], vy[newIndex], vz[newIndex]

for x in newIDs:
   # Add the required large bodies to database
   sim = rebound.Simulation()
   sim.units = ('AU', 'yr', 'Msun')

   sim.add("Sun", m=1)
   xVe, yVe, zVe, vxVe, vyVe, vzVe = getEphemeresOther(t0[count], Noutputs, astNo[count], clonNo[count], 1)
   sim.add(m=2.448e-6, x=xVe, y=yVe, z=zVe, vx=vxVe, vy=vyVe, vz=vzVe)
   sim.add("Earth", date=dateStr)
   sim.add("Mars", date=dateStr)
   sim.add("Jupiter", date=dateStr)
   sim.add("Saturn", date=dateStr)
   sim.add("Uranus", date=dateStr)
   sim.add("Neptune", date=dateStr)

   # Add the required asteroids
   print("Adding asteroid number: ", count)
   print("name: ", name)
   print("coordsVec: ", coordsVec)
   print("velVec: ", velVec)
   print("coordsUncertVec: ", coordsUncertVec)
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, clonNo[count])

   # Save the solar system and increase count by 1
   sim.save("data/simulation_asteroid_close" + str(count) + ".bin")
   count += 1