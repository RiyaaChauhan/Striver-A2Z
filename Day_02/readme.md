# 1. BB to find X in sorted array
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

## Problem Statement
Given a sorted array `arr[]` and an integer `x`, find the index (0-based) of the largest element in `arr[]` that is **less than or equal to `x`**. This element is called the **floor of `x`**. If such an element does not exist, return `-1`.

### Constraints:
- The input array is sorted in non-decreasing order.
- If multiple occurrences of the floor exist, return the **index of the last occurrence**.
- If no element in the array is less than or equal to `x`, return `-1`.

## Example

### Example 1
**Input:**  
```text
arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
```
**Output:**  
```text
1
```
**Explanation:**  
The largest element ≤ `5` is `2`, which is at index `1`.

### Example 2
**Input:**  
```text
arr = [3, 4, 7, 7, 8, 10]
x = 7
```
**Output:**  
```text
3
```
**Explanation:**  
The last occurrence of `7` is at index `3`, so we return `3`.

## Approach
We use **Binary Search** to find the largest element ≤ `x` efficiently:
1. Initialize `left = 0` and `right = len(arr) - 1`.
2. Maintain a variable `ans = -1` to store the index of the floor.
3. Use binary search:
   - Find the middle index `mid`.
   - If `arr[mid] ≤ x`, update `ans = mid` (as a potential answer) and move **right** to find a later occurrence.
   - If `arr[mid] > x`, move **left**.
4. Return `ans`.

## Pseudo Code
```
function findFloor(arr, x):
    left = 0
    right = length(arr) - 1
    ans = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= x:
            ans = mid  // Potential floor found
            left = mid + 1  // Move right to find last occurrence
        else:
            right = mid - 1  // Move left
    
    return ans
```

## Implementation (Python)
```python
def find_floor(arr, x):
    left, right = 0, len(arr) - 1
    ans = -1  # Default answer if no floor is found

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] <= x:
            ans = mid  # Update answer, move right for last occurrence
            left = mid + 1
        else:
            right = mid - 1  # Move left

    return ans
```

## Complexity Analysis
- **Time Complexity:** `O(log N)` (Binary search reduces search space by half in each iteration)
- **Space Complexity:** `O(1)` (Uses only constant extra space)

## Edge Cases Considered
- **x is smaller than all elements** → Return `-1`.
- **x is larger than all elements** → Return the last index.
- **x is present multiple times** → Return the last occurrence.
- **x is exactly equal to an element** → Return its last occurrence.
- **Single element array** → Handle cases where `x` is greater, smaller, or equal.

-----------------------------------------------------------------------------------------------------------------------------------