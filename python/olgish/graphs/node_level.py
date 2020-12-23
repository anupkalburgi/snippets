def nodes_at_levels(graph, source):
    '''
    we want level wise information
    {
        0 : [a]
        1 : [1,2]
        2 : [3,4]
    }
    '''
    level_info = {}
    q = [source]
    level_count = 0
    while q:
        level_info[level_count] = q.copy() # the risk of this could be that we are storing a reference to queue and not a copy
        level_count = level_count + 1
        qsize = len(q)
        for _ in range(qsize):
            node = q.pop(0)
            for neighbhours in graph[node]:
                q.append(neighbhours)
    return level_info
                
graph = {
    0 : [1,2],
    1: [3,4],
    3: [],
    4: [],
    2: []
}
print(nodes_at_levels(graph, 0))
