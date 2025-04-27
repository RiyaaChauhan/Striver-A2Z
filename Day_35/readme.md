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
Detect the loop:
Use Floyd's cycle-finding algorithm (tortoise and hare algorithm) to detect if a loop exists. Initialize two pointers, slow and fast, to the head of the linked list. Move slow one step and fast two steps at a time. If they meet, a loop exists. If fast reaches the end of the list, no loop exists.
Locate a node within the loop:
When slow and fast meet, they are inside the loop. Store this meeting point in a variable, loop_node.
Count the nodes in the loop:
Starting from loop_node, traverse the loop, counting the nodes until you reach loop_node again.
Python