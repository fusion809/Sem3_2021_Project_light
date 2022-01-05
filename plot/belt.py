import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
Noutputs = 10000

plt.figure(1, figsize=(8, 8))
dfParam = pd.read_csv("../output/forwardIAS152e7/parameters_1.csv")
df1 = pd.read_csv("../output/forwardIAS152e7/coords_and_vel_1.csv")
x1 = df1["x"]
y1 = df1["y"]
a = dfParam["a"]
e = dfParam["e"]
thetas = np.linspace(0, 2*np.pi, 10000)
xBase = np.cos(thetas)
yBase = np.sin(thetas)
aEarth = a[Noutputs] - 0.03
eEarth = e[Noutputs]
bEarth = aEarth * np.sqrt(1-eEarth**2)
xEarth = aEarth * xBase
xVenus = a[0] * xBase
yEarth = bEarth * yBase
yVenus = a[0] * yBase
aMars = a[2*Noutputs] + 0.08
eMars = e[2*Noutputs]
bMars = aMars * np.sqrt(1-eMars**2)
xMars = aMars * xBase
yMars = bMars * yBase
aJup = a[3*Noutputs]-0.2
eJup = e[3*Noutputs]
bJup = aJup * np.sqrt(1-eJup**2)
xJup = aJup * xBase
yJup = bJup * yBase
a1 = a[7*Noutputs]
e1 = e[7*Noutputs]
aarr = np.array([a1])
earr = np.array([e1])
plt.scatter(x1[0], y1[0], label="Venus", color="blue", s=[2])
plt.scatter(x1[Noutputs], y1[Noutputs], label="Earth", color="green", s=[2])
plt.scatter(x1[2*Noutputs], y1[2*Noutputs], label="Mars", color="red", s=[2])
plt.scatter(x1[3*Noutputs], y1[3*Noutputs], label="Jupiter", color="orange", s=[2])
plt.scatter(x1[7*Noutputs], y1[7*Noutputs], color="#c967ff", s=[1], label="Svea family")
plt.plot(xEarth, yEarth, color="green")
plt.plot(xVenus, yVenus, color="blue")
plt.plot(xMars, yMars, color="red")
plt.plot(xJup, yJup, color="orange")
for i in range(1, 49):
    df = pd.read_csv("../output/forwardIAS152e7/coords_and_vel_" + str(i) + ".csv")
    dfParami = pd.read_csv("../output/forwardIAS152e7/parameters_" + str(i) + ".csv")
    ai = dfParami["a"]
    ei = dfParami["e"]
    aarr = np.append(aarr, ai[7*Noutputs])
    earr = np.append(earr, ei[7*Noutputs])
    x = df["x"]
    y = df["y"]
    plt.scatter(x[7*Noutputs], y[7*Noutputs], color="#c967ff", s=[1])
# currAx = plt.gca()
amin = np.min(aarr)
# currAx.add_patch(Circle((0, 0), radius=1.8, facecolor="none", ec="k", lw=1))
#currAx.add_patch(Circle((0, 0), radius=3.3, facecolor="grey", ec="k", lw=1))
inner = 1.7
outer = 3.7
x_inner = inner * xBase
y_inner = inner * yBase
x_outer = outer * xBase
y_outer = outer * yBase
xs = outer*np.linspace(-1.1,1.1, 10001)
ys = outer*np.linspace(-1.1,1.1, 10001)
plt.scatter(0, 0, color="black", s=[3], label="Sun")

# mesh for contours
xv,yv = np.meshgrid(xs,ys)
r = xv**2 + yv**2
plt.contourf(xv, yv, r, levels=[inner**2,outer**2], alpha=0.3, colors=('grey','g','b'))
plt.plot(x_inner, y_inner, color='grey', linewidth=1)
plt.plot(x_outer, y_outer, color='grey', linewidth=1)
plt.xlabel("x (AU)", fontsize=8)
plt.ylabel("y (AU)", fontsize=8)
plt.legend(fontsize=8, loc="lower right")
plt.title("Relative location of the asteroid belt (grey) and Svea family", fontsize=12)
plt.show()