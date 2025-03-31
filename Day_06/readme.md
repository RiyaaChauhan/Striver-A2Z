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