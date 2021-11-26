#!/usr/bin/env python3
# Import libraries and create simulation
import re, rebound, requests
import pandas as pd
from astroquery.jplhorizons import Horizons

# Extract asteroid IDs
filename = '416_svea.tab'
data = pd.read_csv(filename, sep = '\s', header=None)
IDs = data.iloc[:, 0]
count = 1

# Add asteroid
def addAsteroid(coordsVec, coordsUncertVec, velVec, coefs, sim):
   sim.add(m=0, 
           x=coordsVec[0] + coefs[0] * coordsUncertVec[0],
           y=coordsVec[1] + coefs[1] * coordsUncertVec[1], 
           z=coordsVec[2] + coefs[2] * coordsUncertVec[2], 
           vx=velVec[0], vy=velVec[1], vz=velVec[2])
   return sim

# Use IDs to get the name required to add to database
for x in IDs:
   # Get the name of the asteroid in a format Horizons will accept
   obj = Horizons(id=x)
   eph = obj.ephemerides()
   name = re.sub(r"^\s*targetname\s*-*\s*-*\n", "", str(eph["targetname"]))
   name = re.sub(r"^[A-Za-z0-9 ]+", "", name)
   name = re.sub(r"\(", "", name)
   name = re.sub(r"\)", "", name)
   
   # URL used to get coordinates from JPL Horizons
   URL = f"https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='"
   URL += name
   URL += "'&OBJ_DATA='YES'&REF_PLANE='ECLIPTIC'&REF_SYSTEM='J2000'&MAKE_EPHEM='YES'&EPHEM_TYPE='VECTORS'&CENTER='500@0'&VEC_TABLE='2x'&TLIST='2459526.5'&OUT_UNITS='AU-D'"
   
   # Query
   response = requests.get(URL)
   respArr = response.text.split('\n')
   coordsVel = re.sub(r"\sXYZ\s*:\s*", "", respArr[66]) 
   # 66th line is where we've got the coordinates
   coordsVel = re.sub(r"[ ]+", ",", coordsVel)
   coordsVelVec = coordsVel.split(',')
   coordsVelVec = [float(x) for x in coordsVelVec]
   coordsVec = coordsVelVec[0:3]
   velVec = coordsVelVec[3:6]
   velVec = [float(x)*365.25 for x in velVec] 
   uncert = re.sub(r"\ssigmas:\s*", "", respArr[67])
   # 67th line is where we've got the uncertainties
   uncert = re.sub(r"[ ]+", ",", uncert)
   uncertVec = uncert.split(',')
   uncertVec = [float(x) for x in uncertVec]
   coordsUncertVec = uncertVec[0:3]

   # Add the required large bodies to database
   sim = rebound.Simulation()
   sim.units = ('AU', 'yr', 'Msun')
   dateStr = "2021-11-08 00:00"
   sim.add("Sun", date=dateStr)
   sim.add("Venus", date=dateStr)
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
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, [0, 0, 0], sim)
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, [1, -1, -1], sim)
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, [-1, 1, -1], sim)
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, [1, -1, 1], sim)
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, [-1, 1, 1], sim)
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, [-1, -1, 1], sim)
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, [1, 1, -1], sim)
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, [1, 1, 1], sim)
   sim = addAsteroid(coordsVec, coordsUncertVec, velVec, [-1, -1, -1], sim)

   # Save the solar system and increase count by 1
   sim.save("data/simulation_asteroid" + str(count) + ".bin")
   count += 1
