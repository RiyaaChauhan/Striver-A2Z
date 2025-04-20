#  **Deletion in Doubly Linked List (DLL)**
##  Types of Deletion Operations

There are **3 major deletion operations** in a DLL:

1. **Delete from the Beginning**  
2. **Delete from the End**  
3. **Delete a Node with a Given Value (or Position)**

---

###  1. Deletion from the Beginning

####  Algorithm
- Check if the DLL is empty (`head == None`).
- Move the head to `head.next`.
- Set `head.prev = None`.

####  Python Code

```python
def delete_from_beginning(head):
    if head is None:
        return None
    new_head = head.next
    if new_head is not None:
        new_head.back = None
    return new_head
```

---

###  2. Deletion from the End

####  Algorithm
- If list is empty, return `None`.
- Traverse to the last node (`tail`).
- Update `tail.back.next = None`.

####  Python Code

```python
def delete_from_end(head):
    if head is None or head.next is None:
        return None
    tail = head
    while tail.next:
        tail = tail.next
    tail.back.next = None
    return head
```

---

###  3. Deletion of a Node with a Given Value

####  Algorithm
- Traverse the list to find the node with the given value `k`.
- If found:
  - If it's the head → use delete from beginning.
  - If it's the tail → use delete from end.
  - Otherwise:
    - Update `node.back.next = node.next`
    - Update `node.next.back = node.back`
- Free the node (in languages like C/C++; in Python, garbage collection handles it).

####  Python Code

```python
def delete_by_value(head, k):
    if head is None:
        return None
    
    # If node to delete is the head
    if head.data == k:
        return delete_from_beginning(head)

    curr = head
    while curr and curr.data != k:
        curr = curr.next

    if curr is None:
        return head  # Value not found

    # If node to delete is the last node
    if curr.next is None:
        curr.back.next = None
    else:
        curr.back.next = curr.next
        curr.next.back = curr.back

    return head
```

---

##  Example

### Original List:
```
12 ⇄ 5 ⇄ 8 ⇄ 7 ⇄ 4
```

### After:
- **Delete from beginning:** `5 ⇄ 8 ⇄ 7 ⇄ 4`
- **Delete from end:** `12 ⇄ 5 ⇄ 8 ⇄ 7`
- **Delete 8:** `12 ⇄ 5 ⇄ 7 ⇄ 4`

---

##  Time & Space Complexity

| Operation             | Time Complexity | Space Complexity |
|----------------------|------------------|------------------|
| Delete from beginning| O(1)             | O(1)             |
| Delete from end      | O(N)             | O(1)             |
| Delete by value      | O(N)             | O(1)             |

> 🔹 *N is the number of nodes in the list.*

---

##  Notes
- Always check for `None` to avoid `AttributeError`.
- Updating both `next` and `prev`/`back` pointers is crucial.
- Deleting head/tail needs special handling (don’t access `.back` or `.next` if `None`).
- Garbage collection in Python removes memory leaks, but in lower-level languages (C/C++), you must explicitly `free()` the node.

---

##  Full Example with Print

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

def print_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def convertArr2DLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    prev = head
    for val in arr[1:]:
        node = Node(val)
        node.back = prev
        prev.next = node
        prev = node
    return head

# Example
arr = [12, 5, 8, 7, 4]
head = convertArr2DLL(arr)
print("Original DLL:")
print_list(head)

head = delete_from_beginning(head)
print("After deleting from beginning:")
print_list(head)

head = delete_from_end(head)
print("After deleting from end:")
print_list(head)

head = delete_by_value(head, 8)
print("After deleting 8:")
print_list(head)
```