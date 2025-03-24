## **Finding the Middle of a Linked List**  

### **Problem Statement:**  
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

---

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

---

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

---

## **Complexity Analysis:**  
| Complexity | Explanation |
|------------|------------|
| **Time Complexity: O(N)** | Each node is visited once (`fast` pointer moves twice as fast, `slow` moves N/2 times). |
| **Space Complexity: O(1)** | No extra space is used apart from pointers. |

---

## **Key Takeaways:**  
✅ Uses **slow & fast pointers** for efficient traversal.  
✅ Works for **both even and odd** lengths.  
✅ **O(N) time** and **O(1) space**, making it optimal.  