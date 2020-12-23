class DFSI:
    explored = set()
    path = []

    def dfs(self , graph,source):
        s = [source]
        while s:
            node = s.pop()
            if node not in self.explored:
                self.explored.add(node)
                self.path.append(node)
                for neighbour in graph[node]:
                    if neighbour not in self.explored:
                        s.append(neighbour)
dss = DFSI()
al_graph = {
    's' : ['a', 'b'],
    'a' : ['s' , 'c'],
    'b' : ['s', 'c'],
    'c' : ['a' , 'b', 'e', 'd'],
    'e' : ['c'],
    'd' : ['c']
}
dss.dfs(al_graph, 's')
print(dss.path)