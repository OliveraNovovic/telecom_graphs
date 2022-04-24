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


filtered_graph_path = "D:\\telecom_Italia_graphs\\graphs_filtered_005"
orig_graph_path = "D:\\telecom_Italia_graphs\\graphs_timestamp"

out_file = open("density.csv", 'w')
out_file.write("ts,density_orig,density_filter" + '\n')
counter = 0

for graph in os.listdir(filtered_graph_path):
    ts = graph.split("_")[0]
    filtered = edge_list_parser(filtered_graph_path + "\\" + graph)
    orig = nx.read_weighted_edgelist(orig_graph_path + "\\" + ts + "_weighted.edgelist")

    density_filter = nx.density(filtered)
    density_orig = nx.density(orig)

    out_file.write(str(ts) + "," + str(density_orig) + "," + str(density_filter) + '\n')

    filtered.clear()
    orig.clear()

    counter += 1
    print(counter)


out_file.close()