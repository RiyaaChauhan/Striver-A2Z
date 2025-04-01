# 1. Finding Minimum in a Rotated Sorted Array

## Methods to Solve the Problem
To find the minimum element in a rotated sorted array, we can use different methods:
1. **Linear Search (`O(N)`)**: Traverse the array and find the minimum. However, this is inefficient for large arrays.
2. **Binary Search (`O(log N)`)**: Since the array is sorted and rotated, binary search helps us efficiently locate the minimum element.

### **Why Use Binary Search?**
- The array maintains a **sorted structure** with a single rotation.
- Binary search allows us to eliminate half of the elements in each step, making it significantly **faster than linear search**.
- Using conditions like `nums[low] <= nums[high]`, we can detect sorted subarrays early and reduce unnecessary comparisons.
- Recognizing the **sorted half** of the array is crucial, as it allows us to systematically eliminate unnecessary search spaces.
- The **rotation point** always contains the minimum element, guiding our search process effectively.

## Problem Statement
You are given a rotated sorted array `nums`, where the original array was sorted in ascending order and then rotated at some unknown pivot. Your task is to find the minimum element in the array in **O(log N)** time complexity.

### **Example 1**
#### **Input:**
```python
nums = [4, 5, 6, 7, 0, 1, 2]
```
#### **Array Representation:**
```
Index:  0  1  2  3  4  5  6  
Nums:   4  5  6  7  0  1  2  
```
#### **Output:**
```
0
```
#### **Explanation:**
- The original sorted array was `[0, 1, 2, 4, 5, 6, 7]`.
- It was rotated at index `3`, causing `0` to become the minimum.

### **Example 2**
#### **Input:**
```python
nums = [3, 4, 5, 1, 2]
```
#### **Array Representation:**
```
Index:  0  1  2  3  4  
Nums:   3  4  5  1  2  
```
#### **Output:**
```
1
```
#### **Explanation:**
- The original sorted array was `[1, 2, 3, 4, 5]`.
- It was rotated at index `2`, making `1` the minimum.

## **Approach: Binary Search**
Since the array is rotated but sorted, **binary search** can be used to find the minimum efficiently.

### **How It Works?**
1. **Find the Middle Element**: Calculate `mid = (low + high) // 2`.
2. **Check If Left Half is Sorted**:
   - If `nums[low] <= nums[high]`, it means the subarray is already sorted, and `nums[low]` is the minimum.
3. **Compare Mid with High**:
   - If `nums[mid] >= nums[low]`, it means the left half is sorted, and the minimum is in the right half → Move `low = mid + 1`.
   - Otherwise, the right half is sorted, and the minimum is in the left half → Move `high = mid - 1`.
4. **Optimize Further**:
   - If the search space is already sorted, the smallest element can be directly determined without further searching.
   - This optimization reduces unnecessary iterations, improving time complexity while maintaining accuracy.

## **Key Points:**
- Initialization: low and high are used to define the current search range within the array. ans starts as infinity to ensure any number found will be smaller.

Binary Search Logic:

- The loop runs as long as low is less than or equal to high.
- mid is calculated to find the middle index.
- Checking Sorted Condition:
    - The condition if nums[low] <= nums[high]: checks if the array segment defined by low and high is sorted. If true, the minimum must be at nums[low] or earlier, and the current ans is updated.
- The break statement exits the loop immediately after updating ans, which is not the typical behavior expected in finding a minimum in a rotated array.

## **Optimized Python Solution**
```python
class Solution:
    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        ans = float('inf')  # Initialize with a large value

        while low <= high:
            mid = (low + high) // 2  # Integer division
            
            # If the subarray is sorted, return the leftmost element
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break

            # Update the answer
            ans = min(ans, nums[mid])

            # Decide which half to explore
            if nums[mid] >= nums[low]:  # Left half is sorted, search in right half
                low = mid + 1
            else:  # Right half is sorted, search in left half
                high = mid - 1

        return ans
```

## **Complexity Analysis**
- **Time Complexity:** `O(log N)` (Binary search reduces the search space by half each iteration)
- **Space Complexity:** `O(1)` (Only a few variables are used)

## **Edge Cases Considered**
- **Already sorted array:** `[1, 2, 3, 4, 5]` → Output: `1`
- **Single element array:** `[10]` → Output: `10`
- **Array with duplicates:** `[2, 2, 2, 0, 1]` → Output: `0`
- **Array rotated at different positions**: Checked for multiple variations to ensure correctness.

## **Why This Works Efficiently?**
- **Binary search** ensures `O(log N)` efficiency compared to `O(N)` in a linear search.
- The condition `nums[low] <= nums[high]` ensures we detect sorted portions early.
- Proper handling of mid-point comparison directs the search to the correct half.
- The **sorted half** may or may not contain the minimum, so careful decision-making in each iteration is key.

-----------------------------------------------------------------------------------------------------------------

# 2. Finding how many times has an array been rotated       
### Problem Statement

You have an increasing sorted array of distinct integers that has been **right-rotated** multiple times. Your task is to find out how many times the array was rotated, denoted as **k**. 

For example, if you have the array \[2, 4, 6, 9\] and it has been rotated 2 times to the right, it will appear as follows:
- **After 1st Rotation:** \[9, 2, 4, 6\]
- **After 2nd Rotation:** \[6, 9, 2, 4\]

### Examples

1. **Input:** \[5, 1, 2, 3, 4\]  
   **Output:** 1  
   **Explanation:** The original sorted array is \[1, 2, 3, 4, 5\]. This was rotated 1 time to the right.

2. **Input:** \[1, 2, 3, 4, 5\]  
   **Output:** 0  
   **Explanation:** The array is already sorted and not rotated at all.

### Approach

To solve this problem efficiently, we can use a modified binary search method. This allows us to achieve the expected time complexity of **O(log(n))**. 

Here's the reasoning behind choosing this approach:
- A binary search can help us identify the rotation point where the sorted order is disrupted.
- By comparing elements in the array, we can determine which half of the array contains the smallest element, which indicates the number of rotations.

### Pseudocode

```plaintext
function findKRotation(arr):
    low = 0
    high = length(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if mid element is the smallest
        if mid > 0 and arr[mid] < arr[mid - 1]: 
            return mid
        
        # Determine the sorted half
        if arr[low] <= arr[mid]: 
            # Left half is sorted
            low = mid + 1
        else:
            # Right half is sorted
            high = mid - 1
            
    return 0  # means the array is not rotated
```

### Explanation of the Code

Let's go through the code step by step:

```python
def findKRotation(arr):
    low = 0  # Start index
    high = len(arr) - 1  # End index

    while low <= high:  # Continue until the search space is exhausted
        mid = (low + high) // 2  # Find the middle index
        
        # Check if mid element is the smallest
        if mid > 0 and arr[mid] < arr[mid - 1]: 
            return mid  # We've found the rotation point
        
        # Determine which part of the array is sorted
        if arr[low] <= arr[mid]:  # Left side is sorted
            low = mid + 1  # Move to the unsorted side
        else:  # Right side is sorted
            high = mid - 1  # Move to the unsorted side
            
    return 0  # If we didn't find the rotation point, return 0
```

### Code Comments
- **low** and **high** represent the current search boundaries.
- We continuously narrow down the search space until we find the rotation point or confirm that the array is unrotated.
- The conditions inside the loop check if the array is sorted and decide which half to search next.
- The algorithm efficiently narrows down possibilities, yielding a logarithmic time complexity.

### Time and Space Complexity

1. **Time Complexity:**
   - The time complexity of the approach is **O(log n)** because we are using a binary search algorithm. In each iteration, we reduce the search space by half. 

2. **Space Complexity:**
   - The space complexity is **O(1)** since we are using a constant amount of extra space (just a few variables) regardless of the size of the input array.

### Edge Cases

Here are some edge cases to consider when implementing the solution:

1. **Empty Array:**
   - **Input:** \[\]
   - **Output:** 0 (The empty array has no rotations.)
   
2. **Single Element Array:**
   - **Input:** \[42\]
   - **Output:** 0 (One-element arrays are trivially not rotated.)

3. **Array Not Rotated:**
   - **Input:** \[1, 2, 3, 4, 5\]
   - **Output:** 0 (Already sorted, no rotations.)

4. **All Elements Same:**
   - Although the problem states that the array consists of **distinct** integers, if we consider it hypothetically, any array with all identical elements (e.g., \[5, 5, 5, 5\]) would also return 0 as it wouldn't be meaningful to discuss rotations.

5. **Max Rotations:**
   - **Input:** \[5, 1, 2, 3, 4\] (rotated fully)
   - The output would be 1, indicating that the sorted version shifted by one position.

6. **Rotated at the Boundaries:**
   - **Input:** \[4, 5, 1, 2, 3\]
   - **Output:** 2 (The smallest element is at index 2).

7. **Large Arrays:**
   - Test with the maximum array size as stipulated in the constraints (e.g., an array of size 100,000). How the algorithm performs under high load should also be verified.