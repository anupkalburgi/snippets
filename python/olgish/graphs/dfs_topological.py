'''
for vertix in all_vertices:
    if vertix is not in visited:
        dfs()
# this step is necessary becase we are going to have to make sure we are visiting all the nodes atleast once 
I am not sure how the given graph can be disconnected, well we can still find the maximum
possible node and backtrack from there

The only kind of requirement here is that the graph be directe with no cycles
there are few thigs that we will have to be able to deduce if a given problem is going to have cycles or no

There is a n^2 solution possible, described in the illustrated book 

step 1: find a edge node that does not have  a incoming edge, that means that will be first node in the topologivcal ordering 
    if there are mutiple of them i.e if there are multliple entry points. One is chosen at random 
    v1
step 2 we remove the source node v1 and all the associated edges and give it he leat availble value 
and contiue this

this is going to take a n^2 time 

and we can do  better using dfs which is going to take O(m + n) time 

at the depth of the tree we start assiging from the highestp possible label and moving to th lowest 


'''
# max_count = 0

# class DFSTOPO: 
#     max_count = 8 # this needs to be initialized with the class
#     visited = set()
#     ordering = {}

#     def topo(self, graph):
#         all_vertices = set()
#         for k, v in graph.items():
#             all_vertices.add(k)
#             for node in v:
#                 all_vertices.add(node)
#         for vertex in all_vertices:
#             if vertex not in self.visited:
#                 self.dfs(graph, vertex)

#     def dfs(self, graph, source):
#         stack = [source]
#         self.visited.add(source)
#         while stack:
#             node = stack.pop()
#             if node is not self.visited:
#                 self.visited.add(node)
#                 for neigbour in graph[node]:
#                     stack.append(neigbour)
#             self.ordering[node] = self.max_count
#             self.max_count = self.max_count - 1

class Solution:
    curr_label = 0000
    explored = set()
    res = {}

    def dfs_topo(self, graph, node):
        self.explored.add(node)
        for neighbour in graph[node]:
            if neighbour not in self.explored:
                self.dfs_topo(graph, neighbour)
        self.res[node] = self.curr_label
        self.curr_label = self.curr_label - 1

    def topo_order(self, graph):
        all_vertices = set()
        
        for vertex , neighbours in graph.items():
            all_vertices.add(vertex)
            for neighbour in neighbours:
                all_vertices.add(neighbour)
        self.curr_label = len(all_vertices)
        
        for v in all_vertices:
            if v not in self.explored:
                self.dfs_topo(graph, v)
        return self.res 


graph_all = {
    's' : ['v', 'w'],
    'v' : ['t'] ,
    'w' : ['t'] ,
    't' : []
}
sol = Solution()
print(sol.topo_order(graph_all))