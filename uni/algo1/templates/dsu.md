# Disjoint Set Union (Union-Find)

Near $O(1)$ amortized operations with path compression and union by rank.

## Implementation

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

## Usage

```python
dsu = DSU(n)
dsu.union(0, 1)
dsu.union(1, 2)
print(dsu.connected(0, 2))  # True
print(dsu.components)        # n - 2
```

## Applications

- **Kruskal's MST**: Process edges by weight, unite if not connected
- **Connected Components**: Unite all edges, count components
- **Cycle Detection**: If `find(u) == find(v)` before `union(u, v)`, cycle exists

## Kruskal's MST Example

```python
def kruskal(n, edges):
    """edges: list of (weight, u, v)"""
    edges.sort()
    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []

    for w, u, v in edges:
        if dsu.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges
```
