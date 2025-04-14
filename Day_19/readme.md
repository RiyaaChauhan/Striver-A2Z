## Problem Statement

You are given:
- An array of integers `nums`
- An integer `target`

Your task is to **return the indices of the two numbers in the array** such that they **add up to the target**.

**Constraints:**
- Each input will have **exactly one solution**
- You **may not use the same element twice**
- The result can be returned **in any order**

## Example

### Example 1:
```python
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```
**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`

## Approaches

### Brute Force Approach

Check every pair of elements to see if they sum up to the target.

#### Logic:
- For each index `i`, loop through all `j > i`
- If `nums[i] + nums[j] == target`, return `[i, j]`

#### Code:
```python
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

#### Time Complexity: `O(n^2)`
#### Space Complexity: `O(1)`

### Why Brute Force Fails

- Inefficient for large inputs
- Double loop results in quadratic time complexity

### Optimal Approach (Using Hash Map)

Use a dictionary to store previously seen numbers and their indices.

#### Logic:
- Loop through the array
- For each `num`, calculate `complement = target - num`
- If `complement` is already in the dictionary, return its index and the current index
- Otherwise, store `num` with its index in the dictionary

#### Code:
```python
def twoSum(nums, target):
    num_map = {}  # stores num: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
```

## Time and Space Complexity

| Complexity | Description |
|------------|-------------|
| **Time**   | `O(n)` — Single pass through the list |
| **Space**  | `O(n)` — Hash map for storing seen numbers |

## Summary

| Approach       | Time   | Space  | Use When                     |
|----------------|--------|--------|------------------------------|
| Brute Force    | O(n²)  | O(1)   | For small input sizes        |
| Optimal (Map)  | O(n)   | O(n)   | For efficient real-world use |