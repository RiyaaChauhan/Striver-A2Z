# 1. BS to find X in sorted array
## Overview  
This function implements the **Binary Search** algorithm to find the index of a given `target` in a sorted array `nums`. If the target is not found, it returns `-1`.  

## Function Signature  
```python
def search(self, nums: List[int], target: int) -> int:
```  

### **Returns**  
- (int): The index of `target` in `nums` if found, otherwise `-1`.  

## Example Usage  

```python
solution = Solution()
print(solution.search([1, 2, 3, 4, 5], 3))  # Output: 2
print(solution.search([10, 20, 30, 40], 25))  # Output: -1
```

### **Additional Examples**  
| Input | Output | Explanation |
|--------|--------|--------------|
| `[1, 3, 5, 7, 9], 7` | `3` | Element `7` found at index `3`. |
| `[2, 4, 6, 8], 5` | `-1` | Element `5` is not present in the array. |

## **Algorithm Explanation**  

1. **Initialize Pointers:**  
   - `low = 0` (starting index)  
   - `high = len(nums) - 1` (last index)  

2. **Binary Search Logic:**  
   - Compute `mid = low + (high - low) // 2`.  
   - If `nums[mid] == target`, return `mid` (found the element).  
   - If `nums[mid] < target`, search in the **right half** (`low = mid + 1`).  
   - Else, search in the **left half** (`high = mid - 1`).  

3. **Repeat until `low > high`**:  
   - If `target` is not found, return `-1`.  

## **Complexity Analysis**  
- **Time Complexity:** **O(log n)** (Binary search reduces search space by half in each iteration).  
- **Space Complexity:** **O(1)** (Uses constant space, no extra data structures).  

## **Why Use Binary Search?**  
- **Efficient for Large Data**: Faster than **O(n)** linear search.  
- **Optimal for Sorted Arrays**: Takes advantage of sorted order.  
- **Logarithmic Growth**: Performs well even with large inputs.  

### **Edge Cases Considered**  
✅ Target at the beginning (`nums[0]`).  
✅ Target at the end (`nums[-1]`).  
✅ Target in the middle.  
✅ Target not present in `nums`.  
✅ Array with only one element.  
✅ Empty array (`nums = []`).  

## **Alternative Approaches**  
- **Linear Search**: O(n) time complexity, but inefficient for large datasets.  
- **Recursive Binary Search**: Uses recursion but has higher memory usage (`O(log n)` call stack).  
-----------------------------------------------------------------------------------------------

# 2. Floor Finder (Binary Search) - Lower Bound

## Problem Statement  
Find the **floor** of `x` in a **sorted array** `arr`. The **floor** is the largest element ≤ `x`. Return `-1` if no such element exists.  

## Input & Output  
- **Input**: `arr` (sorted list of integers), `x` (integer)  
- **Output**: Index of the floor value, or `-1` if no floor exists  

## Examples  
- **Example 1**: `findFloor([1, 2, 8, 10, 10, 12], 5) → 1` (Floor: `2`)  
- **Example 2**: `findFloor([2, 3, 4, 10, 40], 5) → 2` (Floor: `4`)  
- **Example 3**: `findFloor([1, 1, 1, 1], 0) → -1` (No floor exists)  
- **Example 4**: `findFloor([1, 2, 3, 4, 5], 3) → 2` (Floor: `3`)  

## Pseudo Code  
```
function findFloor(arr, x):
    left = 0, right = length(arr) - 1, ans = -1

    while left ≤ right:
        mid = left + (right - left) // 2
        if arr[mid] > x:
            ans = mid   // Store possible floor index
            right = mid - 1
              // Move right to find a closer match
        else:
            left = mid + 1
             // Move left to find smaller values

    return ans
```

## Explanation  
1. **Initialize**: `left = 0`, `right = n-1`, `ans = -1` (stores index of floor).  
2. **Binary Search**:  
   - Calculate `mid`.  
   - If `arr[mid] ≤ x`, update `ans` and move right (`left = mid + 1`).  
   - Else, move left (`right = mid - 1`).  
3. **Return `ans`** (floor index) or `-1` if no floor exists.  

## Why Binary Search?  
- **Efficient**: O(log n) vs. O(n) in linear search.  
- **Sorted Input Utilization**: Eliminates unnecessary comparisons.  
- **Optimized Search**: Narrows search space in each step.  

---  
🚀 **Binary search ensures finding the floor efficiently, making it ideal for large datasets!**
----------------------------------------------------------------------
# 3. Upper Bound (Last occurance) - Floor in Sorted Array
Here's the **README.md** for your implementation:

---

# Find Floor and Ceiling in an Unsorted Array
## Problem Statement
Given an **unsorted** array `arr[]` of integers and an integer `x`, find the **floor** and **ceiling** of `x` in `arr[]`.

- **Floor** of `x`: The largest element in `arr[]` that is **≤ x**. If no such element exists, return `-1`.
- **Ceiling** of `x`: The smallest element in `arr[]` that is **≥ x**. If no such element exists, return `-1`.

## Example
### **Input**
```python
arr = [3, 8, 4, 6, 7, 10]
x = 5
```

### **Output**
```python
[4, 6]
```

### **Explanation**
- The largest number ≤ `5` is **4** (floor).
- The smallest number ≥ `5` is **6** (ceil).

## Approach
Since the array is **unsorted**, we cannot use binary search. Instead, we iterate through the array once:

1. Initialize `floor = -1` and `ceil = -1`.
2. Iterate through each element in `arr[]`:
   - If `arr[i] ≤ x`, update `floor = max(floor, arr[i])`.
   - If `arr[i] ≥ x`, update `ceil = min(ceil, arr[i])`.
3. Return `[floor, ceil]`.

## Code Implementation

```python
class Solution:
    def getFloorAndCeil(self, arr, x):
        floor, ceil = -1, -1  # Default values if no floor/ceil is found
        
        for num in arr:
            if num <= x:  # Check for floor condition
                floor = max(floor, num)
            if num >= x:  # Check for ceil condition
                ceil = min(ceil, num) if ceil != -1 else num
        
        return [floor, ceil]
```

## Complexity Analysis
- **Time Complexity:** `O(n)`, as we iterate through the array once.
- **Space Complexity:** `O(1)`, as we use only a few extra variables.

## Edge Cases Considered
| Case | Example Input | Expected Output |
|------|--------------|----------------|
| **Exact Match Found** | `arr = [3, 8, 4, 6, 7, 10], x = 6` | `[6, 6]` |
| **`x` is Smaller than the Smallest Element** | `arr = [3, 8, 4, 6, 7, 10], x = 2` | `[-1, 3]` |
| **`x` is Larger than the Largest Element** | `arr = [3, 8, 4, 6, 7, 10], x = 12` | `[10, -1]` |
| **All Elements are the Same** | `arr = [5, 5, 5, 5], x = 5` | `[5, 5]` |
| **Single Element Array** | `arr = [5], x = 3` | `[-1, 5]` |

## Usage Example
```python
sol = Solution()
arr = [3, 8, 4, 6, 7, 10]

print(sol.getFloorAndCeil(arr, 5))  # Output: [4, 6]
print(sol.getFloorAndCeil(arr, 10)) # Output: [10, 10]
print(sol.getFloorAndCeil(arr, 2))  # Output: [-1, 3]
print(sol.getFloorAndCeil(arr, 12)) # Output: [10, -1]
```