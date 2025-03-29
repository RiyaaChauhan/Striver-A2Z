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

## **Edge Cases Considered**
✅ **Target at rotation point**  
✅ **No rotation (already sorted array)**  
✅ **Array of size 1**  
✅ **Target not in array**  

## **Usage**
```python
nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))  # Output: 4

target = 3
print(search(nums, target))  # Output: -1
```
---

# 2. **Search in Rotated Sorted Array with Duplicates**  

## **Problem Statement**  
You are given an integer array `nums` sorted in ascending order but **possibly rotated** at an unknown pivot. The array may also contain **duplicate values**.  

Your task is to find if a given target exists in the array. If found, return `True`, otherwise return `False`.  

### **Example 1**  
#### **Input:**  
```python
nums = [1, 0, 1, 1, 1]
target = 0
```
#### **Output:**  
```python
True
```

### **Example 2**  
#### **Input:**  
```python
nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
```
#### **Output:**  
```python
False
```
## **Constraints**  
- `1 <= nums.length <= 5000`  
- `-10^4 <= nums[i], target <= 10^4`  
- The array is **sorted but rotated** at an unknown pivot.  
- **Duplicates are allowed** in the array.  

## **Approach**  
We use a **modified binary search** to achieve an **O(log n)** average time complexity. The key observations:  

1. **Duplicates can affect binary search**  
   - If `nums[low] == nums[mid] == nums[high]`, we skip duplicates by doing `low += 1` and `high -= 1`.  

2. **Identifying the sorted half:**  
   - If `nums[low] <= nums[mid]`, the **left half is sorted**.  
   - If `nums[mid] <= nums[high]`, the **right half is sorted**.  

3. **Binary search logic:**  
   - If the target lies in the sorted half, search there.  
   - Otherwise, search in the unsorted half.  

## **Optimized Solution**  
```python
class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True  # Found target
            
            # Handle duplicates
            while low < mid and nums[low] == nums[mid]:
                low += 1
            while high > mid and nums[high] == nums[mid]:
                high -= 1

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # Right half is sorted
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
```
## **Complexity Analysis**  
- **Best case:** `O(1)` (if `target` is found quickly).  
- **Average case:** `O(log n)` (binary search).  
- **Worst case:** `O(n)` (if many duplicates force linear search).  

## **Edge Cases Considered**  
✅ Array contains **all duplicates except one unique value**.  
✅ **Target is at the pivot** position.  
✅ **Array is not rotated at all**.  
✅ **Smallest possible input** (`nums = [1]`).  