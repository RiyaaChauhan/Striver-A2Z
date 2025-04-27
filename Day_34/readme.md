# 2. Merge 2 sorted linked list

---

# 3. Detect a loop in linked list

Using two pointers, where one pointer moves one step at a time (`i`), and the other moves two steps at a time (`j`), is a common approach known as **Floyd’s Cycle-Finding Algorithm** or the **Tortoise and Hare Algorithm**. 

### Plan:
1. **Initialize two pointers**: 
   - `slow` moves one step at a time.
   - `fast` moves two steps at a time.
2. **Traverse the list**:
   - If there's a cycle, `slow` and `fast` will eventually meet (they will point to the same node).
   - If there’s no cycle, `fast` will reach the end (`None`).
3. **Return the result**:
   - If they meet, a loop exists, return `True`.
   - If `fast` reaches `None`, no loop exists, return `False`.

---

# 4. **Algorithm: Find Start of Cycle in a Linked List**

**Step 1:**  
Initialize two pointers:  
- `slow = head`
- `fast = head`

**Step 2:**  
Move `slow` one step at a time (`slow = slow.next`)  
Move `fast` two steps at a time (`fast = fast.next.next`)

**Step 3:**  
While traversing, if `fast` and `slow` meet, a **cycle** is detected.  
If `fast` becomes `None` or `fast.next` becomes `None`, **no cycle** → return `None`.

**Step 4:**  
Once cycle is detected (slow == fast), reset `slow` pointer back to `head`.

**Step 5:**  
Now move both `slow` and `fast` one step at a time.  
When they meet again, that node is the **starting point of the cycle**. Return that node.

---

### ✨ **Why this works?**
- The distance between head and start of cycle = distance between meeting point and start of cycle inside the loop.
- So, after resetting `slow`, they will meet exactly at the cycle start.