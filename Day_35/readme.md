# 1.Middle of a LinkedList [Tortoise-Hare Method]
- When we want to **delete a middle node** from a Linked List,  
  we use **two pointers**:  
  - `slow` → moves **one step** at a time  
  - `fast` → moves **two steps** at a time  

- `fast` reaching the end means `slow` is at the middle.  
- To **delete** the middle node, we need to maintain another pointer `prev`,  
  which always **lags one step behind slow**.  
- After finding the middle:  
  - we simply do `prev.next = slow.next` to **remove slow** from the list. ✅

**Key Learning:**  
👉 prev saves the position just before slow moves.
👉 Thus, it always "tracks" one node behind slow.

Shortcut to remember 🧠:
prev = slow → before slow moves.

---

# 2.