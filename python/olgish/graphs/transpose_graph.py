import collections
def transpose(graph):
    t_graph = collections.defaultdict(list)
    
    for node, neighbours in graph.items():
        for ngh in neighbours:
            t_graph[ngh].append(node)
    

    return t_graph


graph_al = {
    0 : [2,1],
    1 : [4,3],
    2 : [],
    3 : [],
    4 : []
}

print(transpose(graph_al))