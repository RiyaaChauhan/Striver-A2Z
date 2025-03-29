# 1. Search in Rotated Sorted Array

## **Problem Statement**
Given a sorted array `nums` that has been **rotated at an unknown pivot** (1 ≤ k < nums.length), return the index of a given `target` if it exists in the array. If the target is not found, return `-1`.

You **must** solve this problem in **O(log n)** time complexity.

### **Example 1**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### **Example 2**
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

### **Example 3**
```
Input: nums = [1], target = 0
Output: -1
```
## **Approach: Modified Binary Search**
Since the array is **rotated**, a standard binary search won’t work. Instead, we:
1. **Find the middle element** (`mid`).
2. **Determine the sorted half**:
   - If `nums[left] ≤ nums[mid]`, then the **left half** is sorted.
   - Otherwise, the **right half** is sorted.
3. **Check if the target lies in the sorted half**:
   - If yes, **search** in that half.
   - If not, **search** in the other half.
4. Continue until we **find the target** or return `-1`.

## **Implementation (Python)**
```python
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:  # Target is in the left half
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:  # Target is in the right half
                left = mid + 1
            else:
                right = mid - 1

    return -1  # Target not found
```

## **Complexity Analysis**
| Operation | Time Complexity | Space Complexity |
|-----------|---------------|----------------|
| Search | **O(log n)** (Binary Search) | **O(1)** |

---

## **Edge Cases Considered**
✅ **Target at rotation point**  
✅ **No rotation (already sorted array)**  
✅ **Array of size 1**  
✅ **Target not in array**  

---

## **Usage**
```python
nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))  # Output: 4

target = 3
print(search(nums, target))  # Output: -1
```
---
