# 1. **Odd Even Linked List**
###  **Problem Summary**
You're given a singly linked list, and you need to:
- Group all nodes at **odd indices** together first,
- Then group all nodes at **even indices**,
- Maintain the **original relative order** within odd and even groups,
- Return the modified head of the list.

>  **Important**: Indexing starts at 1, i.e.,  
1st node → odd, 2nd node → even, 3rd node → odd, etc.

---

##  Constraints
- Do it in **O(n)** time.
- Use only **O(1)** extra space.

---

##  Example

**Input:** `1 → 2 → 3 → 4 → 5`  
**Output:** `1 → 3 → 5 → 2 → 4`  

---

##  Step 1: **Brute Force Explanation**
**Idea:**  
- Store nodes at *odd* positions in one list.  
- Store nodes at *even* positions in another.  
- Traverse the original list and separate based on index (starting from 1).  
- Combine both lists in the end.

**Time Complexity:** `O(N)`  
**Space Complexity:** `O(N)` (using extra lists)

---

##  Step 2: **Brute Force Code**:

```python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd_nodes = []
        even_nodes = []
        current = head
        index = 1

        while current:
            if index % 2 == 1:
                odd_nodes.append(current)
            else:
                even_nodes.append(current)
            current = current.next
            index += 1

        dummy = ListNode(0)
        tail = dummy

        for node in odd_nodes + even_nodes:
            tail.next = node
            tail = tail.next

        tail.next = None  # Important to terminate the list
        return dummy.next
```

---

> "But this uses extra space. Since we only need to rearrange pointers, we can do it **in-place** in `O(1)` space and `O(N)` time. Here’s the optimized version…"

---
###  Final Pro Tip:
**Any Linked List reordering problem?**  
→ **Think in terms of pointers first, not values.**  

---
##  Optimal Approach (In-place)
###  Intuition
We split the linked list into **two separate chains**:
- One for **odd-indexed** nodes
- One for **even-indexed** nodes

Then we **reconnect** the even list to the tail of the odd list.

---

###  Steps
1. If the list is empty or has only 1 or 2 nodes, return head directly.
2. Initialize two pointers:
   - `odd` starting at `head`
   - `even` starting at `head.next`
   - `evenHead` keeps reference to even list's head.
3. Traverse as long as both `odd` and `even` are valid and have a next:
   - `odd.next = even.next` → skip even node
   - Move `odd = odd.next`
   - `even.next = odd.next` → skip odd node
   - Move `even = even.next`
4. After the loop, connect `odd.next = evenHead`.

---

###  Code (Optimal – O(1) space, O(n) time)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even  # Save head of even list

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        # Join the two parts
        odd.next = evenHead
        return head
```

---
###  Complexity

| Time | Space |
|------|-------|
| O(n) | O(1)  |
---

##  Dry Run (Visual)

Input: `1 → 2 → 3 → 4 → 5`

- Initial:  
  odd = 1, even = 2, evenHead = 2

- Step 1:  
  odd.next = 3 → odd = 3  
  even.next = 4 → even = 4

- Step 2:  
  odd.next = 5 → odd = 5  
  even.next = None → even = None

Now:  
Odd list: `1 → 3 → 5`  
Even list: `2 → 4`  
Final: `1 → 3 → 5 → 2 → 4`

---

##  Notes for Interviews

- This is not about odd/even **values**, it's about **positions**.
- Make sure to keep a pointer to `evenHead`, else you'll lose the second part.
- Avoid extra data structures to meet space constraint.