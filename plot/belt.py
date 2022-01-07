#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
Noutputs = 10000

# Create plot figure
plt.figure(1, figsize=(12, 9))

# Load first parameter and coords file so we can get planet data
dfParam = pd.read_csv("../output/forwardIAS152e7/parameters_1.csv")
df1 = pd.read_csv("../output/forwardIAS152e7/coords_and_vel_1.csv")
x1 = df1["x"]
y1 = df1["y"]
a = dfParam["a"]
e = dfParam["e"]
thetas = np.linspace(0, 2*np.pi, Noutputs)
xBase = np.cos(thetas)
yBase = np.sin(thetas)

# Venus coordinates
xVenus = a[0] * xBase
yVenus = a[0] * np.sqrt(1-e[0]**2) * yBase

# Earth coordinates
aEarth = a[Noutputs] - 0.02
eEarth = e[Noutputs]
bEarth = aEarth * np.sqrt(1-eEarth**2)
xEarth = aEarth * xBase
yEarth = bEarth * yBase

# Mars coordinates
aMars = a[2*Noutputs] + 0.08
eMars = e[2*Noutputs]
bMars = aMars * np.sqrt(1-eMars**2)
xMars = aMars * xBase
yMars = bMars * yBase

# Jupiter coordinates
aJup = a[3*Noutputs]-0.2
eJup = e[3*Noutputs]
bJup = aJup * np.sqrt(1-eJup**2)
xJup = aJup * xBase
yJup = bJup * yBase

# Size of objects in plot
planetSize = 80
sunSize = 2*planetSize
astSize = planetSize

# Sun
plt.scatter(0, 0, color="black", s=[sunSize], label="Sun")

# Venus - Jupiter orbits
plt.scatter(x1[0], y1[0], label="Venus", color="#006ba4", s=[planetSize])
plt.plot(xVenus, yVenus, color="#006ba4")
plt.scatter(x1[Noutputs], y1[Noutputs], label="Earth", color="#ff800e", s=[planetSize])
plt.plot(xEarth, yEarth, color="#ff800e")
plt.scatter(x1[2*Noutputs], y1[2*Noutputs], label="Mars", color="#5f9ed1", s=[planetSize])
plt.plot(xMars, yMars, color="#5f9ed1")
plt.scatter(x1[3*Noutputs], y1[3*Noutputs], label="Jupiter", color="#ffbc79", s=[planetSize])
plt.plot(xJup, yJup, color="#ffbc79")

# Add Svea family
plt.scatter(x1[7*Noutputs], y1[7*Noutputs], color="#c85200", s=[astSize], label="Svea family")
for i in range(1, 49):
    df = pd.read_csv("../output/forwardIAS152e7/coords_and_vel_" + str(i) + ".csv")
    x = df["x"]
    y = df["y"]
    plt.scatter(x[7*Noutputs], y[7*Noutputs], color="#c85200", s=[astSize])

# Asteroid belt
# This section is based largely on this answer:
# https://stackoverflow.com/a/53948581/1876983
## Inner belt's boundaries
inner = 1.7
x_inner = inner * xBase
y_inner = inner * yBase
## Outer belt's boundaries
outer = 3.9
x_outer = outer * xBase
y_outer = outer * yBase

## Colour in the torus
xs = outer * np.linspace(-1.1, 1.1, Noutputs + 1)
ys = outer * np.linspace(-1.1, 1.1, Noutputs + 1)
xv,yv = np.meshgrid(xs,ys)
r = xv**2 + yv**2
plt.contourf(xv, yv, r, levels=[inner**2,outer**2], alpha=0.3, colors=('grey','g','b'))

## Draw boundaries
plt.plot(x_inner, y_inner, color='grey', linewidth=1)
plt.plot(x_outer, y_outer, color='grey', linewidth=1)

# Add annotations to the plot
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.xlim([-5.2, 5.2])
plt.ylim([-5.2, 5.2])
plt.xlabel(r"$x$ (AU)", fontsize=24)
plt.ylabel(r"$y$ (AU)", fontsize=24)
plt.tight_layout(rect=[0, 0, 0.81, 0.9])
plt.legend(bbox_to_anchor=(1.295, 1), ncol=1, fontsize=20, loc="upper right")
plt.title("Relative location of the asteroid belt (grey region) and \nSvea family within the Solar system", fontsize=26)
plt.savefig("../../Asteroid_belt.png")