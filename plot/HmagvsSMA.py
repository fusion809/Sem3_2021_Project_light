import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')
import numpy as np

# Get required data
dat = pd.read_csv("HmagvsSMA.csv")
IDs = dat["ID"]
H = dat["Hmag"]
a = dat["SMA"]
alin = np.linspace(np.min(a), np.max(a), 10001)
C = 3.5e-5
Hpred = 5*np.log10(np.abs(alin-a[0])/C)

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