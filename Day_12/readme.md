# 1. Linear Search

### Problem Statement

You have been given a random integer array `arr[]` of size `N`, and an integer `X`. You need to search for the integer `X` in the given array using the **Linear Search** algorithm.

Return the index at which `X` is present in the array.  
- If `X` has multiple occurrences, return the **first** index at which it occurs.  
- If `X` is not present in the array, return `-1`.

**Note:**  
Linear search is a method for finding an element within an array. It sequentially checks each element until a match is found or the entire array has been searched.

### Example

#### Example 1:
**Input:**
```
arr = [4, 2, 7, 1, 9]
x = 7
```
**Output:** `2`  
**Explanation:** `7` is found at index `2`.

#### Example 2:
**Input:**
```
arr = [5, 8, 6, 2]
x = 3
```
**Output:** `-1`  
**Explanation:** `3` is not found in the array.

### Approach

We use a simple **linear search** strategy:
- Traverse the array from the beginning.
- Compare each element with the target `X`.
- If found, return the index immediately.
- If not found by the end of the array, return `-1`.

### Why Linear Search?

- Simple and effective for small or unsorted arrays.
- No additional space is required.
- Although not optimal for large datasets, it is easy to implement and sufficient when performance isn't critical.

### Solution

```python
def linearSearch(arr, n, val):
    for i in range(n):
        if arr[i] == val:
            return i
    return -1
```

### Time & Space Complexity

- **Time Complexity:** O(N)  
  We may need to scan all elements in the worst case.

- **Space Complexity:** O(1)  
  No extra space is used apart from loop variables.