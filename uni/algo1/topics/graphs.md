# Graph Algorithms

## Representations

### Adjacency List (most common)
```python
from collections import defaultdict

adj = defaultdict(list)
adj[u].append(v)
adj[v].append(u)  # undirected
```

### Weighted Adjacency List
```python
adj = defaultdict(list)
adj[u].append((v, weight))
```

## BFS - Breadth First Search

$O(V + E)$

```python
from collections import deque

def bfs(start, adj, n):
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    return dist
```

## DFS - Depth First Search

$O(V + E)$

```python
def dfs(u, adj, visited):
    visited.add(u)
    for v in adj[u]:
        if v not in visited:
            dfs(v, adj, visited)

# Iterative (avoids recursion limit)
def dfs_iterative(start, adj):
    visited = set()
    stack = [start]

    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                stack.append(v)

    return visited
```

## Dijkstra's Algorithm

$O((V + E) \log V)$

```python
import heapq

def dijkstra(start, adj, n):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist
```

## Topics to Add

- [ ] Bellman-Ford
- [ ] Floyd-Warshall
- [ ] Topological Sort
- [ ] Strongly Connected Components
- [ ] Minimum Spanning Tree (Kruskal, Prim)
