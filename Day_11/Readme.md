## 📑 Table of Contents

- [1. Remove Duplicates from Sorted Array](#1-remove-duplicates-from-sorted-array)
- [2. Left Rotate an Array by One Place](#2-left-rotate-an-array-by-one-place)
- [3. Left Rotate an Array by D Places](#3-left-rotate-an-array-by-d-places)
- [4. Move Zeros to End](#4-move-zeros-to-end)

# 1. Remove Duplicates from Sorted Array

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the **duplicates in-place** such that each unique element appears only once. Return the number of unique elements `k`, and the first `k` elements of `nums` should hold the final result. You **must** do this with **O(1) extra memory**.

## Constraints

- The array is sorted in non-decreasing order.
- Modifications must be done **in-place**.
- Extra memory is not allowed beyond O(1).

## Example

**Input:**
```python
nums = [1, 1, 2, 2, 3, 4, 4]
```

**Output:**
```
k = 4
nums = [1, 2, 3, 4, _, _, _]
```

## Approaches

### 1 Brute Force (Using Set)

**Idea:**  
Use a `set` to collect unique elements, sort it, and copy back.

```python
class Solution:
    def removeDuplicates(self, nums):
        unique = list(set(nums))
        unique.sort()
        
        for i in range(len(unique)):
            nums[i] = unique[i]
        
        return len(unique)
```

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)  
**Drawback:** ❌ Not in-place

### 3️ Optimal (In-place Two Pointer)

**Idea:**  
Use two pointers to overwrite duplicates while iterating.

```python
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1) ✅  
**Advantage:** ✔️ In-place, Efficient

## Step-by-Step Example (Optimal)

```python
Input: nums = [1, 1, 2, 3, 3]

i = 0 (last unique index)

j = 1 → nums[1] == nums[0] → skip  
j = 2 → nums[2] != nums[0] → i=1, nums[1]=2  
j = 3 → nums[3] != nums[1] → i=2, nums[2]=3  
j = 4 → nums[4] == nums[2] → skip

Final array: [1, 2, 3, _, _]
Return: 3
```
------------------------------------------------------------------------------------------------------
# 2. Left Rotate an Array by One Place
### Problem Statement
Given an array `arr[]` of size `N`, **left rotate** the array by **one position** in **place**.

### 1. Brute Force Approach (Using Extra Space)
#### Idea:
- Store the first element separately.
- Shift all elements to the left.
- Place the first element at the last index.

#### Code:
```python
def leftRotateByOne(arr):
    n = len(arr)
    temp = arr[0]  # Store first element
    for i in range(1, n):
        arr[i - 1] = arr[i]  # Shift left
    arr[-1] = temp  # Place first element at the end
    return arr
```
#### Complexity Analysis:
- **Time Complexity:** `O(N)`  
- **Space Complexity:** `O(1)`, as we use only one temp variable.

### 2. Optimized Approach (Without Extra Space)
This approach is already optimal as it performs the shifting in-place.

#### Alternative Pythonic Way (Using Slicing):
```python
def leftRotateByOne(arr):
    return arr[1:] + arr[:1]  # Rotate using slicing
```
#### Complexity Analysis:
- **Time Complexity:** `O(N)`  
- **Space Complexity:** `O(1)`

### Edge Cases to Consider
✔ **Single element array** → `[5]` should remain `[5]`  
✔ **Already sorted array** → `[1, 2, 3] → [2, 3, 1]`  
✔ **Array with duplicate values** → `[7, 7, 7, 7] → [7, 7, 7, 7]`  
✔ **Large input sizes** should still run efficiently.  

### Final Thoughts
- The **shifting method** is optimal and runs in **O(N) time**.  
- The **slicing method** is more Pythonic but still **O(N)**.  
- We ensure **in-place rotation** with only `O(1)` extra space.  
------------------------------------------------------------------------------------------------------

# 3. Left Rotate an Array by D Places
### Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Constraints

- `1 <= nums.length <= 10⁵`
- `-2³¹ <= nums[i] <= 2³¹ - 1`
- `0 <= k <= 10⁵`
### 🔍 Approach

####  Optimal Approach (Using Reverse)

To rotate the array to the right by `k` steps:
1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the rest of the array from index `k` to end.

This works in-place and avoids extra space.

### Code

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # to handle cases where k > n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
```
### Time and Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

### Examples

#### Example 1:
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
Step 1: Reverse entire array: [7,6,5,4,3,2,1]  
Step 2: Reverse first k=3: [5,6,7,4,3,2,1]  
Step 3: Reverse remaining: [5,6,7,1,2,3,4]
```

#### Example 2:
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
After 2 rotations, the last two elements move to the front.
```
------------------------------------------------------------------------------------------------------

# 4. Move Zeros to End