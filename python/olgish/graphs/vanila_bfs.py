def print_bfs_path(graph, source):
    visited = set()
    q = [source]
    visited.add(source)
    path = []
    while q:
        node = q.pop(0)
        nghs = graph[node]
        path.append(node)
        for v in nghs:
            if v not in visited:
                visited.add(v)
                q.append(v)
                    
    
    return path

al_grap = {
    's' : ['a', 'b'],
    'a' : ['s' , 'c'],
    'b' : ['s', 'c'],
    'c' : ['a' , 'b', 'e', 'd'],
    'e' : ['c'],
    'd' : ['c']
}
print(print_bfs_path(al_grap, 's'))
# o/p = [s, a , b, c, e, d]