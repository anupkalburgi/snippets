def shortest_path(graph, source):

    '''
    the shortest path here is from a given source to all node in the graphh
    '''
    visited = set()
    q = [source]
    visited.add(source)
    dist = {}
    for v in graph.keys():
        if v == source:
            dist[v] = 0
        else:
            dist[v] = 9999

    while q:
        node = q.pop(0)
        for n in graph[node]:
            if n not in visited:
                dist[n] = dist[node] + 1 
                visited.add(n)
                q.append(n)
    return dist
'''
in the dist dict we could have also stored a data class 
having distance and a list that is 
path leading upto it and the append the current node to that list so that we know the path it took
'''


al_graph = {
    's' : ['a', 'b'],
    'a' : ['s' , 'c'],
    'b' : ['s', 'c'],
    'c' : ['a' , 'b', 'e', 'd'],
    'e' : ['c'],
    'd' : ['c']
}
# o/p =
# al_graph = {
#     's' : 0
#     'a' : 1
#     'b' : 1
#     'c' : 2
#     'e' : 3
#     'd' : 3
#* # o/p
print(shortest_path(al_graph, 's'))    