class Solution:
    def searchRange(self, nums, target):
        lower = self.LowerBound(nums, target)
        if lower == -1 or nums[lower] != target:
            return (-1, -1)
        return (lower, self.UpperBound(nums, target))

    def UpperBound(self, arr, x):
        left, right = 0, len(arr) - 1
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def LowerBound(self, arr, x):
        left, right = 0, len(arr) - 1
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] >= x:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

# class Solution:
#     def searchRange(self, nums, target):
#         def findBound(isFirst):
#             left, right = 0, len(nums) - 1
#             ans = -1

#             while left <= right:
#                 mid = left + (right - left) // 2

#                 if nums[mid] == target:
#                     ans = mid
#                     if isFirst:
#                         right = mid - 1  # Move left to find first occurrence
#                     else:
#                         left = mid + 1   # Move right to find last occurrence
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
            
#             return ans

#         first = findBound(True)
#         last = findBound(False)
#         return (first, last)