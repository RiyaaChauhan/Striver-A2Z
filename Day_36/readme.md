# 1. Remove Nth node from back of LL

# 2. **deleting all occurrences of a key in a Doubly Linked List (DLL)** 
### **Goal**:
You want to **delete all nodes** in the list that have a specific value (`key`).

### **Steps**:
1. **Traversal**: We start by traversing the entire linked list, from the head to the tail, and check if the `data` of each node matches the key you want to delete.
   
2. **Deleting Nodes**: When we find a node whose `data` matches the `key`, we need to:
   - Adjust the `prev` and `next` pointers of neighboring nodes to remove the node.
   - We also handle edge cases for head and tail nodes, as deleting these requires updating the `head` and `tail` pointers.

### **Key Cases to Handle**:
1. **If the node is the head**: This is the first node in the list. When it's deleted, the `head` needs to be updated to the next node.
   - If there's no next node, we set the `head` to `None` (the list is now empty).

2. **If the node is the tail**: This is the last node in the list. When it's deleted, the `prev` pointer of the second-to-last node needs to be updated to `None`.

3. **If the node is in the middle**: This node has both a previous and next node. We simply adjust the pointers of the previous and next nodes to "skip" the current node.

### **Detailed Code Explanation**:

```python
class Node:
    def __init__(self, data=None):
        self.data = data  # Node's data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class Solution:
    def deleteKey(self, head, key):
        current = head  # Start with the head node
        
        # Traverse the entire list
        while current:
            if current.data == key:  # Check if current node's data matches the key
                # If it's the head node (no prev node)
                if current.prev is None:
                    head = current.next  # Update head to the next node
                    if head:  # If the list isn't empty, update the new head's prev to None
                        head.prev = None
                # If it's the tail node (no next node)
                elif current.next is None:
                    current.prev.next = None  # Update the second-to-last node's next to None
                else:  # If the node is in the middle
                    current.prev.next = current.next  # Skip the current node in the next direction
                    current.next.prev = current.prev  # Skip the current node in the previous direction

            current = current.next  # Move to the next node

        return head  # Return the updated head of the list

# Helper function to print the DLL
def printDLL(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

# Example usage:
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

# Linking nodes to form a DLL
head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = fifth
fifth.prev = fourth

# Print the original DLL
print("Original DLL:")
printDLL(head)

# Deleting key 3
key = 3
solution = Solution()
head = solution.deleteKey(head, key)

# Print DLL after deleting key 3
print(f"\nDLL after deleting key {key}:")
printDLL(head)
```

### **How This Code Works**:
1. **Node Class**: Represents a single node in the doubly linked list. Each node has:
   - `data`: The value of the node.
   - `next`: Points to the next node.
   - `prev`: Points to the previous node.

2. **Solution Class**: Contains the `deleteKey` function, which deletes all nodes with a specific `key` from the doubly linked list.

   - The `while current:` loop traverses through the entire list.
   - Inside the loop, we check if `current.data == key` to identify the node that needs to be deleted.
   
   **Delete Node Logic**:
   - If the node is the **head**, we update the `head` pointer and ensure the new head's `prev` is `None`.
   - If the node is the **tail**, we update the second-to-last node’s `next` pointer to `None`.
   - If the node is in the **middle**, we adjust the `next` pointer of the previous node and the `prev` pointer of the next node to skip the current node.
   
3. **Helper Function (`printDLL`)**: This is used to print the doubly linked list in the format `data <-> data <-> data <-> None` so we can visualize the linked list.

### **Example Output**:
- **Before Deleting**:
  ```
  Original DLL:
  1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None
  ```
  
- **After Deleting key `3`**:
  ```
  DLL after deleting key 3:
  1 <-> 2 <-> 4 <-> 5 <-> None
  ```

This shows that the node with value `3` is removed from the list.

### **Conclusion**:
This approach ensures that all occurrences of the key are deleted from the **Doubly Linked List (DLL)**. The important part is correctly managing the `prev` and `next` pointers to maintain the structure of the list while removing nodes.

---

# 3. Check if LL is palindrome or not

### Steps:
1. **Find the middle of the list**:
   - Use the **slow and fast pointer** approach (Tortoise and Hare) to find the middle of the linked list. The `slow` pointer will be at the middle when the `fast` pointer reaches the end.
   
2. **Reverse the second half of the list**:
   - Once you find the middle, reverse the second half of the list.
   
3. **Compare the first half and the reversed second half**:
   - Use two pointers, one starting from the head of the list and the other starting from the beginning of the reversed second half. Compare the values at each step.
   
4. **Restore the second half (optional)**:
   - If you want to maintain the original structure of the linked list, you can reverse the second half again to restore the original list.

### Code:
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list (slow and fast pointers)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Compare the first half and the reversed second half
        left = head
        right = prev
        while right:  # Only need to check the second half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
```

### Explanation:
1. **Finding the middle**:
   - The `fast` pointer moves two steps at a time, and the `slow` pointer moves one step at a time. When the `fast` pointer reaches the end, the `slow` pointer will be at the middle of the list.
   
2. **Reversing the second half**:
   - After the middle is found, we reverse the second half of the list starting from the `slow` pointer.
   
3. **Comparing the two halves**:
   - We then compare the values in the first half and the reversed second half. If they match at every step, it's a palindrome.

### Time Complexity:
- Finding the middle of the list takes \( O(n) \).
- Reversing the second half takes \( O(n/2) \), which is effectively \( O(n) \).
- Comparing the two halves takes \( O(n/2) \), which is also \( O(n) \).
So, the overall time complexity is \( O(n) \).

### Space Complexity:
- Since we only use a few extra pointers (constant space), the space complexity is \( O(1) \).