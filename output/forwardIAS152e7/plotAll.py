#!/usr/bin/env python
import pandas as pd
import os
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')

# DataFrame
Noutputs = 10000
for astNo in range(1, 49):
    # Get coordinates from CSV file
    df = pd.read_csv("coords_and_vel_" + str(astNo) + ".csv")
    x = df["x"]
    y = df["y"]
    
    # Get planets
    xVenus = x[0:Noutputs]
    yVenus = y[0:Noutputs]
    xEarth = x[Noutputs:2*Noutputs]
    yEarth = y[Noutputs:2*Noutputs]
    xMars = x[2*Noutputs:3*Noutputs]
    yMars = y[2*Noutputs:3*Noutputs]
    xJupiter = x[3*Noutputs:4*Noutputs]
    yJupiter = y[3*Noutputs:4*Noutputs]
    for cloneNo in range(0, 9):
        xAst = x[(7 + cloneNo)*Noutputs:(8 + cloneNo)*Noutputs]
        yAst = y[(7 + cloneNo)*Noutputs:(8 + cloneNo)*Noutputs]

        # Figure 1, plot asteroid against Venus to Mars
        plt.figure(1, figsize=(8, 6))
        plt.plot(xVenus, yVenus, label="Venus")
        plt.plot(xEarth, yEarth, label="Earth")
        plt.plot(xMars, yMars, label="Mars")
        plt.plot(xAst, yAst, 
        label="Asteroid " + str(astNo) + " clone " + str(cloneNo))
        plt.legend(fontsize=18)
        title="Asteroid " + str(astNo) + " clone " + str(cloneNo)
        title += " forward simulation 20 My using IAS15"
        plt.title(title, fontsize=20)
        plt.xlabel("x (AU)", fontsize=20)
        plt.ylabel("y (AU)", fontsize=20)
        VEMADir = "../../plots/forwardIAS152e7/VEMA_asteroid_"
        svgfile = VEMADir + str(astNo) + "_clone_" + str(cloneNo) + ".svg" 
        pngfile = VEMADir + str(astNo) + "_clone_" + str(cloneNo) + ".png"
        plt.savefig(svgfile)
        os.system("convert {} {}".format(svgfile, pngfile))
        plt.close()
    
        # Figure 2, plot asteroid against Venus to Earth
        plt.figure(2, figsize=(8, 6))
        plt.plot(xVenus, yVenus, label="Venus")
        plt.plot(xEarth, yEarth, label="Earth")
        plt.plot(xAst, yAst, 
        label="Asteroid " + str(astNo) + " clone " + str(cloneNo))
        plt.legend(fontsize=18)
        plt.title(title, fontsize=20)
        plt.xlabel("x (AU)", fontsize=20)
        plt.ylabel("y (AU)", fontsize=20)
        VEADir = "../../plots/forwardIAS152e7/VEA_asteroid_"
        svgfile = VEADir + str(astNo) + "_clone_" + str(cloneNo) + ".svg" 
        pngfile = VEADir + str(astNo) + "_clone_" + str(cloneNo) + ".png"
        plt.savefig(svgfile)
        os.system("convert {} {}".format(svgfile, pngfile))
        plt.close()

        # Figure 3, plot asteroid against Venus
        plt.figure(3, figsize=(8, 6))
        plt.plot(xVenus, yVenus, label="Venus")
        plt.plot(xAst, yAst, 
        label="Asteroid " + str(astNo) + " clone " + str(cloneNo))
        plt.legend(fontsize=18)
        plt.title(title, fontsize=20)
        plt.xlabel("x (AU)", fontsize=20)
        plt.ylabel("y (AU)", fontsize=20)
        VADir = "../../plots/forwardIAS152e7/VA_asteroid_"
        svgfile = VADir + str(astNo) + "_clone_" + str(cloneNo) + ".svg" 
        pngfile = VADir + str(astNo) + "_clone_" + str(cloneNo) + ".png"
        plt.savefig(svgfile)
        os.system("convert {} {}".format(svgfile, pngfile))
        plt.close()

        # Figure 4, plot asteroid against Venus to Jupiter
        plt.figure(4, figsize=(8, 6))
        plt.plot(xVenus, yVenus, label="Venus")
        plt.plot(xEarth, yEarth, label="Earth")
        plt.plot(xMars, yMars, label="Mars")
        plt.plot(xJupiter, yJupiter, label="Jupiter")
        plt.plot(xAst, yAst, 
        label="Asteroid " + str(astNo) + " clone " + str(cloneNo))
        plt.legend(fontsize=18)
        plt.title(title, fontsize=20)
        plt.xlabel("x (AU)", fontsize=20)
        plt.ylabel("y (AU)", fontsize=20)
        VEMJADir = "../../plots/forwardIAS152e7/VEMJA_asteroid_"
        svgfile = VEMJADir + str(astNo) + "_clone_" + str(cloneNo) + ".svg" 
        pngfile = VEMJADir + str(astNo) + "_clone_" + str(cloneNo) + ".png"
        plt.savefig(svgfile)
        os.system("convert {} {}".format(svgfile, pngfile))
        plt.close()
