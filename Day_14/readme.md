## 📑 Table of Contents

- [1. Missing Number](#1-missing-number)
- [2. Maximum consecutive ones](#2-maximum-consecutive-ones)

## 1. Missing Number in Array

You are given an array `arr[]` of size `n`, containing `n` **distinct numbers** in the range `0` to `n`.  
This means **one number from the range [0, n] is missing** in the array.  
Your task is to **find the missing number**.

### Example

```
Input: arr = [3, 0, 1]
Output: 2

Input: arr = [0, 1]
Output: 2
```

## Brute Force Approach

### Intuition:
- For every number from `0` to `n`, check whether it is present in the array.

### Code:
```python
def missing_number_brute(arr):
    n = len(arr)
    for i in range(n + 1):
        if i not in arr:
            return i
```

### Time Complexity: `O(n^2)`  
(because of `in` operation inside a loop)

### Space Complexity: `O(1)`

### Why it fails:
- Very slow for large inputs due to repeated search in array.

## Better Approach (Using Hashing / Visited Array)

### Intuition:
- Create a boolean array of size `n+1` to mark visited numbers.

### Code:
```python
def missing_number_better(arr):
    n = len(arr)
    visited = [False] * (n + 1)
    for num in arr:
        visited[num] = True
    for i in range(n + 1):
        if not visited[i]:
            return i
```

### Time Complexity: `O(n)`  
### Space Complexity: `O(n)`

### Why not optimal:
- Extra space used for the visited array.

## Optimal Approach 1: Sum Formula

### Intuition:
- Use the formula of sum of first `n` natural numbers.
- Subtract the array’s actual sum from it to find the missing number.

### Code:
```python
def missing_number_sum(arr):
    n = len(arr)
    total = n * (n + 1) // 2
    return total - sum(arr)
```

### Time Complexity: `O(n)`  
### Space Complexity: `O(1)`

##  Optimal Approach 2: XOR Method

### Intuition:
- XOR all numbers from `0` to `n` and all elements of the array.
- The result will be the missing number.

### Code:
```python
def missing_number_xor(arr):
    n = len(arr)
    xor1 = 0
    xor2 = 0

    for i in range(n + 1):
        xor1 ^= i
    for num in arr:
        xor2 ^= num

    return xor1 ^ xor2
```

### Time Complexity: `O(n)`  
### Space Complexity: `O(1)`

##  Summary

| Approach           | Time Complexity | Space Complexity | Notes                   |
|--------------------|------------------|-------------------|--------------------------|
| Brute Force        | O(n²)            | O(1)              | Simple, not scalable     |
| Better (Hashing)   | O(n)             | O(n)              | Uses extra space         |
| Optimal (Sum)      | O(n)             | O(1)              | Fast, simple logic       |
| Optimal (XOR)      | O(n)             | O(1)              | Bit manipulation-based   |

-----------------------------------------------------------------------
## 2. Maximum consecutive ones