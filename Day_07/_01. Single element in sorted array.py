class Solution:
    def singleNonDuplicate(self, nums):

        n=len(nums)
        if n==1:
            return nums[0]

        if (nums[0] != nums[1]):
            return nums[0]

        if nums[n-1]!=nums[n-2]:
            return nums[n-1]

        low,high=1,n-2
        while (low<=high):
            mid=(low+high)//2
            if (nums[mid]!=nums[mid+1] and nums[mid] != nums[mid-1]):
                return nums[mid]

            if (mid%2==1 and nums[mid]==nums[mid-1] or (mid%2==0 and nums[mid]==nums[mid+1])):
                low=mid+1
            else:
                high=mid-1
        return -1




# class Solution:
#     def singleNonDuplicate(self, nums):

#             left, right = 0, len(nums) - 1

#             while left < right:
#                 mid = left + (right - left) // 2
#                 # Ensure mid is even for pair checking
#                 if mid % 2 == 1:
#                     mid -= 1  

#                 if nums[mid] == nums[mid + 1]:
#                     left = mid + 2  # Move right
#                 else:
#                     right = mid  # Move left

#             return nums[left]