### 🔁 **Problem 1: Move 0 to end**
Great thought process! You’re on the right track with tracking the non-zero elements. Let me refine your idea into a classic two-pointer approach:

### ✅ Optimized Two-Pointer Strategy:

* Initialize a pointer `j = 0` → This will always point to the position where the **next non-zero** element should go.
* Iterate through the array using pointer `i` from 0 to n-1:

  * If `nums[i] != 0`, we **place `nums[i]` at `nums[j]`**, and increment `j`.
* After the loop, **from index `j` to end**, fill the rest with `0`s.

This approach keeps the relative order and works in-place with **O(n)** time and **O(1)** space.

---

### 💡 Python Code:

```python
class Solution:
    def moveZeroes(self, nums):
        j = 0  # position to place the next non-zero element

        # First pass: move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Second pass: fill the rest with zeroes
        while j < len(nums):
            nums[j] = 0
            j += 1
```