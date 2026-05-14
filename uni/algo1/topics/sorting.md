# Sorting Algorithms

## Overview

Sorting is fundamental to competitive programming. Most problems require sorted data for binary search, two pointers, or greedy approaches.

## Complexity Summary

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Timsort (Python) | $O(n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| Quick Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No |
| Merge Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| Counting Sort | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | $O(k)$ | Yes |

## Python Sorting

```python
# Default ascending
arr.sort()
sorted_arr = sorted(arr)

# Descending
arr.sort(reverse=True)

# Custom key function
arr.sort(key=lambda x: x[1])  # sort by second element

# Multiple criteria
arr.sort(key=lambda x: (x[0], -x[1]))  # asc by first, desc by second

# Sort with custom comparison (slower)
from functools import cmp_to_key
arr.sort(key=cmp_to_key(lambda a, b: a - b))
```

## Common Patterns

### Coordinate Compression
```python
def compress(arr):
    sorted_unique = sorted(set(arr))
    mapping = {v: i for i, v in enumerate(sorted_unique)}
    return [mapping[x] for x in arr]
```

### Sorting Tuples by Second Element
```python
pairs = [(1, 3), (2, 1), (3, 2)]
pairs.sort(key=lambda x: x[1])  # [(2, 1), (3, 2), (1, 3)]
```

### Finding Kth Smallest (O(n) average)
```python
import heapq
# Kth smallest
kth = heapq.nsmallest(k, arr)[-1]
# Kth largest
kth = heapq.nlargest(k, arr)[-1]
```
