### 🔁 **Problem 1: Reverse a String (Leetcode #344)**

#### 📝 Problem Statement:

Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array in-place with O(1) extra memory.

#### 🧠 Approach (Two Pointers):

* Place one pointer `left` at the beginning and `right` at the end.
* Swap the characters at `left` and `right`.
* Move `left++` and `right--` until they cross.

#### ✅ Code (Python):

```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

#### 📦 Example:

Input: `["h","e","l","l","o"]`
Output: `["o","l","l","e","h"]`

---

### 🔁 **Problem 4: Remove duplicates from sorted array**
### 🔁 Line: `nums[left] = nums[right]`

This line **overwrites the duplicate value at index `left + 1` with a new unique value from `right`**.

---

### 📦 Context:

You're working on the problem: **"Remove duplicates from a sorted array"**, and using two pointers:

* `left`: Points to the last unique element.
* `right`: Scans the array looking for the next unique element.

When `nums[right] != nums[left]`, it means you've found a new unique number.

---

### 💡 So, what does `nums[left] = nums[right]` do?

Let’s walk through a short example:

#### Input:

```python
nums = [1, 1, 2, 3, 3]
```

#### Steps:

* Initially: `left = 0`, `right = 1`
* `nums[1] == nums[0]`, so no action.
* `right = 2`, `nums[2] != nums[0]` → new unique value!

  * So increment `left → 1`, then do: `nums[1] = nums[2]` → now `nums = [1, 2, 2, 3, 3]`
* This continues...

By the end, the **first `left + 1` elements** in `nums` will be all the unique values.

---

### 🔁 **Problem 5: Remove Element**
### 💡 Refined Idea (Optimized Two-Pointer Approach):

* You don’t need to “send to end,” since order **doesn’t matter**.
* Instead, when you find an element equal to `val`, **replace it** with the **last valid element** from the array (pointed to by `right`).
* Then decrease `right` (since that’s now processed).
* Otherwise, move the `left` pointer forward.

---

### ✅ Dry Run:

Given: `nums = [3, 2, 2, 3], val = 3`

```
left = 0, right = 3

1. nums[0] == 3 → replace with nums[3] → nums = [3, 2, 2, 3] (but right now becomes 2)
2. left = 0 again, nums[0] == 3 → replace with nums[2] → nums = [2, 2, 2, 3]
3. left = 0, nums[0] == 2 → left++
4. left = 1, nums[1] == 2 → left++

Loop stops when left > right.
```

We end up with `nums = [2, 2, _, _]` and return 2.

---

### ✅ Code:

```python
class Solution:
    def removeElement(self, nums, val):
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
```

---
### ✅ Time complexity:
This is **O(n)** time and **O(1)** space — best for in-place operations.
---