#*****************************
# nome: Paria 
# cognome: Haji Abolfath 
# 2044012
#*****************************

import networkx as nx
from numpy import array, where

folder='DHFR'
inFile='DHFR_graph_indicator.txt' # graph indicator
inAdj= 'DHFR_A.txt' # adjecency list in same folder
inEdgeLabel = 'DHFR_edge_labels.txt'

# 1. compute number of nodes
nodeCount = 0
node_graph_id = [] # the index i is in graph node_graph_id[i]

graphs = [] # a list of graphs
for _ in range(394):
    graph = nx.DiGraph() # directed graph
    graphs.append(graph)

with open('/'.join([folder,inFile])) as tmp:
    for line in tmp.readlines():
        # so each line corresponds 
        lineIndex = int(line)-1 # 0 based indexing
        # print(lineIndex)
        node_graph_id.append(int(line))
        nodeCount = nodeCount + 1
print(nodeCount) #9380

# 394, because 0 is not considered in graph indexing. graph labels start from 1 until 393
graph_node_count = [1] * 394 # at index i, graph_node_count[i] holds the number of nodes that graph i owns
for i in range (len(node_graph_id)): # i here is graph index, the value inside the list is the number of nodes it owns
    if i==0:
        graph_node_count[i] = 0
    if i!=0:
        # if i==1:
        #     graph_node_count[i] = 1
        if node_graph_id[i] == node_graph_id[i-1]: # encounter of another node of the same graph
            graph_node_count[node_graph_id[i-1]] = graph_node_count[node_graph_id[i-1]] + 1 
        else:
            graph_node_count[node_graph_id[i]]=1

# print(min(node_graph_id)) # 1
# print(max(node_graph_id)) # 393

# print(len(graph_node_count)) # 394
# print(graph_node_count[0]) #0 - no graph with label 0
# print(graph_node_count[2]) #17

# add to graph i (from 1 to 393) 
node_idx=1
for i in range (1, len(graph_node_count)): # 394
    if i>1:
        node_idx=j+node_idx+1
    for j in range(0, graph_node_count[i]): 
        graphs[i].add_node(j+node_idx)

# add edges : 
node_idx = 1
edge_list = []
edge_list.append((0, 0))
with  open('/'.join([folder, inAdj])) as tmp :
    for line in tmp.readlines():
        ni,nj = [ int(a) for a in line.split(',')]
        edge_list.append((ni, nj))

# edge labels
edge_label =[]
edge_label.append(0)
with  open('/'.join([folder, inEdgeLabel])) as tmp :
    for line in tmp.readlines():
        edge_label.append(int(line))         
      
graph_idx=1
# c=0
for j in range(1, len(edge_list)):
    nodes_ = graphs[graph_idx].nodes()
    v1, v2 = edge_list[j]
    if (v1 in nodes_) & (v2 in nodes_):
        graphs[graph_idx].add_edge(v1, v2, weight=edge_label[j])
        # if graph_idx==1:
        #     c+=1
        #     print("adding edge ", v1, ", ", v2, " with count ", c)
    else:
        graph_idx = graph_idx + 1

# writing degrees to txt file
f = open("texts/DegOut.txt", "a")
for i in range (1, len(graph_node_count)): # 394
    for j in (graphs[i].nodes):
        f.write(str((graphs[i]).degree[j]))
        f.write("\n")
f.close()

# writing Closeness Centrality to txt file
f = open("texts/ClosOut.txt", "a")
for i in range (1, len(graph_node_count)): # 394
    node_dic = nx.closeness_centrality(graphs[i])
    for key, value in node_dic.items():
        f.write(str(key))
        f.write(",")
        f.write(str(value))
        f.write("\n")
f.close()

# writing Betweenness Centrality to txt file
f = open("texts/BetOut.txt", "a")
for i in range (1, len(graph_node_count)): # 394
    node_dic = nx.betweenness_centrality(graphs[i])
    for key, value in node_dic.items():
        f.write(str(key))
        f.write(",")
        f.write(str(value))
        f.write("\n")
f.close()
    


