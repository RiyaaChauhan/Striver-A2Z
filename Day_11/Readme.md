## 📑 Table of Contents

- [1. Remove Duplicates from Sorted Array](#1-remove-duplicates-from-sorted-array)
- [2. Left Rotate an Array by One Place](#2-left-rotate-an-array-by-one-place)
- [3. Left Rotate an Array by D Places](#3-left-rotate-an-array-by-d-places)
- [4. Move Zeros to End](#4-move-zeros-to-end)
- [5. Linear Search](#5-linear-search)
- [6. Find the Union of Two Arrays](#6-find-the-union-of-two-arrays)
- [7. Find Missing Number in an Array](#7-find-missing-number-in-an-array)
- [8. Maximum Consecutive Ones](#8-maximum-consecutive-ones)
- [9. Find the Number that Appears Once (Others Twice)](#9-find-the-number-that-appears-once-others-twice)
- [10. Longest Subarray with Given Sum K (Only Positives)](#10-longest-subarray-with-given-sum-k-only-positives)
- [11. Longest Subarray with Sum K (Positives + Negatives)](#11-longest-subarray-with-sum-k-positives--negatives)

# 1. Remove Duplicates from Sorted Array

## 🧩 Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the **duplicates in-place** such that each unique element appears only once. Return the number of unique elements `k`, and the first `k` elements of `nums` should hold the final result. You **must** do this with **O(1) extra memory**.

## 🔍 Constraints

- The array is sorted in non-decreasing order.
- Modifications must be done **in-place**.
- Extra memory is not allowed beyond O(1).

## 🧪 Example

**Input:**
```python
nums = [1, 1, 2, 2, 3, 4, 4]
```

**Output:**
```
k = 4
nums = [1, 2, 3, 4, _, _, _]
```

## 🧠 Approaches

### 1️⃣ Brute Force (Using Set)

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

### 3️⃣ Optimal (In-place Two Pointer)

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

## 💬 Step-by-Step Example (Optimal)

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
------------------------------------------------------------------------------------------------------

# 3. Left Rotate an Array by D Places
------------------------------------------------------------------------------------------------------

# 4. Move Zeros to End
------------------------------------------------------------------------------------------------------

# 5. Linear Search
------------------------------------------------------------------------------------------------------

# 6. Find the Union of Two Arrays
------------------------------------------------------------------------------------------------------

# 7. Find Missing Number in an Array
------------------------------------------------------------------------------------------------------

# 8. Maximum Consecutive Ones
------------------------------------------------------------------------------------------------------

# 9. Find the Number that Appears Once (Others Twice)
------------------------------------------------------------------------------------------------------

# 10. Longest Subarray with Given Sum K (Only Positives)
------------------------------------------------------------------------------------------------------

# 11. Longest Subarray with Sum K (Positives + Negatives)