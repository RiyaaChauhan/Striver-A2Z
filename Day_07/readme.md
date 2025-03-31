# 1. Single element in sorted array
## Problem Statement
We are given a **sorted array** where every element appears **twice**, except for one element that appears **only once**. Our goal is to find this single unique element in **O(log n)** time and **O(1)** space.

## Example: 
- **Input**: `[1, 1, 2, 2, 3, 4, 4]`  
- **Output**: `3` (since `3` appears only once)

## Code Breakdown and Explanation 

```python
class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1  # Initialize two pointers
```
✅ **Initialization:**  
- `left = 0` (start of array)  
- `right = len(nums) - 1` (end of array)

```python
        while left < right:  # Continue until two pointers converge
            mid = left + (right - left) // 2  # Find the middle index
```
✅ **Binary Search Loop:**  
- Runs while `left < right`, meaning we haven't found the unique element yet.  
- `mid` is calculated to divide the search space.

```python
            # Ensure mid is even for pair checking
            if mid % 2 == 1:
                mid -= 1  
```
✅ **Adjusting `mid` to be even:**  
- Since pairs of elements occur at even indices, we **ensure `mid` is even**.  
- If `mid` is **odd**, we decrement it (`mid -= 1`).

```python
            if nums[mid] == nums[mid + 1]:
                left = mid + 2  # Move right to the next pair
            else:
                right = mid  # Move left
```
✅ **Checking for Pairs and Moving the Search Space:**  
- If `nums[mid] == nums[mid + 1]`:  
  - The **single element is in the right half**, so move `left = mid + 2`.  
- Else:  
  - The **single element is in the left half**, so move `right = mid`.

```python
        return nums[left]  # Return the single non-duplicate element
```
✅ **Final Return Statement:**  
- When `left == right`, this index contains the **unique element**.  

## Key Observations
1. **Why Binary Search?**  
   - A **linear scan (O(n))** would work, but the problem requires **O(log n)** time.  
   - **Binary search** helps efficiently narrow down the search space.

2. **Why Ensure `mid` is Even?**  
   - In a sorted array with **pairs**, elements appear at **even indices** first (`0, 2, 4, ...`).  
   - This guarantees correct pair checking.

3. **How Does the Approach Work?**  
   - Before the unique element, pairs follow the `(even, odd)` pattern.  
   - After the unique element, the pattern breaks, which helps us decide whether to move left or right.

## Complexity Analysis 
✅ **Time Complexity**: **O(log n)**  
- **Binary search** halves the search space at each step.  

✅ **Space Complexity**: **O(1)**  
- **No extra space** is used apart from the two pointers (`left` and `right`).

## Example Walkthrough
## Example 1:  
🔹 **Input**: `[1, 1, 2, 2, 3, 4, 4]`  
🔹 **Steps**:
| Left | Right | Mid | `nums[mid]` | `nums[mid + 1]` | Action |
|------|------|-----|------------|----------------|---------|
| 0 | 6 | 3 | 2 | 2 | Move `left = mid + 2 = 5` |
| 5 | 6 | 5 | 3 | 4 | Move `right = mid = 5` |
| 5 | 5 | - | 3 | - | Return `nums[left] = 3` |

🔹 **Output**: `3`

## Final Summary
✅ **Efficient O(log n) solution using Binary Search**  
✅ **No extra space required (O(1) space complexity)**  
✅ **Ensures `mid` is even to maintain the pair structure**  
✅ **Works optimally for large input sizes**  