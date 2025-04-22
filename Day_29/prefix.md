##  **Prefix Sum**

---
###  **What is Prefix Sum?**

The **Prefix Sum** (also called **cumulative sum**) of an array is a new array where each element at index `i` contains the sum of all elements from index `0` to `i` in the original array.

---

###  **Formula:**

For an array `arr` of length `n`, the prefix sum array `prefix` is defined as:

```
prefix[0] = arr[0]
prefix[i] = prefix[i-1] + arr[i]   for i > 0
```

---

###  **Why Use Prefix Sum?**

Prefix sums allow you to compute the **sum of any subarray in O(1)** time after an initial O(n) preprocessing.

---

###  **How to Construct Prefix Sum Array (Python):**

```python
def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix
```

---

###  **Example:**

```python
arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)
print(prefix)  # Output: [1, 3, 6, 10, 15]
```

---

###  **How to Find Subarray Sum from i to j:**

Once you have the prefix sum array, the sum from index `i` to `j` is:

```
If i == 0:
    sum = prefix[j]
Else:
    sum = prefix[j] - prefix[i - 1]
```

---

###  **Example Usage:**

```python
arr = [5, 2, 9, 1, 7]
prefix = prefix_sum(arr)

# Sum of elements from index 1 to 3 (2 + 9 + 1)
sum_1_to_3 = prefix[3] - prefix[0]
print(sum_1_to_3)  # Output: 12
```

---

##  **Prefix Sum for 2D Arrays (Matrix)**

To compute the sum of submatrices quickly, you can use a 2D prefix sum array.

```python
def compute_2D_prefix_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            top = prefix[i-1][j] if i > 0 else 0
            left = prefix[i][j-1] if j > 0 else 0
            top_left = prefix[i-1][j-1] if i > 0 and j > 0 else 0

            prefix[i][j] = matrix[i][j] + top + left - top_left
    return prefix
```

---

## **Common Interview Problems Using Prefix Sum:**

1. **Subarray Sum Equals K** (LeetCode 560)
2. **Range Sum Query** (LeetCode 303)
3. **Find Pivot Index** (LeetCode 724)
4. **Equilibrium Index**
5. **Maximum Subarray Sum of Fixed Size**

---

## **Tips and Tricks:**

- Prefix sum is best when you are given **multiple range sum queries**.
- Can be used with **binary search** for advanced problems.
- Useful for solving **sliding window** variants.
- Can be extended to **difference arrays** for range updates.

---

## Final Takeaways:

- **Prefix Sum reduces time complexity** for range sum problems.
- Use it after a **one-time O(n) preprocessing**.
- Applies to both **1D arrays** and **2D matrices**.
- Always be careful with **indexing**, especially for 0-based arrays.