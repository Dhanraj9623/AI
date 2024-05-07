from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start):
        visited = [False] * (8)
        self.dfs_util(start, visited)

    def bfs(self, start):
        visited = [False] * (8)                           #-----------
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            v = queue.popleft()
            print(v, end=' ')

            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = Graph()

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,6)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(4,7)
g.add_edge(5,2)



start_node = 0
print("DFS traversal starting from node", start_node)
g.dfs(start_node)
print("\nBFS traversal starting from node", start_node)
g.bfs(start_node)