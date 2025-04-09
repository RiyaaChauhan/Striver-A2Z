## 📑 Table of Contents

- [1. Missing Number](#1-missing-number)
- [2. Maximum consecutive ones](#2-maximum-consecutive-ones)

## 1. Missing Number

> Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.
### Examples

```python
Input: nums = [3, 0, 1]
Output: 2

Input: nums = [0, 1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

### Approaches

#### Brute Force (Sorting)
```python
def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)
```
- Time: O(n log n)  
- Space: O(1)

** Why it's not preferred:**  
→ Sorting modifies the input array (not ideal).  
→ Sorting takes extra time: O(n log n), which can be avoided.

####  Better (hash Set)
```python
def missingNumber(nums):
    num_set = set(nums)
    for i in range(len(nums) + 1):
        if i not in num_set:
            return i
```
- Time: O(n)  
- Space: O(n)

** Why it's not preferred:**  
→ Uses extra space for the set.  
→ We can solve it using constant space.

####  Optimal (Math Formula)
```python
def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
```
- ⏱ Time: O(n)  
- 💾 Space: O(1)

✅ **Best choice** — clean, simple, and most efficient.

### Test Cases

```python
assert missingNumber([3, 0, 1]) == 2
assert missingNumber([0, 1]) == 2
assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8
assert missingNumber([0]) == 1
```
---------------------------------------------------------------------
## 2. Maximum consecutive ones