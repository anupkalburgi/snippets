class DFSS:
    explorededdd = []
    def dfs(self, graph, source):
        self.explorededdd.append(source)
        for neighbour in graph[source]:
            if neighbour not in self.explorededdd:
                self.dfs(graph, neighbour)
                

graph = {
    's' : ['a', 'b'],
    'a' : ['s' , 'c'],
    'b' : ['s', 'c'],
    'c' : ['a' , 'b', 'e', 'd'],
    'e' : ['c'],
    'd' : ['c']
}
dfss = DFSS()
dfss.dfs(graph, 's')
print(dfss.explorededdd)