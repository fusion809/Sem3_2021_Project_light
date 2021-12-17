import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Get required data
dat = pd.read_csv("HmagvsSMA.csv")
IDs = dat["ID"]
H = dat["Hmag"]
a = dat["SMA"]
alin = np.linspace(np.min(a), np.max(a), 10001)
C = 2.5e-5
Hpred = 5*np.log10(np.abs(alin-a[0])/C)

# Plot it
plt.figure(1)
plt.scatter(a, H, label="Asteroid values")
plt.plot(alin, Hpred, label="Predicted values")
plt.xlabel("Semimajor axis (AU)")
plt.ylabel("Hmag")
plt.ylim((np.min(H), np.max(H)))
plt.legend()
plt.title("Hmag vs SMA")
plt.savefig("../plots/HmagvsSMA/plot.svg")
plt.close()