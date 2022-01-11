#!/usr/bin/env python
import pandas as pd

no = 25
df = pd.read_csv("../output/ordinary/output/parameters_" + str(no) + ".csv")
a = df["a"]
for i in range(0, 8):
    print("For clone = {}".format(i+1))
    print("a at start of simulation = {}\n".format(a[81600 +  i*10000]))