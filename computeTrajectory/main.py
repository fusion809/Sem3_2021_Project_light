#!/usr/bin/env python3
import rebound, argparse, os
import numpy as np

# Args
parser = argparse.ArgumentParser(description='Simulate the trajectory for the specified Svea family asteroid')
parser.add_argument('integers', metavar='no', type=int, nargs='+', help='an integer specifying the binary file used')
args = parser.parse_args()
no = args.integers[0]

# Simulation
## File our object data is stored within
filename = os.path.expanduser('~')
basedir = filename + "/Sem3_2021_Project_light/"
filename = basedir + "data/"
filename += "simulation_asteroid" + str(no) + ".bin"

# Create simulation object
sim = rebound.Simulation(filename)
sim.collision = "direct"

# Files to write to
writeFileParams = basedir + "output/parameters_"
writeFileParams += str(no) + ".csv"
fParams = open(writeFileParams, "w")
writeFileCoords = basedir + "output/coords_and_vel_"
writeFileCoords += str(no) + ".csv"
fCoords = open(writeFileCoords, "w")
writeFileColl = basedir + "output/collision_"
writeFileColl += str(no) + ".csv"
fColl = open(writeFileColl, "w")
writeFileEscap = basedir + "output/escaped_" + str(no) + ".csv"
fEscap = open(writeFileEscap, "w")

# Define the variables related to the simulation
sim.dt = 0.02
Noutputs = 10000
noYears = 1e8
Nobj = 9 + 8 - 1

# Times we're getting our solution values for
times = np.linspace(0.,int(noYears), Noutputs)

# Coordinate arrays
x = np.zeros((Nobj,Noutputs))
vx = np.zeros((Nobj,Noutputs))
y = np.zeros((Nobj,Noutputs))
vy = np.zeros((Nobj,Noutputs))
z = np.zeros((Nobj,Noutputs))
vz = np.zeros((Nobj,Noutputs))
a = np.zeros((Nobj,Noutputs))
e = np.zeros((Nobj,Noutputs))
inc = np.zeros((Nobj,Noutputs))
Omega = np.zeros((Nobj,Noutputs))
omega = np.zeros((Nobj,Noutputs))
f = np.zeros((Nobj,Noutputs))

# We use the mercurius integrator because it switches to ias15 when objects get 
# close, but otherwise uses WHF
sim.integrator = "mercurius"
sim.move_to_com()

# Perform integration
ps = sim.particles
counter = np.zeros((Nobj,1))
fColl.write("t,particle1,particle2\n")
fEscap.write("t,particle\n")
for i,time in enumerate(times):
    try:
        sim.integrate(time)

    # Check for collision and document it in fColl
    except rebound.Collision:
        fColl.write(str(time) + ",")
        pt=1
        for p in ps:
            if p.lastcollision == sim.t:
                if (pt == 1):
                    fColl.write(str(p.index) + ",")
                else:
                    fColl.write(str(p.index))
                pt += 1
        fColl.write("\n")

    # Loop over asteroids
    for j in range(0, Nobj):
        x[j][i] = ps[j+1].x
        y[j][i] = ps[j+1].y
        z[j][i] = ps[j+1].z
        vx[j][i] = ps[j+1].vx
        vy[j][i] = ps[j+1].vy
        vz[j][i] = ps[j+1].vz
        a[j][i] = ps[j+1].orbit.a
        if (ps[j+1].orbit.d > 100 and counter[j] == 0):
            fEscap.write(str(time) + "," + str(j) + "\n")
            counter[j] += 1
        e[j][i] = ps[j+1].orbit.e
        inc[j][i] = ps[j+1].orbit.inc
        Omega[j][i] = ps[j+1].orbit.Omega
        omega[j][i] = ps[j+1].orbit.omega
        f[j][i] = ps[j+1].orbit.f
fColl.close()

# Write to file
fCoords.write("t,x,y,z,vx,vy,vz\n")
fParams.write("a,e,inc,Omega,omega,f\n")
for j in range(0, Nobj):
    for i in range(0, len(times)):
        fParams.write(str(a[j][i]) + ",")
        fParams.write(str(e[j][i]) + ",")
        fParams.write(str(inc[j][i]) + ",")
        fParams.write(str(Omega[j][i]) + ",")
        fParams.write(str(omega[j][i]) + ",")
        fParams.write(str(f[j][i]) + "\n")
        fCoords.write(str(times[i]) + ",")
        fCoords.write(str(x[j][i]) + ",")
        fCoords.write(str(y[j][i]) + ",")
        fCoords.write(str(z[j][i]) + ",")
        fCoords.write(str(vx[j][i]) + ",")
        fCoords.write(str(vy[j][i]) + ",")
        fCoords.write(str(vz[j][i]) + "\n")

fParams.close()
fCoords.close()
