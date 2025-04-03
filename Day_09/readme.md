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
## Problem Statement
Given an array `arr`, find the **second largest** element in the array. If there is no valid second largest element (i.e., array contains less than two distinct values), return `-1`.

## Approach
We iterate through the array while keeping track of:
- The **largest element** found so far.
- The **second largest element** found so far.

### Key Steps:
1. **Initialize two variables:** `largest` and `second_largest`, both set to `-1`.
2. **Iterate through the array:**
   - If the current element is greater than `largest`, update `second_largest` to `largest` and set `largest` to the current element.
   - Otherwise, if the element is greater than `second_largest` but smaller than `largest`, update `second_largest`.
3. **Return `second_largest`, or `-1` if no valid second largest exists.**

## Implementation
```python
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1  # Not enough elements for a second largest
        
        largest = second_largest = -1
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num

        return second_largest if second_largest != -1 else -1
```

## Complexity Analysis
- **Time Complexity:** `O(n)`, since we traverse the array once.
- **Space Complexity:** `O(1)`, as we only use two extra variables.

## Example Usage
```python
solution = Solution()
print(solution.getSecondLargest([3, 1, 4, 2, 5]))  # Output: 4
print(solution.getSecondLargest([10, 10, 10]))      # Output: -1
print(solution.getSecondLargest([7]))              # Output: -1
print(solution.getSecondLargest([5, 2, 8, 8, 3]))  # Output: 5
```

## Edge Cases Considered
1. **Array with all identical values** (e.g., `[10, 10, 10]` → Output: `-1`)
2. **Array with a single element** (e.g., `[7]` → Output: `-1`)
3. **Already sorted arrays** (e.g., `[1, 2, 3, 4, 5]` → Output: `4`)
4. **Unsorted arrays with duplicates** (e.g., `[5, 2, 8, 8, 3]` → Output: `5`)