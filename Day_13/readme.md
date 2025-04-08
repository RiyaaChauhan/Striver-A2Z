# 1.  Problem Statement
You are given two sorted arrays `a[]` and `b[]`, where each array may contain duplicate elements.  
Your task is to return the **union** of the two arrays in **sorted order**, **without duplicates**.

> Union: A set containing **distinct** elements that are present in **either** of the arrays.

## Example

```
Input:
a = [1, 2, 2, 3, 4]
b = [2, 2, 3, 5, 6]

Output:
[1, 2, 3, 4, 5, 6]
```

## Brute Force Approach

### Intuition:
- Combine both arrays.
- Use a set to remove duplicates.
- Sort the set and return.

### Code:
```python
def union_brute(a, b):
    union_set = set(a + b)
    return sorted(list(union_set))
```

### Time Complexity:
- `O((n + m) log(n + m))`

### Space Complexity:
- `O(n + m)` (for storing elements in a set)

###  Why this fails:
- You lose the advantage of **sorted input arrays**.
- Sorting is extra work.

##  Better Approach (Two Pointer + Set)

### Intuition:
- Traverse both arrays using two pointers.
- Add elements to a set to maintain uniqueness.
- Return the sorted set.

### Code:
```python
def union_better(a, b):
    i, j = 0, 0
    union_set = set()
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            union_set.add(a[i])
            i += 1
        elif b[j] < a[i]:
            union_set.add(b[j])
            j += 1
        else:
            union_set.add(a[i])
            i += 1
            j += 1
    while i < len(a):
        union_set.add(a[i])
        i += 1
    while j < len(b):
        union_set.add(b[j])
        j += 1
    return sorted(list(union_set))
```

### Time Complexity:
- `O(n + m + k log k)` (`k` = number of unique elements)

### Space Complexity:
- `O(n + m)`

### Why this still isn’t optimal:
- You still **sort at the end**, adding overhead.

## Optimal Approach (Two Pointer Merge Without Set)

### Intuition:
- Merge arrays like merge sort.
- Directly skip duplicates and build the result.

### Code:
```python
def union_optimal(a, b):
    i, j = 0, 0
    union = []
    while i < len(a) and j < len(b):
        if len(union) > 0 and union[-1] == a[i]:
            i += 1
            continue
        if len(union) > 0 and union[-1] == b[j]:
            j += 1
            continue
        if a[i] < b[j]:
            union.append(a[i])
            i += 1
        elif a[i] > b[j]:
            union.append(b[j])
            j += 1
        else:
            union.append(a[i])
            i += 1
            j += 1
    while i < len(a):
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1
    while j < len(b):
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1
    return union
```

### Time Complexity:
- `O(n + m)`

### Space Complexity:
- `O(1)` extra (result list only)

## Time & Space Complexity

| Approach       | Time Complexity     | Space Complexity  |
|----------------|---------------------|-------------------|
| Brute Force    | O((n + m) log(n + m)) | O(n + m) for set  |
| Better         | O(n + m + log(n + m)) | O(n + m) for set  |
| Optimal        | O(n + m)             | O(1) extra (excluding result) |