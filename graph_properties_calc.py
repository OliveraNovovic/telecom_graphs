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


filtered_graphs = "D:\\telecom_Italia_graphs\\graphs_filtered_005\\"


def write_dict_pkl(ts, dict, name):
    file_name = 'D:\\results\\' + name + '\\' + ts + '_' + name + '.pkl'
    pkl_file = open(file_name, "wb")
    pickle.dump(dict, pkl_file)
    pkl_file.close()


counter = 0
for g in os.listdir(filtered_graphs):
    ts = g.split('_')[0]
    G = edge_list_parser(filtered_graphs + g)
    G.remove_edges_from(nx.selfloop_edges(G))
    page_rank = nx.pagerank(G, weight='weight')
    bet_cent = nx.betweenness_centrality(G, weight='weight')
    clust_coef = nx.clustering(G, weight='weight')
    write_dict_pkl(ts, page_rank, 'page_rank')
    write_dict_pkl(ts, bet_cent, 'bet_cent')
    write_dict_pkl(ts, clust_coef, 'clust_coef')
    counter += 1
    print(counter)
    G.clear()
    page_rank.clear()
    bet_cent.clear()
    clust_coef.clear()






