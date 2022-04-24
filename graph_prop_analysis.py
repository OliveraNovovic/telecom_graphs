import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np


def plotting(df):
    orig = df['density_orig']     # x axis
    filter = df['density_filter']   # y axis
    #plt.figure(figsize=(8, 8))
    plt.scatter(orig, filter)
    plt.title("Graphs density")
    plt.xlabel("Density original")
    plt.ylabel("Density after filtering")
    plt.tight_layout()
    plt.show()


data = "D:\\results\\graph_prop_bucket"

li = []

for filename in os.listdir(data):
    df = pd.read_csv(data + '\\' + filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

#print(frame.describe())

density_df = pd.read_csv("density.csv")
plotting(density_df)
#plotting(frame)


