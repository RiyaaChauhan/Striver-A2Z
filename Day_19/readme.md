## Problem Statement
You are given:
- An array of integers `nums`
- An integer `target`

Your task is to **return the indices of the two numbers in the array** such that they **add up to the target**.

**Constraints:**
- Each input will have **exactly one solution**
- You **may not use the same element twice**
- The result can be returned **in any order**

### Example 1:
```python
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```
**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`

### ✅ Variant 1:
Return **"YES"** if **any two distinct numbers** in the array sum up to the target. Otherwise, return **"NO"**.

### ✅ Variant 2:
Return the **indices** `[i, j]` of the two numbers such that `arr[i] + arr[j] == target`. If no such pair exists, return `[-1, -1]`.

> ⚠️ Note: You may **not** use the same element twice.

---
## Approaches

### 1. Brute Force (Naive)
- Time Complexity: **O(N²)**
- Space Complexity: **O(1)**
- Compare all possible pairs.

```python
def two_sum_brute_variant1(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return "YES"
    return "NO"

def two_sum_brute_variant2(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]
```

---

### 2. Better Approach (Using HashMap)
- Time Complexity: **O(N)**
- Space Complexity: **O(N)**
- Use a set or dictionary to store visited elements.

```python
def two_sum_better_variant1(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return "YES"
        seen.add(num)
    return "NO"

def two_sum_better_variant2(arr, target):
    index_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i
    return [-1, -1]
```

---

### 3. Optimal Approach (Two Pointers - Requires Sorting)
- Time Complexity: **O(N log N)** (due to sorting)
- Space Complexity: **O(1)** (if original indices not needed)

```python
def two_sum_optimal_variant1(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return "YES"
        elif s < target:
            left += 1
        else:
            right -= 1
    return "NO"
```

---

## Test Cases

```python
assert two_sum_brute_variant1([2, 6, 5, 8, 11], 14) == "YES"
assert two_sum_brute_variant2([2, 6, 5, 8, 11], 14) == [1, 3]

assert two_sum_better_variant1([2, 6, 5, 8, 11], 15) == "NO"
assert two_sum_better_variant2([2, 6, 5, 8, 11], 15) == [-1, -1]
```

## Time and Space Complexities

| **Approach**           | **Variant** | **Time Complexity** | **Space Complexity** | **Explanation**                                                                 |
|------------------------|-------------|----------------------|-----------------------|---------------------------------------------------------------------------------|
| **1. Brute Force**     | 1 & 2       | `O(N^2)`             | `O(1)`                | Checks all pairs using two nested loops.                                        |
| **2. Better (HashMap)**| 1           | `O(N)`               | `O(N)`                | Stores visited elements in a set.                                               |
|                        | 2           | `O(N)`               | `O(N)`                | Uses a dictionary to track index of each element.                               |
| **3. Optimal (2 Pointer)** | 1       | `O(N log N)`         | `O(1)`                | Sorts the array, then uses two pointers. Only valid for **Variant 1**.          |

---

## Notes:

- For **Variant 2 (returning indices)**, the **Optimal approach is not applicable** without extra data structures, because sorting the array will lose the original indices unless you store them.
- The **Brute Force** approach is simplest but inefficient for large inputs.
- The **Better** approach is best for both variants in terms of performance and ease.