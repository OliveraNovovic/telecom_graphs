import community as community_louvain
import networkx as nx
import os


def edge_list_parser(file):
    graph = nx.Graph()
    gf = open(file)
    lines = gf.readlines()
    for line in lines:
        elements = line.split(" ")
        node1 = int(elements[0])
        node2 = int(elements[1])
        weight = float(elements[3].strip(','))
        graph.add_edge(node1, node2, weight=weight)

    gf.close()
    return graph


filtered_graphs = "D:\\telecom_Italia_graphs\\graphs_filtered_005\\"

out_file = open("communities.csv", 'w')
out_file.write("ts,comm_num,communities" + '\n')
counter = 0
for g in os.listdir(filtered_graphs):
    ts = g.split('_')[0]
    G = edge_list_parser(filtered_graphs + g)
    G.remove_edges_from(nx.selfloop_edges(G))
    partition = community_louvain.best_partition(G, weight='weight')
    out_file.write(ts + ',' + str(len(partition)) + ',' + str(partition) + '\n')
    counter += 1
    print(counter)
    G.clear()
    partition.clear()

out_file.close()



