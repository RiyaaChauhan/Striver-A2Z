# 1. Check If Array is Sorted and Rotated

## Problem Statement
Given an integer array `nums`, determine if it is a sorted array that has been **rotated**. A sorted array means non-decreasing order, and rotation means some elements have been shifted circularly.

### **Example**
#### **Valid Rotated Sorted Arrays:**
```
[3, 4, 5, 1, 2]  → True (Rotated version of [1, 2, 3, 4, 5])
[5, 1, 2, 3, 4]  → True (Rotated version of [1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]  → True (Already sorted)
```
#### **Invalid Cases:**
```
[2, 1, 3, 4]    → False (Not a rotated sorted array)
[3, 2, 1, 5, 4] → False (Not sorted at all)
```

## Approach
We count how many times the order is violated (i.e., `nums[i] > nums[i+1]`).
- If the count is **at most 1**, it means the array is a rotated sorted array.
- If the count is **more than 1**, then it's not a rotated sorted array.

### **Algorithm**
1. Initialize `count = 0`.
2. Iterate through the array:
   - If `nums[i] > nums[(i + 1) % n]`, increment `count`.
3. If `count` exceeds `1`, return `False`, otherwise return `True`.

## Implementation
```python
class Solution:
    def check(self, nums):
        n = len(nums)
        count = 0  # Count the number of out-of-order pairs

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Compare with next element (circular)
                count += 1
            if count > 1:  # More than 1 disorder means not a rotated sorted array
                return False

        return True  # At most 1 disorder means it's a rotated sorted array
```

## Complexity Analysis
- **Time Complexity:** `O(n)`, since we traverse the array once.
- **Space Complexity:** `O(1)`, since we use only one extra variable.

## Test Cases
```python
sol = Solution()
print(sol.check([3, 4, 5, 1, 2]))  # Output: True
print(sol.check([2, 1, 3, 4]))     # Output: False
print(sol.check([1, 2, 3, 4, 5]))  # Output: True
print(sol.check([1, 1, 1, 1, 1]))  # Output: True
print(sol.check([5, 1, 2, 3, 4]))  # Output: True
print(sol.check([3, 2, 1, 5, 4]))  # Output: False
```

## Edge Cases Considered
1. **Already sorted array** (e.g., `[1, 2, 3, 4, 5]` → Output: `True`)
2. **Array rotated by one element** (e.g., `[5, 1, 2, 3, 4]` → Output: `True`)
3. **Unsorted array** (e.g., `[3, 2, 1, 5, 4]` → Output: `False`)
4. **Array with all identical elements** (e.g., `[1, 1, 1, 1]` → Output: `True`)
5. **Array with only two elements** (e.g., `[2, 1]` → Output: `True`)