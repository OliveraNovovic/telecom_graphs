import pandas as pd
import networkx as nx

data_path = "D:\\Telecom Italia data\\Connectivity-MI-TN\\"

schema = ["timestamp", "sq1", "sq2", "weight"]

df = pd.read_csv(data_path + "MItoMI-2013-11-01.txt", sep='\t', header='infer', names=schema)


#print(df.sort_values(by=['timestamp']))
#df['datetime'] = pd.to_datetime(df['timestamp']/1000, unit='s')

#df = df.drop('timestamp', 1)

#grouped = df.groupby(["datetime", "sq1", "sq2"]).sum("weight")

#todo: do this for each timestamp

subs = df[df["timestamp"] == 1383260400000]
name = "1383260400000"
g = nx.from_pandas_edgelist(subs, 'sq1', 'sq2', ['weight'])

nx.write_weighted_edgelist(g, name + "_weighted.edgelist")
