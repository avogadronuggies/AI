class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_matrix = [[0] * len(nodes) for _ in nodes]

    def add_edge(self, u, v):
        i, j = self.nodes.index(u), self.nodes.index(v)
        self.adj_matrix[i][j] = self.adj_matrix[j][i] = 1

    def bfs(self, start):
        visited, queue, traversal_order = set(), [start], []
        print("\nBFS Traversal:")
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                index = self.nodes.index(node)
                for i, is_edge in enumerate(self.adj_matrix[index]):
                    if is_edge and self.nodes[i] not in visited and self.nodes[i] not in queue:
                        queue.append(self.nodes[i])
                print(f"Visited: {node}, Queue: {queue}")
        print("Final BFS Traversal Order:", traversal_order)

    def dfs(self, start):
        visited, stack, traversal_order = set(), [start], []
        print("\nDFS Traversal:")
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                index = self.nodes.index(node)
                for i in reversed(range(len(self.nodes))):
                    if self.adj_matrix[index][i] and self.nodes[i] not in visited and self.nodes[i] not in stack:
                        stack.append(self.nodes[i])
                print(f"Visited: {node}, Stack: {stack}")
        print("Final DFS Traversal Order:", traversal_order)

if __name__ == "__main__":
    nodes = input("Enter node names (space-separated): ").split()
    g = Graph(nodes)
    print("Enter adjacency matrix row by row:")
    for i in range(len(nodes)):
        row = input().split()
        for j, val in enumerate(row):
            if val == '1':
                g.add_edge(nodes[i], nodes[j])
    start_node = input("Enter start node for BFS and DFS: ")
    g.bfs(start_node)
    g.dfs(start_node)

# Sample Input:
# Enter node names (space-separated): A B C D
# Enter adjacency matrix row by row:
# 0 1 0 0
# 1 0 1 1
# 0 1 0 0
# 0 1 0 0
# Enter start node for BFS and DFS: A
