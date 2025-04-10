# 01. Longest subarray with sum K (Positives)

### **Problem Statement**
Given an array of integers `nums` and an integer `k`, return the total number of **subarrays** whose sum equals to `k`.
A **subarray** is a contiguous part of an array (non-empty).

### **Brute Force Approach**
**Idea:**  
Check all possible subarrays and calculate their sum. If any subarray’s sum is equal to `k`, increment the count.

```python
def subarraySum(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            total = sum(nums[i:j+1])
            if total == k:
                count += 1
    return count
```

**Time Complexity:** O(n³) (because of the `sum()` inside nested loop)  
**Space Complexity:** O(1)

#### Why this fails:
Too slow for large arrays (e.g. 10^4 elements), will time out in most platforms.
### **Better Approach**
**Idea:**  
Use **prefix sum** technique.  
Instead of recalculating the sum every time, we keep track of the cumulative sum so far.

```python
def subarraySum(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    return count
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

#### Still not optimal:
Still too slow for large arrays – nested loop remains.

### **Optimal Approach (Using HashMap)**
**Idea (Prefix Sum + HashMap):**  
- Maintain a hashmap to store the frequency of prefix sums.
- For each element, calculate current prefix sum.
- Check if `prefix_sum - k` is already in hashmap. If yes, we found subarrays ending at current index with sum = k.
- Update hashmap with current prefix sum.

```python
def subarraySum(nums, k):
    from collections import defaultdict

    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1  # For the case when prefix itself = k

    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        count += prefix_sum_count[current_sum - k]
        prefix_sum_count[current_sum] += 1

    return count
```

### **Time & Space Complexity**
| Approach      | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| Brute Force   | O(n³)           | O(1)             |
| Better        | O(n²)           | O(1)             |
| Optimal       | O(n)            | O(n)             |

### **End Moment Summary (Approach in Brief)**
- Brute: Try all subarrays, sum manually – very slow.
- Better: Keep running sum inside inner loop – better but still nested.
- Optimal: Use prefix sum and hashmap to count matching sums on-the-go.