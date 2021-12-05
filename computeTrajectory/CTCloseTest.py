#!/usr/bin/env python3
import rebound, os
import pandas as pd
import numpy as np

#
no = 5

# Simulation
## File our object data is stored within
filename = os.path.expanduser('~')
basedir = filename + "/Sem3_2021_Project_light/"
filename = basedir + "data/"
filename += "simulation_asteroid_close_" + str(no) + ".bin"

# Create simulation object
sim = rebound.Simulation(filename)

# closeEncounters.csv
data = pd.read_csv("../closeEncounters.csv")
t0 = data["t0"]
tf = data["t1"]

# Define the variables related to the simulation
sim.dt = 0.02
Noutputs = 10000
Nobj = 8

# Times we're getting our solution values for
times = np.linspace(t0[no-1],tf[no-1], Noutputs)

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
# for i,time in enumerate(times):
#     sim.integrate(time)

#     # Loop over asteroids
#     for j in range(0, Nobj):
#         x[j][i] = ps[j+1].x
#         y[j][i] = ps[j+1].y
#         z[j][i] = ps[j+1].z
#         vx[j][i] = ps[j+1].vx
#         vy[j][i] = ps[j+1].vy
#         vz[j][i] = ps[j+1].vz