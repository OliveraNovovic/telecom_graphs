import os
import zipfile
import pandas as pd
import networkx as nx


def make_graph(df, ts):
    subs = df[df["timestamp"] == ts]
    name = str(ts)
    path = "D:\\telecom_Italia_graphs\\graphs_timestamp\\"
    g = nx.from_pandas_edgelist(subs, 'sq1', 'sq2', ['weight'])

    nx.write_weighted_edgelist(g, path + name + "_weighted.edgelist")


zip_file = "D:\\Telecom Italia data\\Connectivity-MI-TN\\MI-to-MI-december.zip"

schema = ["timestamp", "sq1", "sq2", "weight"]

with zipfile.ZipFile(zip_file) as z:
    for filename in z.namelist():
        print(filename)
        with z.open(filename) as f:
            df = pd.read_csv(f, sep='\t', header='infer', names=schema)
            timestamps = df["timestamp"].unique()
            for ts in timestamps:
                make_graph(df, ts)
