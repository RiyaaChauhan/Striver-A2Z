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

# 2. Length of loop in Linked list:
1. **Detecting the Loop:** 
   - We can use the **Floyd’s Cycle-Finding Algorithm (Tortoise and Hare)** to detect if a cycle exists. 
   - The idea is to have two pointers, `slow` and `fast`. `slow` moves one step at a time, while `fast` moves two steps at a time.
   - If there's a loop, `slow` and `fast` will eventually meet inside the loop.

2. **Counting the Length of the Loop:** 
   - Once we detect the cycle (when `slow == fast`), we can reset one of the pointers (let's say `slow`) to the meeting point and keep it fixed.
   - Then, move the other pointer (say `fast`) around the loop while counting each step until `fast` reaches `slow` again. 
   - This count will give you the length of the loop.
---
Steps:
Cycle Detection:

We use slow and fast pointers to detect the cycle.

If they meet (slow == fast), we have a cycle.

Counting the Length of the Loop:

After detecting the cycle, we reset the slow pointer to where fast met it and start counting nodes until slow reaches fast again.