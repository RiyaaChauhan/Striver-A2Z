# 1.Middle of a LinkedList [Tortoise-Hare Method]
✅ **Step 1**:  
Use two pointers —  
- `slow` → moves **one step** at a time.  
- `fast` → moves **two steps** at a time.  

✅ **Step 2**:  
When `fast` reaches the end, `slow` will be at the **middle** node.  

✅ **Step 3**:  
To **delete the middle node**, you need to somehow **skip** it.  
➡️ So you'll also keep a pointer like `prev` which will track the node **before slow**.  
➡️ Then do `prev.next = slow.next`, meaning you unlink (delete) the slow (middle) node!

✅ **Step 4**:  
Return the modified linked list.

Key point:

prev saves the position just before slow moves.
Thus, it always "tracks" one node behind slow.

Shortcut to remember 🧠:
prev = slow → before slow moves.

---

# 2.