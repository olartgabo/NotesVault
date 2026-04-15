# Segment Tree

Point update, range query in $O(\log n)$.

## Basic Implementation

```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        # Build tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, i, val):
        """Set arr[i] = val"""
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def query(self, l, r):
        """Sum of arr[l:r] (exclusive r)"""
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res
```

## Usage

```python
arr = [1, 3, 5, 7, 9, 11]
st = SegTree(arr)

print(st.query(1, 4))  # 3 + 5 + 7 = 15
st.update(2, 10)       # arr[2] = 10
print(st.query(1, 4))  # 3 + 10 + 7 = 20
```

## Min/Max Segment Tree

```python
class MinSegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])

    def query(self, l, r):
        res = float('inf')
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = min(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = min(res, self.tree[r])
            l //= 2
            r //= 2
        return res
```

## Variants

- **Lazy Propagation**: Range updates in $O(\log n)$
- **Persistent**: Query historical versions
- **2D Segment Tree**: Range queries on 2D grid
