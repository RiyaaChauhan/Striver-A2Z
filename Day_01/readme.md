# **1. Inserting a Node in a Singly Linked List**
## Problem Statement
Given the head of a **singly linked list** and a value `x`, insert a new node with value `x` at the end of the list.

## Approach
1. Create a new node with value `x`.
2. If the list is empty, return the new node as the head.
3. Traverse the list to find the last node.
4. Append the new node to the last node's `next` pointer.
5. Return the updated head.

## Pseudo-code
```python
class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)
        if head is None:
            return new_node
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return head
```

## Complexity Analysis
- **Time Complexity:** `O(n)` (Traverses the list once)
- **Space Complexity:** `O(1)` (Uses constant extra space)

## Example
**Input:** `head = [1 -> 2 -> 3 -> None], x = 4`

**Output:** `1 -> 2 -> 3 -> 4 -> None`
---------------------------------------------------------------------------- 

# **2. Delete a Node in a Singly Linked List**

## **Problem Statement**  
You are given a **node** in a **singly linked list**, and you need to **delete** this node.

## **Constraints:**  
- You **do not** have access to the **head** of the linked list.  
- The given node **is not the last node** in the list.  
- The linked list contains **unique values**.  
- The deletion should:
  - Remove the given node’s value from the linked list.  
  - Keep all other nodes in the same order.  
  - Reduce the linked list length by 1.  

## **Example**  
### **Input:**  
```plaintext
Linked List: 4 -> 5 -> 1 -> 9
Node to delete: 5
```

### **Process:**  
1. Copy the value of the **next node** (`1`) into `5`.  
2. Change `5`'s `next` pointer to skip `1` and point to `9`.  

### **Output:**  
```plaintext
Modified Linked List: 4 -> 1 -> 9
```

## **Approach**  
Since we **do not have access to the previous node**, we cannot directly unlink the node from the list. Instead, we do the following:  
1. **Copy the value** of the next node into the current node.  
2. **Update the next pointer** of the current node to skip the next node.  

## **Pseudo Code**  
```plaintext
Function deleteNode(node):
    If node is None or node.next is None:
        Return  # Edge case (should not happen as per constraints)
    
    node.data = node.next.data  # Copy value of next node into current node
    node.next = node.next.next  # Skip the next node
```
## **Complexity Analysis**  
| Complexity | Explanation |
|------------|------------|
| **Time Complexity: O(1)** | We only modify one node in constant time. |
| **Space Complexity: O(1)** | No extra space is used. |

-------------------------------------------------------------------

# **3. Find the length of Linked List**
# Count Nodes in a Linked List

## Problem Statement
Given the head of a **singly linked list**, count the total number of nodes.

## Approach
1. Initialize `count = 0`.
2. Traverse the list using a pointer `curr`.
3. Increment `count` for each node until reaching `None`.
4. Return `count`.

## Pseudo-code
```python
class Solution:
    def getCount(self, head):
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        return count
```

## Complexity Analysis
- **Time Complexity:** `O(n)` (Traverses the list once)
- **Space Complexity:** `O(1)` (Uses constant extra space)

-------------------------------------------------------------------------------------------------------- 

# **4. Search an element in Linked List**
## **Problem Statement:**  
Algorithm for Searching a Key in a Singly Linked List
The goal of this function is to determine whether a given key exists in a singly linked list.

## Algorithm:
- Initialize a pointer curr to the head of the linked list.
- Iterate through the linked list while curr is not None:
    - Check if curr.data is equal to key.
    - If found, return True.
- Otherwise, move curr to the next node.
- If the loop completes without finding the key, return False.

# Search Key in a Linked List

## Problem Statement
Given a singly linked list of `n` nodes and a key, the task is to check whether the key is present in the linked list.

## Pseudocode
```
FUNCTION searchKey(head, key):
    curr = head  // Initialize current node to head
    
    WHILE curr is NOT NULL:
        IF curr.data == key:
            RETURN True  // Key found, return True
        curr = curr.next  // Move to the next node
    
    RETURN False  // Key not found
```

## Explanation
1. Initialize a pointer `curr` to the head of the linked list.
2. Traverse the linked list while `curr` is not `NULL`:
   - If `curr.data` matches `key`, return `True`.
   - Otherwise, move `curr` to the next node.
3. If the loop completes without finding the key, return `False`.

## **Complexity Analysis**  
| Complexity | Explanation |
|------------|------------|
| **Time Complexity: O(n)** |In the worst case, we may traverse all nodes in the list |
| **Space Complexity: O(1)** |Uses only a few extra variables, no additional data structures|

## Example Walkthrough
### Example 1: Key is present
**Input:**
```
n = 5
Linked List: 1 -> 3 -> 5 -> 7 -> 9
key = 7
```
**Steps:**
1. Start at head (`1`). `1 != 7`, move to next.
2. Check `3`. `3 != 7`, move to next.
3. Check `5`. `5 != 7`, move to next.
4. Check `7`. **Found the key!** Return `True`.

-------------------------------------------------------------------------------------------------------- 

# **5. Finding the Middle of a Linked List**  
## **Problem Statement:**  
Given the head of a singly linked list, find the middle node.  
- If the list has an **odd number** of nodes, return the middle node.  
- If the list has an **even number** of nodes, return the **second middle** node.  
### **Example Cases:**  
#### **Example 1 (Odd Length)**  
**Input:** `1 -> 2 -> 3 -> 4 -> 5`  
**Output:** `3`  
#### **Example 2 (Even Length)**  
**Input:** `1 -> 2 -> 3 -> 4 -> 5 -> 6`  
**Output:** `4`  

## **Approach (Two-Pointer Method - Slow & Fast Pointers)**  
We use two pointers:  
- **Slow pointer (`slow`)** moves **one step** at a time.  
- **Fast pointer (`fast`)** moves **two steps** at a time.  
- When `fast` reaches the end, `slow` will be at the **middle node**.  
- If the list length is **even**, `slow` will be at the **second middle node** (since `fast` moves twice as fast).  
### **Pseudo Code:**  
```
Function getMiddle(head):
    If head is NULL:
        Return NULL

    slow = head
    fast = head

    While fast is not NULL and fast.next is not NULL:
        slow = slow.next
        fast = fast.next.next

    Return slow.data  # Middle node's value
```

## **Implementation**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def getMiddle(self, head):
        if head is None:
            return None  # If list is empty
        
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data  # Return middle node's value

# Test cases
arr1 = [1, 2, 3, 4, 5]  # Odd length -> Middle is 3
arr2 = [1, 2, 3, 4, 5, 6]  # Even length -> Middle is 4

head1 = create_linked_list(arr1)
head2 = create_linked_list(arr2)

solution = Solution()
print(solution.getMiddle(head1))  # Output: 3
print(solution.getMiddle(head2))  # Output: 4
```
## **Complexity Analysis:**  
| Complexity | Explanation |
|------------|------------|
| **Time Complexity: O(N)** | Each node is visited once (`fast` pointer moves twice as fast, `slow` moves N/2 times). |
| **Space Complexity: O(1)** | No extra space is used apart from pointers. |

## **Key Takeaways:**  
✅ Uses **slow & fast pointers** for efficient traversal.  
✅ Works for **both even and odd** lengths.  
✅ **O(N) time** and **O(1) space**, making it optimal.  