```plain text
# 1. Floor and Ceil of a Number in a Sorted Array

## Problem Statement
Given a sorted array `a` of size `n` and a target value `x`, find:
- **Floor**: The largest number in `a` that is **≤ x**.
- **Ceil**: The smallest number in `a` that is **≥ x**.

If no floor or ceil exists, return `-1` for that value.

## Approach
1. Initialize `left = 0`, `right = n - 1`, `floor = -1`, `ceil = -1`.
2. Perform a binary search:
   - Compute `mid = left + (right - left) // 2`.
   - If `a[mid] == x`, return `(x, x)` (both floor and ceil are `x`).
   - If `a[mid] < x`, update `floor = a[mid]` and search in the right half (`left = mid + 1`).
   - If `a[mid] > x`, update `ceil = a[mid]` and search in the left half (`right = mid - 1`).
3. Return `(floor, ceil)` after binary search completes.

## Pseudo-code
```python
def getFloorAndCeil(a, n, x):
    left, right = 0, n - 1
    floor, ceil = -1, -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if a[mid] == x:
            return (a[mid], a[mid])
        
        if a[mid] < x:
            floor = a[mid]
            left = mid + 1
        else:
            ceil = a[mid]
            right = mid - 1
    
    return (floor, ceil)
```

## Complexity Analysis
- **Time Complexity:** `O(log n)` (Binary search halves the search space each iteration)
- **Space Complexity:** `O(1)` (Uses constant extra space)

## Example
### Input
```python
a = [1, 2, 8, 10, 10, 12, 19]
n = len(a)
x = 5
print(getFloorAndCeil(a, n, x))
```

### Output
```
(2, 8)
```

### Additional Cases
#### Case 1: `x = 6` in `[1, 3, 5, 7, 9]`
**Output:** `(5, 7)`

#### Case 2: `x = 20` in `[1, 2, 5, 10]`
**Output:** `(10, -1)` (No ceil exists)

#### Case 3: `x = 0` in `[3, 4, 6, 8]`
**Output:** `(-1, 3)` (No floor exists)
```

------------------------------------------------------------------------------------------------------------
# 2. Occurance of number in sorted arr with duplicates

------------------------------------------------------------------------------------------------------------
# 3. Find the first or last occurance of given number


