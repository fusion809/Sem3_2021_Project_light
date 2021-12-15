import pandas as pd
import matplotlib.pyplot as plt

# Get required data
dat = pd.read_csv("HmagvsSMA.csv")
IDs = dat["ID"]
H = dat["Hmag"]
a = dat["SMA"]

# Plot it
plt.figure(1)
plt.scatter(a, H)
plt.xlabel("Semimajor axis (AU)")
plt.ylabel("Hmag")
plt.title("Hmag vs SMA")
plt.savefig("../plots/HmagvsSMA/plot.svg")