'''
from the book algorithms illuminated 
this is very much like connected islands 
but his is in adjucency list 

so there can we two versions of this problem 
1. to find number of connected graphs 
2. the list [list] connected islands - here we can also track the graph component that it is connecteded to. 
depeding on a problem that can be usefull 



visted = set()
all_vertices = []
connnected_count = 0 
for v in all_vertices: 
    if v is not visited:
        call_bfs
        connected_count = connected_count +  1 

    def bfs(source):
        q = [source]
        while q:
            node = q.pop(0)
            for n in graph[node]:
                if n not in visted:
                    visted.add(n)
                    q.append(n)

'''
    
def connected_components(graph):

    '''
    Is going to return count of connected islands
    '''

    visited  = set()
    all_vertices = set()
    connected_count = 0

    for k, v in graph.items():
        all_vertices.add(k)
        for nghs in v:
            all_vertices.add(nghs)

    # if i were to move it out to a function. bfs(graph, source, visted)
    def bfs(source):
        q = [source]
        path = []
        visited.add(source)
        while q:
            qnode = q.pop(0)
            path.append(qnode)
            nghs = graph[qnode]
            for nn in nghs:
                if nn not in visited:
                    visited.add(nn)
                    q.append(nn)
        return path

    clusters = []
    for node in all_vertices:
        if node not in visited:
            path =  bfs(node) # if we want a list[list] then we can have this method take a empty list as wel
            clusters.append(path)
            connected_count = connected_count + 1

    return (connected_count,clusters)

graph = {
    'a' :['b', 'c'],
    'b' : ['a' , 'c'],
    'c' : ['a', 'b' , 'd', 'e'],
    'd' : ['c'],
    'e' : ['c'],
    'f' : ['g'],
    'g' : ['f'],
    'h' : ['i','j'],
    'i' : ['h'],
    'j' : ['h']
}
print(connected_components(graph))