###  Problem Summary:
You're given two non-empty linked lists representing two non-negative integers. Each node contains a single digit, and digits are stored in **reverse order**. You need to add the two numbers and return the result as a linked list.

---
Sure! Here's a **clean and clear pseudocode** (or approach) for the **"Add Two Numbers"** problem using linked lists:

---

### ✅ **Problem Summary**  
You are given two non-empty linked lists `l1` and `l2` representing two non-negative integers. The digits are stored in **reverse order** (least significant digit first). Add the two numbers and return the sum as a linked list.

---

###  **Approach / Pseudocode**

```
1. Initialize a dummy head node (dummy) to help build the result list
2. Initialize a pointer (cur) to dummy
3. Initialize a carry variable = 0

4. While l1 is not null OR l2 is not null OR carry is not 0:
    a. If l1 is not null, set v1 = l1.val, else v1 = 0
    b. If l2 is not null, set v2 = l2.val, else v2 = 0

    c. total = v1 + v2 + carry
    d. carry = total // 10         (integer division to get carry)
    e. digit = total % 10          (remainder is the new digit)

    f. Create a new node with value = digit and link it to cur.next
    g. Move cur to cur.next

    h. Move l1 and l2 to their next nodes if they exist

5. Return dummy.next (skipping the dummy head node)
```

---

###  Example:
If `l1 = [2,4,3]` and `l2 = [5,6,4]`  
That means:  
`342 + 465 = 807` → Output should be `[7,0,8]`

The algorithm goes:
```
2+5 = 7 → carry=0 → append 7
4+6 = 10 → carry=1 → append 0
3+4+1 = 8 → carry=0 → append 8
```

Final list = `7 -> 0 -> 8`

---

###  Code:

```python
# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Dummy node to simplify edge cases
        dummy = ListNode()
        current = dummy
        carry = 0

        # Traverse both lists until all digits and carry are processed
        while l1 or l2 or carry:
            # Extract current values from each list or 0 if None
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate total sum and carry
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            # Create a new node with the digit and attach to the result list
            current.next = ListNode(digit)

            # Move current pointer and input list pointers forward
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the next of dummy since dummy is a placeholder
        return dummy.next
```

---

###  Explanation (Line-by-Line Notes):

- `dummy = ListNode()`:  
  Acts as a placeholder to start the result linked list. Helps avoid special cases when adding the first node.

- `current = dummy`:  
  This pointer will be used to build the result list by appending new nodes.

- `carry = 0`:  
  Keeps track of the carry from the sum of two digits (just like addition on paper).

- `while l1 or l2 or carry`:  
  Continue the loop if any list still has nodes or if there's a remaining carry to add.

- `v1 = l1.val if l1 else 0`:  
  Get the value from `l1` if it exists; otherwise, treat it as 0.

- `v2 = l2.val if l2 else 0`:  
  Same as above for `l2`.

- `total = v1 + v2 + carry`:  
  Add values and any carry from the previous step.

- `carry = total // 10`:  
  If the result is ≥ 10, set carry for the next iteration.

- `digit = total % 10`:  
  Keep only the unit digit to store in the current node.

- `current.next = ListNode(digit)`:  
  Create a new node with the digit and attach it to the result list.

- `current = current.next`:  
  Move forward to build the next node.

- `l1 = l1.next if l1 else None`, `l2 = l2.next if l2 else None`:  
  Move the input list pointers forward.

- `return dummy.next`:  
  The final result starts after the dummy node.

---

###  Example:

**Input:**
- l1 = [2, 4, 3] (represents 342)
- l2 = [5, 6, 4] (represents 465)

**Process:**
```
2 + 5 = 7 -> [7]
4 + 6 = 10 -> [0], carry = 1
3 + 4 + 1 = 8 -> [8]
```

**Output:**
- [7, 0, 8] (represents 807)

---

### 💡 Tips for Interviews:

- Always ask if the digits are stored in **reverse** or **forward** order.
- Handle **carry** carefully.
- Use a **dummy node** to simplify edge cases.
- Test with **unequal length lists** and carry-over at the end (e.g., [9,9] + [1] = [0,0,1]).