# **Delete a Node in a Singly Linked List**

## **Problem Statement**  
You are given a **node** in a **singly linked list**, and you need to **delete** this node.

### **Constraints:**  
- You **do not** have access to the **head** of the linked list.  
- The given node **is not the last node** in the list.  
- The linked list contains **unique values**.  
- The deletion should:
  - Remove the given node’s value from the linked list.  
  - Keep all other nodes in the same order.  
  - Reduce the linked list length by 1.  

---

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

---

## **Approach**  
Since we **do not have access to the previous node**, we cannot directly unlink the node from the list. Instead, we do the following:  
1. **Copy the value** of the next node into the current node.  
2. **Update the next pointer** of the current node to skip the next node.  

---

## **Pseudo Code**  
```plaintext
Function deleteNode(node):
    If node is None or node.next is None:
        Return  # Edge case (should not happen as per constraints)
    
    node.data = node.next.data  # Copy value of next node into current node
    node.next = node.next.next  # Skip the next node
```

---

## **Complexity Analysis**  
| Complexity | Explanation |
|------------|------------|
| **Time Complexity: O(1)** | We only modify one node in constant time. |
| **Space Complexity: O(1)** | No extra space is used. |

This approach efficiently **removes the node without needing the head**. 🚀 Let me know if you need more clarifications!

