##  1. Reverse a Linked List (Iterative Approach)

###  Problem Statement

Given the head of a singly linked list, reverse the list and return the new head.

### 🧠 Key Idea

The idea is to reverse the direction of the `next` pointer for each node. You’ll use **three pointers**:

- `prev` → tracks the previous node (starts as `None`)
- `curr` → the current node we’re processing
- `next_node` → a temporary pointer to store the next node before we change `curr.next`

###  Example

Original Linked List:
```
1 -> 2 -> 3 -> 4 -> 5 -> None
```

After Reversing:
```
5 -> 4 -> 3 -> 2 -> 1 -> None
```
---

## 🔍 Brute Force, Better, Optimal — Reverse a Linked List

### ⚙️ Brute Force (Not Recommended, Just Theoretical)

- **Idea**: Use an array or list to store all node values, then create a new linked list in reverse.
- **Steps**:
  1. Traverse the original linked list and store values in an array.
  2. Reverse the array.
  3. Create a new linked list using reversed values.

- **Time**: O(n)  
- **Space**: O(n) — uses extra array

```python
def reverseList(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    
    dummy = ListNode()
    cur = dummy
    for val in reversed(vals):
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next
```

> ⚠️ This method **violates** the constraint of **O(1) space**, and creates a **new list** instead of reversing in-place.

---

### 🔧 Better (Recursive)

- **Idea**: Recursively reverse the list by reversing the rest of the list and then adjusting pointers.
- **Time**: O(n)  
- **Space**: O(n) — due to recursion stack

```python
def reverseList(head):
    if not head or not head.next:
        return head
    
    newHead = reverseList(head.next)
    head.next.next = head
    head.next = None
    return newHead
```

> 👍 Cleaner and elegant, but not constant space due to recursion.

---

### 🚀 Optimal (Iterative – In-Place)

This is the best solution.

- **Time**: O(n)  
- **Space**: O(1)

```python
def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev
```

✅ **In-place, constant space, one-pass**

---

###  Summary

| Approach      | Time  | Space | Notes                                  |
|---------------|-------|--------|----------------------------------------|
| Brute Force   | O(n)  | O(n)   | Uses extra array, creates new list     |
| Recursive     | O(n)  | O(n)   | Clean code but uses recursion stack    |
| Iterative ✅   | O(n)  | O(1)   | Best approach, modifies in-place       |
