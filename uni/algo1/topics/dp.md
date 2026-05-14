# Dynamic Programming

## Core Concepts

1. **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
2. **Overlapping Subproblems**: Same subproblems solved multiple times

## Common Patterns

### 1D DP - Linear Recurrence

**Fibonacci**
```python
def fib(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# With memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### 2D DP - Grid Problems

**Unique Paths**
```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
```

### Knapsack Problems

**0/1 Knapsack** - $O(nW)$
```python
def knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for cap in range(W, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[W]
```

**Unbounded Knapsack**
```python
def unbounded_knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for cap in range(W + 1):
        for w, v in zip(weights, values):
            if cap >= w:
                dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[W]
```

### LCS - Longest Common Subsequence

$O(nm)$

```python
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]
```

### LIS - Longest Increasing Subsequence

$O(n \log n)$

```python
from bisect import bisect_left

def lis(arr):
    dp = []
    for x in arr:
        pos = bisect_left(dp, x)
        if pos == len(dp):
            dp.append(x)
        else:
            dp[pos] = x
    return len(dp)
```

## Topics to Add

- [ ] Bitmask DP
- [ ] Digit DP
- [ ] Tree DP
- [ ] DP on DAG
