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

# 4.