#!/usr/bin/env python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
plt.style.use('tableau-colorblind10')

# Args
df19 = pd.read_csv("escaped_19.csv")
pt19 = np.array(df19["particle"])
t19 = np.array(df19["t"])
df25 = pd.read_csv("escaped_25.csv")
pt25 = np.array(df25["particle"])
t25 = np.array(df25["t"])

particleNo = np.concatenate([pt19 - 7, pt25 + 2])
time = np.concatenate([t19, t25])

# Build histogram
plt.figure(1, figsize=(8, 6))
plt.hist(time, bins = 8)
plt.xlabel("Time (years)", fontsize=18)
plt.ylabel("Count", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.title("Histogram of escape times for the clones of asteroids 19 and 25", fontsize=22)
svgtitle = "../../../plots/HistogramEscapeTimes/HistogramEscapeTimes.svg"
pngtitle = "../../../plots/HistogramEscapeTimes/HistogramEscapeTimes.png"
plt.savefig(svgtitle)
plt.close()
os.system("convert {} {}".format(svgtitle, pngtitle))