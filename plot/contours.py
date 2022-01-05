import matplotlib.pyplot as pyplot
import numpy as np
# inner radius
inner = 0.5

# the two circles
thetas = np.linspace(0,2*np.pi, 200)
# you don't need r = np.one(len(thetas))
x_unit_circle = np.cos(thetas)
y_unit_circle = np.sin(thetas)

x_eigens = x_unit_circle * inner
y_eigens = y_unit_circle * inner

xs = np.linspace(-1.1,1.1, 201)
ys = np.linspace(-1.1,1.1, 201)

# mesh for contours
xv,yv = np.meshgrid(xs,ys)

# generate the level map
r = xv**2 + yv**2

pyplot.figure(figsize=(8,8))

# plot the contours with two levels only
# notice the xv, yv parameters
pyplot.contourf(xv, yv, r, levels=[inner**2,1], colors=('r','g','b'))

# plot the two circles
pyplot.plot(x_unit_circle, y_unit_circle, color='b', linewidth=3)
pyplot.plot(x_eigens, y_eigens, color='g', linewidth=3, linestyle='--')

pyplot.show()