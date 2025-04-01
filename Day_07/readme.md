# 1. Single element in sorted array
## Problem Statement

You are given a sorted array `nums` that contains integers. Every element appears exactly twice except for one element, which appears only once. Your task is to find the single element that appears only once.

### Examples

1. **Example 1**
   - **Input:** `nums = [1, 1, 2, 2, 3, 3, 4, 4, 5]`
   - **Output:** `5`
   - **Explanation:** The number `5` appears only once, while all other numbers appear twice.

2. **Example 2**
   - **Input:** `nums = [2, 2, 3, 3, 4, 4, 5]`
   - **Output:** `5`
   - **Explanation:** Again, `5` is the only number that appears once.

3. **Example 3**
   - **Input:** `nums = [1, 2, 2, 3, 3]`
   - **Output:** `1`
   - **Explanation:** Here, `1` is the unique element.

### Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- The array is sorted.

## Code Explanation

Here’s the implementation of the solution:

```python
class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Check first and last element for uniqueness
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        # Binary search algorithm to find the single element
        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is the single element
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            
            # Determine the half to continue searching
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
```

### Logic and Working of the Code

1. **Input Handling:**
   - The function starts by determining the length of the input list `nums`.
   - If the length is `1`, it returns that single element since it’s the answer.
   - It checks if the first or the last elements are unique, returning one of them immediately if so.

2. **Binary Search Approach:**
   - The method uses a binary search technique to efficiently find the unique number.
   - It initializes two pointers, `low` (starting from 1) and `high` (ending at `n-2`), for searching within the array.
   - The middle index `mid` is calculated during each iteration.

3. **Checking for Uniqueness:**
   - The code checks if the current `mid` element is unique by comparing it with its neighbors (`mid-1` and `mid+1`).
   - If it is found to be unique, it returns `nums[mid]`.

4. **Searching Logic:**
   - The algorithm divides the array based on conditions that relate the value of `mid` (whether it's even or odd) and its neighbors:
     - If `mid` is odd and matches the left neighbor, or if `mid` is even and matches the right neighbor, the unique element must be in the right half since pairs would be formed correctly up to `mid`. Thus, it sets `low = mid + 1`.
     - Otherwise, it narrows down the search to the left half by setting `high = mid - 1`.

5. **Completion:**
   - The process continues until `low` surpasses `high`, ensuring that the loop only examines valid parts of the sorted array.
   - If no unique element is found (which theoretically should not happen given the guarantees of the problem), it returns `-1`.

### Time Complexity

- The average time complexity of this solution is **O(log n)** because it employs a binary search approach over the sorted list.

### Space Complexity

- The space complexity is **O(1)** since we are not using any additional data structures that grow with input size.

This efficient solution ensures you can handle large lists while finding the single unique number quickly! If you need any further clarification or details, feel free to ask!