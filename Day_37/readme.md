# 1. Reverse LinkedList in groups of given size K
### Step-by-Step Explanation:
✅ **1. `reverse(start, end)` helper function**:
- We create a function to **reverse a part of the linked list**.
- It starts from `start` node and stops *just before* `end`.
- It returns the **new head** of the reversed portion.

```python
def reverse(start, end):
    prev = None
    curr = start
    while curr != end:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

---
✅ **2. Dummy Node**:
- We create a dummy node pointing to head (`dummy.next = head`).
- It helps in easily handling **edge cases**, especially if head changes after reversal.

```python
dummy = ListNode(0)
dummy.next = head
group_prev = dummy
```
---
✅ **3. Main While Loop**:
- We repeat the process **group by group** (k nodes at a time).

```python
while True:
    kth = group_prev
    for _ in range(k):
        kth = kth.next
        if not kth:
            return dummy.next
```
- We try to find the **k-th node** after `group_prev`.
- If there are **less than k nodes left**, we stop and return the final list.

---
✅ **4. Reversing the Group**:
- If we found k nodes:
  - `group_next = kth.next` → Save the next node after kth (we’ll reconnect later).
  - Start reversing from `group_prev.next` till `group_next`.

```python
group_next = kth.next
prev, curr = group_next, group_prev.next
while curr != group_next:
    tmp = curr.next
    curr.next = prev
    prev = curr
    curr = tmp
```
- Here:
  - `prev` keeps track of **new head** of reversed group.
  - `curr` moves node-by-node, **reversing** their `.next` pointer.

---
✅ **5. Connect the reversed group back**:
- After reversing, we connect:
  - `group_prev.next = kth` (kth becomes new head of this group).
  - Move `group_prev` to `tmp` (which was the start node before reversal).

```python
tmp = group_prev.next
group_prev.next = kth
group_prev = tmp
```

---

### 📜 Big Picture

Think of the process like **chunking** the linked list into k-sized groups:

1. Find k nodes ✔️
2. Reverse them ✔️
3. Connect properly ✔️
4. Move forward ✔️

---

### ⚡ Time Complexity:
- Finding k nodes → O(k)
- Reversing k nodes → O(k)
- Total → O(N), because every node is visited a constant number of times.

---

# 2. **Rotate a linked list to the right by `k` positions**
#### 🧠 Intuition:
Rotating the list means we want the last `k` elements to come in front, and the rest to follow them.

### 🪜 Steps:

1. **Find the length of the list** (`n`):
   - Traverse the list once and count the number of nodes.

2. **Make the list circular**:
   - Connect the last node to the head, making it a loop.

3. **Find the new tail**:
   - The new tail will be at position `(n - k % n - 1)` from the start.
   - `k % n` handles cases where `k` is larger than `n`.

4. **Break the loop**:
   - The node after the new tail will be the new head.
   - Set `new_tail.next = None` to break the circular link.

---

### 🧮 Example:

List: `1 → 2 → 3 → 4 → 5`  
`k = 2`  
Length (`n`) = 5  
`k % n = 2`  
New tail is at position `5 - 2 - 1 = 2` → node with value `3`  
New head is node `4`  
Final: `4 → 5 → 1 → 2 → 3`

---
