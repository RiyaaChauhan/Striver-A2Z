## Problem: Maximum Consecutive Ones

You are given a binary array `nums` (i.e., it contains only `0`s and `1`s).  
Your task is to return the **maximum number of consecutive 1's** in the array.

### Example

```
Input: nums = [1, 1, 0, 1, 1, 1]
Output: 3
Explanation: The first two 1's form a streak, then a 0 breaks it, followed by a streak of three 1's.

Input: nums = [1, 0, 1, 1, 0, 1]
Output: 2
```

## Brute Force Approach

### Intuition:
Loop through the array and for every 1, start counting the length of consecutive 1's. Reset when you hit a 0.

### Code:
```python
def max_consecutive_ones_brute(nums):
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == 1:
                    count += 1
                else:
                    break
            max_count = max(max_count, count)
    return max_count
```

### Time Complexity: `O(n^2)`  
### Space Complexity: `O(1)`

### Why it fails:
- Inefficient due to nested loops. Redundant checks for already counted 1's.

## Better Approach

### Intuition:
Use a single loop to maintain a count of consecutive 1's. Reset count on encountering 0.

### Code:
```python
def max_consecutive_ones_better(nums):
    count = 0
    max_count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
```

### Time Complexity: `O(n)`  
### Space Complexity: `O(1)`

### Why not optimal:
- This is already optimal in terms of time and space.

## Optimal Approach (Same as Better)

Since the better approach already uses one traversal and no extra space, it is also considered **optimal**.

## Summary

| Approach           | Time Complexity | Space Complexity | Notes                             |
|--------------------|------------------|-------------------|------------------------------------|
| Brute Force        | O(n²)            | O(1)              | Nested loop leads to inefficiency  |
| Better (Optimal)   | O(n)             | O(1)              | Efficient single-pass solution     |