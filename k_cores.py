import os
import networkx as nx


filtered_graphs = "D:\\telecom_Italia_graphs\\graphs_filtered_005\\"
k_core_path = "D:\\telecom_Italia_graphs\\k_core\\"
core_num_path = "D:\\results\\core_number\\"
out_file = open(core_num_path + "core_num.csv", 'w')
out_file.write("ts;core_number" + '\n')
counter = 0

for g in os.listdir(filtered_graphs):
    ts = g.split('_')[0]
    G = nx.read_edgelist(filtered_graphs + g)
    G.remove_edges_from(nx.selfloop_edges(G))
    k_core = nx.k_core(G) #maximal subgraph
    nx.write_edgelist(k_core, k_core_path + ts + "_k_core.edgelist")
    core_num = nx.core_number(G)
    out_file.write(ts + ';' + str(core_num) + '\n')
    counter += 1
    print(counter)
    G.clear()
    k_core.clear()
    core_num.clear()

out_file.close()

#todo: What exactly do we need, k_core or core_num? Is the core_num graph property?
# keep the max core subgraph
# keep