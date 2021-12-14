import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dat = pd.read_csv("HmagvsSMA.csv")
IDs = dat.iloc[:, 0]
H = dat.iloc[:, 1]
a = dat.iloc[:, 2]

plt.figure(1)
plt.scatter(a, H)
plt.xlabel("Semimajor axis (AU)")
plt.ylabel("Hmag")
plt.title("Hmag vs SMA")
plt.show()