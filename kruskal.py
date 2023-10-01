class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

def kruskal(graph):
    graph.graph = sorted(graph.graph, key=lambda item: item[2])
    parent = []
    rank = []

    def find(i):
        if parent[i] == i:
            return i
        return find(parent[i])

    def union(i, j):
        i_root = find(i)
        j_root = find(j)
        if i_root != j_root:
            if rank[i_root] < rank[j_root]:
                parent[i_root] = j_root
            elif rank[i_root] > rank[j_root]:
                parent[j_root] = i_root
            else:
                parent[j_root] = i_root
                rank[i_root] += 1

    for node in range(graph.V):
        parent.append(node)
        rank.append(0)

    result = []
    e = 0
    i = 0

    while e < graph.V - 1:
        u, v, w = graph.graph[i]
        i = i + 1
        x = find(u)
        y = find(v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(x, y)

    minimum_spanning_tree = []
    for u, v, weight in result:
        minimum_spanning_tree.append((u, v, weight))

    return minimum_spanning_tree

# ตัวอย่างการใช้งาน
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

minimum_spanning_tree = kruskal(g)
print("Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print(f"Edge: ({u}, {v}), Weight: {weight}")