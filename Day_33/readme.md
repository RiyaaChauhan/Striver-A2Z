✅ **Quick Explanation of code:**

- You start from `curr = head`.
- While there are at least two nodes (`curr` and `curr.next`):
  - If **current node value == next node value** ➔ skip the next node by `curr.next = curr.next.next`.
  - Else ➔ move `curr` to `curr.next`.
- Finally, return the `head` of modified list.

---

⚡ **Time Complexity:**  
- `O(N)` — you visit each node exactly once.

⚡ **Space Complexity:**  
- `O(1)` — no extra space used, just pointer manipulation.