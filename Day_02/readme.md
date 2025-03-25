# 3. Upper Bound (Last occurance)

## Problem Statement
Given a sorted array `arr[]` and an integer `x`, find the index (0-based) of the largest element in `arr[]` that is **less than or equal to `x`**. This element is called the **floor of `x`**. If such an element does not exist, return `-1`.

### Constraints:
- The input array is sorted in non-decreasing order.
- If multiple occurrences of the floor exist, return the **index of the last occurrence**.
- If no element in the array is less than or equal to `x`, return `-1`.

## Example

### Example 1
**Input:**  
```text
arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
```
**Output:**  
```text
1
```
**Explanation:**  
The largest element ≤ `5` is `2`, which is at index `1`.

### Example 2
**Input:**  
```text
arr = [3, 4, 7, 7, 8, 10]
x = 7
```
**Output:**  
```text
3
```
**Explanation:**  
The last occurrence of `7` is at index `3`, so we return `3`.

## Approach
We use **Binary Search** to find the largest element ≤ `x` efficiently:
1. Initialize `left = 0` and `right = len(arr) - 1`.
2. Maintain a variable `ans = -1` to store the index of the floor.
3. Use binary search:
   - Find the middle index `mid`.
   - If `arr[mid] ≤ x`, update `ans = mid` (as a potential answer) and move **right** to find a later occurrence.
   - If `arr[mid] > x`, move **left**.
4. Return `ans`.

## Pseudo Code
```
function findFloor(arr, x):
    left = 0
    right = length(arr) - 1
    ans = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= x:
            ans = mid  // Potential floor found
            left = mid + 1  // Move right to find last occurrence
        else:
            right = mid - 1  // Move left
    
    return ans
```

## Implementation (Python)
```python
def find_floor(arr, x):
    left, right = 0, len(arr) - 1
    ans = -1  # Default answer if no floor is found

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] <= x:
            ans = mid  # Update answer, move right for last occurrence
            left = mid + 1
        else:
            right = mid - 1  # Move left

    return ans
```

## Complexity Analysis
- **Time Complexity:** `O(log N)` (Binary search reduces search space by half in each iteration)
- **Space Complexity:** `O(1)` (Uses only constant extra space)

## Edge Cases Considered
- **x is smaller than all elements** → Return `-1`.
- **x is larger than all elements** → Return the last index.
- **x is present multiple times** → Return the last occurrence.
- **x is exactly equal to an element** → Return its last occurrence.
- **Single element array** → Handle cases where `x` is greater, smaller, or equal.

-----------------------------------------------------------------------------------------------------------------------------------