class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u,v):
            if u  not in self.graph:
                self.graph[u] =[]
            self.graph[u].append(v)
    def dfs(self, start):
        visited = set()
        self.__dfs__recursive(start, visited)
        def __dfs__recursive(self,node, visited):
            if node not in visisted:
                