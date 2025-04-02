# Day 2-7 Revision
# Binary Search Revision from file 1 to file 5
--------------------------------------------------------------------------------------
# 6. Largest element in array
## Description
This program defines a Python class `Solution` that contains a method `largest` to find the largest element in a given list of numbers. The function iterates through the list and updates the largest element found.

## Implementation
The `largest` function follows these steps:
1. Initialize `largest` with the first element of the list.
2. Iterate through the rest of the list.
3. Compare each element with the current `largest` and update it if a larger value is found.
4. Return the largest element found.

## Code
```python
from typing import List

class Solution:
    def largest(self, arr: List[int]) -> int:
        largest = arr[0]
        n = len(arr)
        for i in range(1, n):
            if largest < arr[i]:
                largest = arr[i]
        return largest
```

## Example Usage
```python
sol = Solution()
numbers = [3, 5, 7, 2, 8, 10, 1]
print(sol.largest(numbers))  # Output: 10
```

## Complexity Analysis
- **Time Complexity**: O(n) since the function iterates through the list once.
- **Space Complexity**: O(1) as only a single variable (`largest`) is used to store the maximum value.

## Edge Cases Considered
- The list contains all negative numbers.
- The list contains only one element.
- The list contains duplicate largest elements.
- The list is already sorted in ascending or descending order.
--------------------------------------------------------------------------------------
# 7. Second Largest Element in an Array without sorting