#!/usr/bin/env python
import rebound
import pandas as pd
import numpy as np

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

# masses
m = np.array([1, 
4.8675e24/(1.9885e30), 
5.9724e24/(1.9885e30), 
6.4171e23/(1.9885e30), 
1.898187e27/(1.9885e30), 
5.68317e26/(1.9885e30), 
8.6813e25/(1.9885e30), 
1.02413e26/(1.9885e30)])
Noutputs = 10000
coordsMat = np.array([[0, 0, 0],
[1,  -1, -1],
[-1,  1, -1],
[1,  -1,  1],
[-1,  1,  1],
[-1, -1, 1],
[1,   1, -1],
[1,   1,  1],
[-1, -1, -1]])

# Find the index corresponding to the asteroid clone at the time just before 
# entering 5 x Hill radius
def findIndex(t0, Noutputs, asteroidNo, cloneNo):
    coordsVelBase = "output/ordinary/output/coords_and_vel_"
    t = pd.read_csv(coordsVelBase + str(asteroidNo) + ".csv")["t"]
    t = np.asarray(t)
    indices = np.where(t == t0)[0]
    for i in indices:
        if i >= 7 * Noutputs + cloneNo * Noutputs:
            return i

# Get the ephemeres of an asteroid
def getEphemeres(t0, Noutputs, asteroidNo, cloneNo):
    coordsVelBase = "output/ordinary/output/coords_and_vel_"
    index = findIndex(t0, Noutputs, asteroidNo, cloneNo)
    ephData = pd.read_csv(coordsVelBase + str(asteroidNo) + ".csv")
    x = ephData["x"]
    y = ephData["y"]
    z = ephData["z"]
    vx = ephData["vx"]
    vy = ephData["vy"]
    vz = ephData["vz"]
    return x[index], y[index], z[index], vx[index], vy[index], vz[index]

# Get the ephemeres of a planet or the Sun
def getEphemeresOther(t0, Noutputs, asteroidNo, cloneNo, objNo):
    index = findIndex(t0, Noutputs, asteroidNo, cloneNo)
    ephData = pd.read_csv("output/coords_and_vel_base.csv")
    x = ephData["x"]
    y = ephData["y"]
    z = ephData["z"]
    vx = ephData["vx"]
    vy = ephData["vy"]
    vz = ephData["vz"]
    nIndex = objNo * Noutputs + (index - 7*Noutputs - cloneNo*Noutputs)
    return x[nIndex], y[nIndex], z[nIndex], vx[nIndex], vy[nIndex], vz[nIndex]

for ast in newIDs:
   # Add the required large bodies to database
   sim = rebound.Simulation()
   sim.units = ('AU', 'yr', 'Msun')

   for i in range(0, 8):
       x, y, z, vx, vy, vz = getEphemeresOther(t0[count-1], Noutputs, 
       astNo[count-1], clonNo[count-1], i)
       sim.add(m=m[i], x=x, y=y, z=z, vx=vx, vy=vy, vz=vz)

   # Add asteroid clone
   xAst, yAst, zAst, vxAst, vyAst, vzAst = getEphemeres(t0[count-1], Noutputs, 
   astNo[count-1], clonNo[count-1])
   sim.add(m=0, x=xAst, y=yAst, z=zAst, vx=vxAst, vy=vyAst, vz=vzAst)
   
   # Save the solar system and increase count by 1
   sim.save("../data/simulation_asteroid_close_" + str(count) + ".bin")
   count += 1