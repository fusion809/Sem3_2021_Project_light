#!/usr/bin/env python3
import rebound, os
import numpy as np

# Simulation
## File our object data is stored within
filename = os.path.expanduser('~')
basedir = filename + "/Sem3_2021_Project_light/Coding/"
filename = basedir + "data/"
filename += "simulation_base.bin"

# Create simulation object
sim = rebound.Simulation(filename)

# Files to write to
writeFileCoords = basedir + "output/coords_and_vel_base.csv"
fCoords = open(writeFileCoords, "w")

# Define the variables related to the simulation
sim.dt = 0.02
Noutputs = 10000
noYears = 1e8
Nobj = 8

# Times we're getting our solution values for
times = np.linspace(0.,int(noYears), Noutputs)

# Coordinate arrays
x = np.zeros((Nobj,Noutputs))
vx = np.zeros((Nobj,Noutputs))
y = np.zeros((Nobj,Noutputs))
vy = np.zeros((Nobj,Noutputs))
z = np.zeros((Nobj,Noutputs))
vz = np.zeros((Nobj,Noutputs))

# We use the mercurius integrator because it switches to ias15 when objects get 
# close, but otherwise uses WHF
sim.integrator = "mercurius"
sim.move_to_com()

# Perform integration
ps = sim.particles
for i,time in enumerate(times):
    sim.integrate(time)

    # Loop over asteroids
    for j in range(0, Nobj):
        x[j][i] = ps[j].x
        y[j][i] = ps[j].y
        z[j][i] = ps[j].z
        vx[j][i] = ps[j].vx
        vy[j][i] = ps[j].vy
        vz[j][i] = ps[j].vz

# Write to file
fCoords.write("t,x,y,z,vx,vy,vz\n")
for j in range(0, Nobj):
    for i in range(0, len(times)):
        fCoords.write(str(times[i]) + ",")
        fCoords.write(str(x[j][i]) + ",")
        fCoords.write(str(y[j][i]) + ",")
        fCoords.write(str(z[j][i]) + ",")
        fCoords.write(str(vx[j][i]) + ",")
        fCoords.write(str(vy[j][i]) + ",")
        fCoords.write(str(vz[j][i]) + "\n")

fCoords.close()
