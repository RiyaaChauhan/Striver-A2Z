## 🔧 PROBLEM BREAKDOWN: Partition List Around a Pivot

### ✅ Goal:
Move nodes `< x` to the front  
Keep **relative order**  
Do **not** create new nodes

---

### 💡 Step-by-Step Strategy (Two Dummy Nodes Technique):

We’ll use two lists:
- One for nodes `< x`
- One for nodes `>= x`

Then stitch them together at the end.

---

### ✨ Code Blueprint:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_head = ListNode(0)  # Dummy node for less-than-x
        after_head = ListNode(0)   # Dummy node for greater/equal-x

        before = before_head
        after = after_head

        current = head

        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next

        after.next = None  # Terminate the list
        before.next = after_head.next  # Connect before list with after list

        return before_head.next
```

---

### 🔁 Time Complexity:
- **O(n)**: One pass through the list

### 💾 Space:
- **O(1)**: Just re-linking nodes, no new ones

---

### 🎯 Test Case:
Try:
```python
# 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
```
You should get:
```python
# 1 -> 2 -> 2 -> 4 -> 3 -> 5
```