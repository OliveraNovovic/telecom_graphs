import networkx as nx
import os
from graph_filtering import backbone


def filtering_func(graph_bucket, alpha, all_graphs_ts, filtered_graph_path, p):
    print("filtering in thread: ", str(p))
    out = open(out_path + "graph_prop_" + str(p) + ".csv", 'w')
    out.write("ts,nodes_orig,edges_orig,nodes_filter,edges_filter" + '\n')
    for g in graph_bucket:
        ts = g.split('_')[0]
        G = nx.read_weighted_edgelist(all_graphs_ts + '\\' + g)
        g_alpha = backbone.disparity_filter(G, 'weight')
        g_filtered = nx.Graph([(u, v, d) for u, v, d in g_alpha.edges(data=True) if d['alpha'] < alpha])
        out.write(ts + ',' + str(G.number_of_nodes()) + ',' + str(G.number_of_edges()) + ','
                    + str(g_filtered.number_of_nodes()) + ',' + str(g_filtered.number_of_edges()) + '\n')
        name = ts + "_filtered.edgelist"
        nx.write_edgelist(g_filtered, filtered_graph_path + '\\' + name)
        print("Ended for graph: ", name, "bucket: ", p)
        #Clear the graphs to release the memory
        G.clear()
        g_alpha.clear()
        g_filtered.clear()
    out.close()


if __name__ == '__main__':
    all_graphs_ts = "D:\\telecom_Italia_graphs\\graphs_timestamp"
    filtered_graph_path = "D:\\telecom_Italia_graphs\\graphs_filtered_005"
    out_path = "D:\\results\\"
    alpha = 0.05
    graphs_list = []

    for graph in os.listdir(all_graphs_ts):
        graphs_list.append(graph)

    graph_bucket_1 = graphs_list[:892]
    graph_bucket_2 = graphs_list[892:2*892]
    graph_bucket_3 = graphs_list[2*892:3*892]
    graph_bucket_4 = graphs_list[3*892:4*892]
    graph_bucket_5 = graphs_list[4*892:5*892]
    graph_bucket_6 = graphs_list[5*892:6*892]
    graph_bucket_7 = graphs_list[6*892:7*892]
    graph_bucket_8 = graphs_list[7*892:8*892]
    graph_bucket_9 = graphs_list[8*892:9*892]
    graph_bucket_10 = graphs_list[9*892:]

    filtering_func(graph_bucket_3, alpha, all_graphs_ts, filtered_graph_path, "b3")

    print("We are done here.")



