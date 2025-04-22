from collections import deque

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = [[0]*len(nodes) for _ in nodes]

    def add_edge(self, u, v):
        i, j = self.nodes.index(u), self.nodes.index(v)
        self.adj[i][j] = self.adj[j][i] = 1

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        print("\nBFS Traversal:")
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                print(f"Visited: {node}, Queue: {list(queue)}")
                i = self.nodes.index(node)
                for j, is_edge in enumerate(self.adj[i]):
                    if is_edge and self.nodes[j] not in visited and self.nodes[j] not in queue:
                        queue.append(self.nodes[j])
        print("Final BFS Traversal Order:", list(visited))

    def dfs(self, start):
        visited = set()
        stack = [start]
        print("\nDFS Traversal:")
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(f"Visited: {node}, Stack: {list(stack)}")
                i = self.nodes.index(node)
                for j in reversed(range(len(self.nodes))):
                    if self.adj[i][j] and self.nodes[j] not in visited and self.nodes[j] not in stack:
                        stack.append(self.nodes[j])
        print("Final DFS Traversal Order:", list(visited))

# Input
nodes = input("Enter node names (space-separated): ").split()
g = Graph(nodes)
print("Enter adjacency matrix row by row:")
for i in range(len(nodes)):
    row = input().split()
    for j in range(len(nodes)):
        if row[j] == '1':
            g.add_edge(nodes[i], nodes[j])
start = input("Enter start node for BFS and DFS: ")
g.bfs(start)
g.dfs(start)
