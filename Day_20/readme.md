# Sort 0s, 1s, and 2s (Dutch National Flag Problem)

Given an array consisting of only `0s`, `1s`, and `2s`, the task is to sort the array in-place **without using any inbuilt sort functions**, ideally in **a single pass** and **constant space**.

---

## Problem Statement

Sort an array of 0s, 1s, and 2s such that all 0s come first, followed by all 1s, then all 2s.

> 💡 Expected: **O(N)** time and **O(1)** space.

---

## Examples

```python
Input:  [0, 2, 1, 2, 0, 1]  
Output: [0, 0, 1, 1, 2, 2]
```

---

## Approaches

###  Brute Force Approach (Using Built-in Sort)

#### Algorithm:
- Simply sort the array using a sorting algorithm.

### Python Code:
```python
def sortArrayBruteForce(arr):
    arr.sort()  # Using Python's built-in Timsort (O(N log N))
```

 ### Why Brute Force is Not Preferred


 1. **Time Complexity: O(N log N)**
 2. **Misses the Opportunity to Optimize**
 3. **Doesn’t Follow the Problem Constraint**

### Better Approach (Counting Sort)

#### Algorithm:
1. Count the number of 0s, 1s, and 2s.
2. Overwrite the array accordingly.

#### Steps:
```python
count_0 = count_1 = count_2 = 0
for num in arr:
    if num == 0:
        count_0 += 1
    elif num == 1:
        count_1 += 1
    else:
        count_2 += 1

arr[:count_0] = [0] * count_0
arr[count_0:count_0+count_1] = [1] * count_1
arr[count_0+count_1:] = [2] * count_2
```

#### Time Complexity:
- `O(N)` (two passes)

#### Space Complexity:
- `O(1)`

---

### Optimal Approach (Dutch National Flag Algorithm)

#### 🔧 Algorithm:
Use three pointers:
- `low` for 0s
- `mid` for current index
- `high` for 2s

#### Steps:
```python
def sortArray(arr):
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
```

#### Example:
```python
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
print(arr)  # Output: [0, 0, 1, 1, 2, 2]
```

#### ⏱Time Complexity:
- `O(N)` (single traversal)

#### Space Complexity:
- `O(1)`

---

## Time and Space Complexity Table

| Approach                  | Time Complexity | Space Complexity |
|---------------------------|----------------|------------------|
| Brute Force               | O(N log N)     | O(1) or O(N)     |
| Counting (Better)         | O(N)           | O(1)             |
| Dutch National Flag (Best)| O(N)           | O(1)             |