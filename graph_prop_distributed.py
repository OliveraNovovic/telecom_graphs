import networkx as nx
import pickle
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


def write_dict_pkl(ts, dict, name):
    file_name = 'D:\\results\\' + name + '\\' + ts + '_' + name + '.pkl'
    pkl_file = open(file_name, "wb")
    pickle.dump(dict, pkl_file)
    pkl_file.close()


def local_graph_prop(graph_bucket, b, filtered_graphs_path):
    print("Local graph properties for bucket: ", str(b))
    for g in graph_bucket:
        ts = g.split('_')[0]
        G = edge_list_parser(filtered_graphs_path + g)
        G.remove_edges_from(nx.selfloop_edges(G))
        page_rank = nx.pagerank(G, weight='weight')
        bet_cent = nx.betweenness_centrality(G, weight='weight')
        clust_coef = nx.clustering(G, weight='weight')
        write_dict_pkl(ts, page_rank, 'page_rank')
        write_dict_pkl(ts, bet_cent, 'bet_cent')
        write_dict_pkl(ts, clust_coef, 'clust_coef')
        G.clear()
        page_rank.clear()
        bet_cent.clear()
        clust_coef.clear()


if __name__ == '__main__':
    filtered_graphs = "D:\\telecom_Italia_graphs\\graphs_filtered_005\\"
    graphs_list = []

    for graph in os.listdir(filtered_graphs):
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

    local_graph_prop(graph_bucket_1, "b1", filtered_graphs)

    print("We are done here.")