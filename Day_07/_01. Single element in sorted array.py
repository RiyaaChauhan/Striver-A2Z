class Solution:
    def singleNonDuplicate(self, nums):

            left, right = 0, len(nums) - 1

            while left < right:
                mid = left + (right - left) // 2
                # Ensure mid is even for pair checking
                if mid % 2 == 1:
                    mid -= 1  

                if nums[mid] == nums[mid + 1]:
                    left = mid + 2  # Move right
                else:
                    right = mid  # Move left

            return nums[left]