import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import numpy as np

# Get required data
dat = pd.read_csv("HmagvsSMA.csv")
IDs = dat["ID"]
H = dat["Hmag"]
a = dat["SMA"]
aC = a[0]
alin = np.linspace(np.min(a), np.max(a), 10001)
C = 3.5e-5
Hpred = 5*np.log10(np.abs(alin-aC)/C)
Cvec = np.array([2.5, 3.5]) * 1e-5
rho = 1.5
pV = 0.06
tage = 1e9 * (Cvec*1e4) * (aC/2.5)**2 * (rho/2.5) * np.sqrt(0.2/pV)
print("tage = {}".format(tage))

# Plot it
plt.figure(1, figsize=(8, 6))
plt.scatter(a, H, label="Asteroid values")
plt.plot(alin, Hpred, label="Predicted values with C={}".format(C))
plt.xlabel("Semimajor axis (AU)", fontsize=20)
plt.xticks(fontsize=16)
plt.ylabel("H magnitude", fontsize=20)
plt.yticks(fontsize=16)
plt.ylim((np.min(H), np.max(H)))
plt.legend(loc="best", fontsize=14)
plt.title("H magnitude vs semi-major axis", fontsize=24)
plt.savefig("../plots/HmagvsSMA/plotC{}.svg".format(C))
plt.close()