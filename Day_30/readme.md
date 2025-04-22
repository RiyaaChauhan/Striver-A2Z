# 1. **"Odd Even Linked List"**
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

##  Brute Force (Not recommended but good for understanding)

###  Idea
1. Traverse list and **store nodes in a list or two separate lists**:
   - One for odd indices, one for even indices.
2. Reconnect the nodes at the end.

###  Cons:
- Uses **O(n)** extra space.
- Breaks in-place constraint.
---

###  code:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd_nodes = []
        even_nodes = []

        index = 1
        current = head

        # Separate nodes into odd and even indexed
        while current:
            if index % 2 == 1:
                odd_nodes.append(current)
            else:
                even_nodes.append(current)
            current = current.next
            index += 1

        # Reconnect the odd nodes
        for i in range(len(odd_nodes) - 1):
            odd_nodes[i].next = odd_nodes[i + 1]

        # Reconnect the even nodes
        for i in range(len(even_nodes) - 1):
            even_nodes[i].next = even_nodes[i + 1]

        # Connect last odd node to head of even list
        if odd_nodes:
            odd_nodes[-1].next = even_nodes[0] if even_nodes else None

        # Last even node should point to None
        if even_nodes:
            even_nodes[-1].next = None

        return odd_nodes[0]
```

###  Key Points:
- This approach stores odd and even nodes in two separate Python lists.
- Then reconnects all the odd nodes, followed by the even ones.
- **Extra space complexity: O(n)** due to the additional lists.
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