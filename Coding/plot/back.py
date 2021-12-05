#!/usr/bin/env python
import argparse
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import pandas as pd

# Args
parser = argparse.ArgumentParser(description='Plot the trajectory of celestial bodies in specified file')
parser.add_argument('integer', metavar='no', type=int, nargs="+", help="Integers specifying the file to be used")
args = parser.parse_args()
no = args.integer[0]

# Read file
file = "../output/back/coords_and_velBack_" + str(no) + ".csv"
paramsFile = "../output/back/parametersBack_" + str(no) + ".csv"
df = pd.read_csv(file, sep=",")
paramsDf = pd.read_csv(paramsFile, sep=",")
times = df['t']
x = df['x']
y = df['y']
z = df['z']
a = paramsDf['a']
e = paramsDf['e']
inc = paramsDf['inc']
Noutputs = 10000

# Plot each clone relative to the terrestrial planets we've modelled
for i in range(0, 9):
    # Starting index 
    startIndex = (i + 7) * Noutputs
    endIndex = (i + 8) * Noutputs
    asteroidLabel = "Asteroid_" + str(no) + "_clone_" + str(i)
    asteroidLabelTeX = "Asteroid " + str(no) + " clone " + str(i)

    # First figure is a plot of the ith clone of the asteroid and 
    # Venus, Earth and Mars
    plt.figure(1)
    plt.plot(x[0:Noutputs], y[0:Noutputs], label="Venus")
    plt.plot(x[Noutputs:2*Noutputs], y[Noutputs:2*Noutputs], label="Earth")
    plt.plot(x[2*Noutputs:3*Noutputs], y[2*Noutputs:3*Noutputs], label="Mars")
    plt.plot(x[startIndex:endIndex], y[startIndex:endIndex], label=asteroidLabelTeX)
    plt.xlabel("x (AU)")
    plt.ylabel("y (AU)")
    plt.title("Trajectory of Venus, Earth, Mars and " + asteroidLabelTeX)
    plt.legend()
    plt.savefig("../plots/N1e8Noutputs1e4/" + asteroidLabel + "_back_wo_Jupiter_et_al.svg")
    plt.close(fig=1)

    # Semi-major axis vs time plot
    plt.figure(2)
    plt.plot(times[startIndex:endIndex], a[startIndex:endIndex], label=asteroidLabelTeX)
    plt.xlabel("t (years)")
    plt.ylabel("Semimajor axis (AU)")
    plt.title("Semimajor axis vs time plot for " + asteroidLabelTeX)
    plt.legend()
    plt.savefig("../plots/Semimajor_axis/" + asteroidLabel + "_back_semimajor_time.svg")
    plt.close(fig=2)

    # Eccentricity vs time plot
    plt.figure(3)
    plt.plot(times[startIndex:endIndex], e[startIndex:endIndex], label=asteroidLabelTeX)
    plt.xlabel("t (years)")
    plt.ylabel("Eccentricity")
    plt.title("Eccentricity vs time plot for " + asteroidLabelTeX)
    plt.legend()
    plt.savefig("../plots/Eccentricity/" + asteroidLabel + "_back_eccentricity_time.svg")
    plt.close(fig=3)
    
    # Inclination vs time plot
    plt.figure(4)
    plt.plot(times[startIndex:endIndex], inc[startIndex:endIndex], label=asteroidLabelTeX)
    plt.xlabel("t (years)")
    plt.ylabel("Inclination")
    plt.title("Inclination vs time plot for " + asteroidLabelTeX)
    plt.legend()
    plt.savefig("../plots/Inclination/" + asteroidLabel + "_back_inclination_time.svg")
    plt.close(fig=4)
