import networkx as nx
import os
from graph_filtering import backbone
import threading

all_graphs_ts = "D:\\telecom_Italia_graphs\\graphs_timestamp"
filtered_graph_path = "D:\\telecom_Italia_graphs\\graphs_filtered_005"
out_path = "D:\\results\\"
alpha = 0.05
graphs_list = []


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
        print("Ended for graph: ", name, "thread: ", str(p))
        #Clear the graphs to release the memory
        G.clear()
        g_alpha.clear()
        g_filtered.clear()
    out.close()


for graph in os.listdir(all_graphs_ts):
    graphs_list.append(graph)


graph_bucket_1 = graphs_list[:2232]
graph_bucket_2 = graphs_list[2232:2*2232]
graph_bucket_3 = graphs_list[2*2232:3*2232]
graph_bucket_4 = graphs_list[3*2232:]

t1 = threading.Thread(target=filtering_func, args=(graph_bucket_1, alpha, all_graphs_ts, filtered_graph_path, "t1"))
#t2 = threading.Thread(target=filtering_func, args=(graph_bucket_2, alpha, all_graphs_ts, filtered_graph_path, "t2"))
#t3 = threading.Thread(target=filtering_func, args=(graph_bucket_3, alpha, all_graphs_ts, filtered_graph_path, "t3"))
#t4 = threading.Thread(target=filtering_func, args=(graph_bucket_4, alpha, all_graphs_ts, filtered_graph_path, "t4"))


t1.start()
#t2.start()
#t3.start()
#t4.start()

t1.join()
#t2.join()
#t3.join()
#t4.join()

print("We are done here.")



#print('alpha = %s' % alpha)
#print('original: nodes = %s, edges = %s' % (G.number_of_nodes(), G.number_of_edges()))
#print('backbone: nodes = %s, edges = %s' % (g_filtered.number_of_nodes(), g_filtered.number_of_edges()))
#print(g_filtered.edges(data=True))

#alpha = 0.05
#original: nodes = 7518, edges = 115972
#backbone: nodes = 3905, edges = 6909