#  **Deletion in Doubly Linked List (DLL)**

##  Types of Deletion Operations in DLL

There are **4 major types** of deletion operations:

1. 🔹 **Delete from the Beginning**  
2. 🔹 **Delete from the End**  
3. 🔹 **Delete the k-th Node (by Position)**  
4. 🔹 **Delete by Value**

---

## 1️⃣ Delete from the Beginning

###  Algorithm
- Check if list is empty.
- Move `head` to `head.next`.
- Set `head.prev` (or `head.back`) to `None`.

###  Python Code

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

## 2️⃣ Delete from the End

###  Algorithm
- If list is empty, return `None`.
- Traverse to the last node.
- Update `last.prev.next = None`.

### 🧑‍💻 Python Code

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

## 3️⃣ Delete the k-th Node (by Position)

###  Algorithm
- If `k == 1`, call `delete_from_beginning`.
- Traverse to the `k-th` node.
- If node exists:
  - Update pointers:
    - `node.prev.next = node.next`
    - `node.next.prev = node.prev`

###  Python Code

```python
def delete_kth_node(head, k):
    if head is None:
        return None
    if k == 1:
        return delete_from_beginning(head)
    
    curr = head
    count = 1
    while curr and count < k:
        curr = curr.next
        count += 1
    
    if curr is None:
        return head  # k is out of range

    if curr.next:
        curr.next.back = curr.back
    if curr.back:
        curr.back.next = curr.next

    return head
```

---

## 4️⃣ Delete a Node by Value

###  Algorithm
- Traverse to find the node with `data == value`.
- If found:
  - If it's the head → use delete from beginning.
  - If it's the tail → use delete from end.
  - Else:
    - Update `node.prev.next = node.next`
    - Update `node.next.prev = node.prev`

###  Python Code

```python
def delete_by_value(head, value):
    if head is None:
        return None
    if head.data == value:
        return delete_from_beginning(head)
    
    curr = head
    while curr and curr.data != value:
        curr = curr.next

    if curr is None:
        return head  # Value not found

    if curr.next:
        curr.next.back = curr.back
    if curr.back:
        curr.back.next = curr.next

    return head
```

---

##  Time and Space Complexity

| Operation             | Time Complexity | Space Complexity |
|----------------------|------------------|------------------|
| Delete from beginning| O(1)             | O(1)             |
| Delete from end      | O(N)             | O(1)             |
| Delete by position   | O(K)             | O(1)             |
| Delete by value      | O(N)             | O(1)             |

> 🔹 *N is the number of nodes in the list, and K is the position.*

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