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
xEarth = x[Noutputs:2*Noutputs]
yEarth = y[Noutputs:2*Noutputs]
plt.figure(1)
plt.plot(xEarth, yEarth)
plt.show()