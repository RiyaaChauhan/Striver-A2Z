# 📂 Miscellaneous DSA Problems

This folder contains problems that are **not part of the standard Striver Sheet** but are carefully selected to **deepen conceptual clarity**, **reinforce core logic**, and **simulate real-world interview challenges**.
---

## 📁 Problem Tracker

| S.No. | Problem Name         | Topic        | Platform | code.py                                  |
|-------|----------------------|--------------|----------|------------------------------------------|
| 1     |[Partition Linked List](https://leetcode.com/problems/partition-list/)| Linked List, 2-pointers  | LeetCode #86 | [code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_31) |
|2|[ k-th node from the end of the linked list]()||||


## 📁 Pattern wise ques
| S.No. | Algo/Ques         |    code.py     | Platform | Status|
|-------|----------------------|--------------|----------|------------------------------|
| 1.| **Two Pointers**|||||
|→|[Introduction](https://github.com/RiyaaChauhan/Striver-A2Z/blob/main/Day_43/_01.Two_pointers_Introduction.md)||||[Intro](https://github.com/RiyaaChauhan/Striver-A2Z/blob/main/Day_43/_01.Two_pointers_Introduction.md)|✅|
|→|Pair with Target Sum ||||
|→|[Remove Duplicates]()|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_43)|Leetcode|✅|
|→|Squaring a Sorted Array||||
|→|Triplet Sum to Zero||||
|→|Triplet Sum Close to Target||||
|→|Triplets with Smaller Sum||||
|→|Subarrays with Product Less than a Target ||||
|→|Dutch National Flag Problem||||
|→|Quadruple Sum to Target||||
|→|Comparing Strings containing Backspaces||||
|→|Minimum Window Sort||||
|→|[Reverse String]()|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_43)|Leetcode|✅|
|→|[Two Sum II]()|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_43)|Leetcode|✅|
|→|[Remove Element](https://leetcode.com/problems/remove-element/)|[code.py](https://github.com/RiyaaChauhan/Striver-A2Z/tree/main/Day_43)|Leetcode|✅|
|2.|**Fast and Slow Pointers**||||
|→|Introduction||||
|3.|**Sliding Window**||||
---

# CHEATSHEET
### **Two Pointer Techniques for Linked Lists:**

#### 1. **Tortoise and Hare (Cycle Detection)**
   - **Use Case**: Detect if there is a cycle in the LL.
   - **Steps**:
     - Use two pointers: `slow` (moves one step) and `fast` (moves two steps).
     - If `slow` and `fast` meet, there's a cycle.
     - If `fast` reaches the end (`None`), no cycle exists.

#### 2. **Finding the N-th Node from the End**
   - **Use Case**: Find the N-th node from the end of a linked list.
   - **Steps**:
     - Move `fast` pointer `n` steps ahead.
     - Then, move both `slow` and `fast` pointers together until `fast` reaches the end.
     - The `slow` pointer will be at the N-th node from the end.

#### 3. **Deleting the N-th Node from the End**
   - **Use Case**: Remove the N-th node from the end.
   - **Steps**:
     - Move `fast` pointer `n` steps ahead.
     - Then, move both `slow` and `fast` together until `fast.next` is `None`.
     - `slow.next` is the node to delete.

#### 4. **Detecting the Start of a Cycle**
   - **Use Case**: Find the start node of the cycle (if it exists).
   - **Steps**:
     - First detect the cycle using the Tortoise and Hare method.
     - Once a cycle is detected, reset the `slow` pointer to the head of the list.
     - Move both pointers one step at a time. When they meet, it's the start of the cycle.

#### 5. **Reversing a Linked List (Using Two Pointers)**
   - **Use Case**: Reverse a singly linked list.
   - **Steps**:
     - Use two pointers: `prev` and `current`.
     - Traverse through the list, updating the `current.next` to `prev`.
     - Move `prev` to `current` and `current` to `next_node`.

---

### **Quick Pointers to Remember:**
1. **Fast Pointer** moves faster than **slow pointer** (often twice as fast).
2. After shifting the fast pointer, always **move both pointers simultaneously** to maintain the gap.
3. Use a **prev pointer** when you need to remove a node or track the previous node.