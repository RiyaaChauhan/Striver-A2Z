# 1. Search Insert Position

## Problem Statement
Given a **sorted array** of **distinct integers** and a **target** value, return the **index** if the target is found. If not, return the **index where it would be** if it were inserted in order.

You must write an algorithm with **O(log n)** runtime complexity.

### Example 1:
#### **Input:**
```python
nums = [1, 3, 5, 6]
target = 5
```
#### **Output:**
```python
2
```

### Example 2:
#### **Input:**
```python
nums = [1, 3, 5, 6]
target = 2
```
#### **Output:**
```python
1
```

### Example 3:
#### **Input:**
```python
nums = [1, 3, 5, 6]
target = 7
```
#### **Output:**
```python
4
```
## Approach
We use **Binary Search** since the array is sorted, achieving an efficient **O(log n)** time complexity.

### Steps:
1. **Initialize Pointers:**
   - `left = 0`, `right = len(nums) - 1`
   - Set `ans = len(nums)` (default insertion index if `target` is greater than all elements)
2. **Perform Binary Search:**
   - Calculate `mid = left + (right - left) // 2`
   - If `nums[mid] >= target`, update `ans = mid` and move `right = mid - 1`
   - Otherwise, move `left = mid + 1`
3. **Return `ans` as the index where the target should be inserted.**

## Pseudo-code
```python
class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = len(nums)  # Default to last index if target is greater than all elements

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
```
## Complexity Analysis
- **Time Complexity:** `O(log n)` (Binary search efficiently halves the search space)
- **Space Complexity:** `O(1)` (Uses only a few extra variables)

## Edge Cases Considered
- **Target already exists in the array** → Returns its index
- **Target is smaller than all elements** → Inserts at index `0`
- **Target is greater than all elements** → Inserts at index `len(nums)`
- **Empty array case** → Returns `0`