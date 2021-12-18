#!/usr/bin/env python
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Args
parser = argparse.ArgumentParser(description='Plot the trajectory of celestial bodies in specified file')
parser.add_argument('integer', metavar='no', type=int, nargs="+", help="Integers specifying the file to be used")
args = parser.parse_args()
no = args.integer[0]

# DataFrame
Noutputs = 10000
df = pd.read_csv("coords_and_vel_close_" + str(no) + ".csv")
x = df["x"]
y = df["y"]
z = df["z"]
xVenus = x[0:Noutputs]
yVenus = y[0:Noutputs]
xEarth = x[Noutputs:2*Noutputs]
yEarth = y[Noutputs:2*Noutputs]
xMars = x[2*Noutputs:3*Noutputs]
yMars = y[2*Noutputs:3*Noutputs]
xJupiter = x[3*Noutputs:4*Noutputs]
yJupiter = y[3*Noutputs:4*Noutputs]
xSaturn = x[4*Noutputs:5*Noutputs]
ySaturn = y[4*Noutputs:5*Noutputs]
xUranus = x[5*Noutputs:6*Noutputs]
yUranus = y[5*Noutputs:6*Noutputs]
xNeptune = x[6*Noutputs:7*Noutputs]
yNeptune = y[6*Noutputs:7*Noutputs]
xAst = x[7*Noutputs:8*Noutputs]
yAst = y[7*Noutputs:8*Noutputs]
plt.figure(1)
plt.plot(xVenus, yVenus, label="Venus")
plt.plot(xEarth, yEarth, label="Earth")
plt.plot(xMars, yMars, label="Mars")
plt.plot(xJupiter, yJupiter, label="Jupiter")
plt.plot(xSaturn, ySaturn, label="Saturn")
plt.plot(xUranus, yUranus, label="Uranus")
plt.plot(xNeptune, yNeptune, label="Neptune")
plt.legend()
plt.show()
plt.figure(2)
plt.plot(xAst, yAst)
plt.show()