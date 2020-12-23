# This was problem was taken from educative io
# for this to solve properly we have to fist solve the transpose problem
# https://www.educative.io/courses/algorithms-coding-interviews-python/myj0v2P4mYE
'''
the idea behind kosaraju's algotrithm is 
make sure you can connect all the nodes from a given node any random node for that matter 
and the make sure every one else can reach the same node that way we can be  sure that we can reach all any node from any node
and why that is corret ?
'''

def bfs(graph, vertex):
    visited = set()
    path = []        
    qu = [vertex]
    while qu:
        node = qu.pop()
        visited.add(node)
        path.append(node)
        for ngh in graph[node]:
            if ngh not in visited:
                qu.append(ngh)
    return path

def strongly_connected(graph):
    '''
    woulf return true if there is path between each pair 
    this is going to be a O(n(m+n))
    may be using matrix approach might help to get it to n^2?

    '''

    all_vertices = set()
    for node, neighbours in graph.items():
        all_vertices.add(node)
        for ngh in neighbours:
            all_vertices.add(ngh)

    for vertex in all_vertices:
        path = bfs(graph, vertex)
        if len(path) != len(all_vertices):
            return False

    return True





# graph_al = {
#     0 : [1],
#     1 : [2],
#     2 : [3,4],
#     3 : [0],
#     4 : [2]
# }
graph_al = {
      0 : [1]
    , 1 : [2]
    , 2 : [3]
    , 3 : []
}
print(strongly_connected(graph_al))

