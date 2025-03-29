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

------------------------------------------------------------------------------------------------------------
# 2. Occurance of number in sorted arr with duplicates
# Count Occurrences of a Target in a Sorted Array

## Problem Statement
Given a sorted array `arr[]` and a number `target`, find the number of occurrences of `target` in `arr[]`.

## Approach
Since the array is **sorted**, we can efficiently find the number of occurrences of `target` using **binary search** instead of iterating through the entire array. The idea is to:

1. Find the **first occurrence** of `target` in `arr[]`.
2. Find the **last occurrence** of `target` in `arr[]`.
3. Compute the count as:
   
   ```
   count = last index - first index + 1
   ```

## Implementation

### 1️⃣ Binary Search Approach (O(log n))
```python
# Function to find first occurrence
def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1  # Move left to find first occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first

# Function to find last occurrence
def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1  # Move right to find last occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last

# Function to count occurrences of target
def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0  # Target not found
    last = last_occurrence(arr, target)
    return last - first + 1

# Example Usage
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(count_occurrences(arr, target))  # Output: 3
```

### 2️⃣ Alternative Approach (Using `bisect` – O(log n))
Python’s `bisect` module provides an efficient way to find the leftmost and rightmost occurrences of an element.

```python
import bisect

def count_occurrences(arr, target):
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target)
    return right - left

# Example Usage
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(count_occurrences(arr, target))  # Output: 3
```

## Complexity Analysis
- **Binary Search Approach:** `O(log n)`
- **`bisect` Approach:** `O(log n)`
- **Naive Linear Search:** `O(n)`

## Summary
✅ **Efficient:** Uses binary search instead of iterating over the array.
✅ **Optimized:** Runs in `O(log n)` instead of `O(n)`.
✅ **Uses Sorted Property:** Leverages sorted order for fast searching.

🚀 **Recommended Approach:** Use **binary search** or `bisect` for optimal performance!

------------------------------------------------------------------------------------------------------------
# 3. Find the first or last occurance of given number
## **Problem Statement**  
Given a sorted array `nums` and a target value `target`, find the starting and ending position of `target` in the array.  
If `target` is not found, return `(-1, -1)`.  
You must write an algorithm with **O(log n)** runtime complexity.  

## **Approach**  
We use **Binary Search** to efficiently find the first and last occurrence of the target.  

1. **Find the Lower Bound (First Occurrence)**  
   - Perform a binary search to find the smallest index where `nums[i] >= target`.  

2. **Find the Upper Bound (Last Occurrence)**  
   - Perform a binary search to find the largest index where `nums[i] <= target`.  

3. **Edge Cases**  
   - If the target is not in `nums`, return `(-1, -1)`.  

## **Code Implementation**  

```python
class Solution:
    def searchRange(self, nums, target):
        lower = self.LowerBound(nums, target)
        if lower == -1 or nums[lower] != target:
            return (-1, -1)
        return (lower, self.UpperBound(nums, target))

    def UpperBound(self, arr, x):
        left, right = 0, len(arr) - 1
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def LowerBound(self, arr, x):
        left, right = 0, len(arr) - 1
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] >= x:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
```
## **Complexity Analysis**  
- **Time Complexity:** `O(log n)` (Binary search halves the search space each iteration)  
- **Space Complexity:** `O(1)` (Uses constant extra space)  

## **Example Walkthrough**  

### **Example 1:**  
#### **Input:**  
```python
nums = [5,7,7,8,8,10], target = 8
```
#### **Output:**  
```python
(3, 4)
```
#### **Explanation:**  
The first occurrence of `8` is at index **3**, and the last occurrence is at index **4**.  

### **Example 2:**  
#### **Input:**  
```python
nums = [5,7,7,8,8,10], target = 6
```
#### **Output:**  
```python
(-1, -1)
```
#### **Explanation:**  
The target `6` is not found in the array, so we return `(-1, -1)`.  

## **Edge Cases Considered**  
✔ Empty array `[]`  
✔ Target is smaller/larger than all elements  
✔ Single-element array  
✔ Target occurs multiple times  

---