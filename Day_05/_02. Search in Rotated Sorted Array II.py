class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Found target
            if nums[mid] == target:
                return True

            # Handling duplicates (skip them)
            while low < mid and nums[low] == nums[mid]:
                low += 1
            while high > mid and nums[high] == nums[mid]:
                high -= 1

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1  # Search left
                else:
                    low = mid + 1   # Search right
            else:  # Right half is sorted
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1  # Search right
                else:
                    high = mid - 1  # Search left

        return False  # Target not found
# class Solution:
#     def search(self, nums, target):
#         low,high=0,len(nums)-1
#         while low<=high:
#             mid=(low+high)//2
#             if nums[mid]==target:
#                 return True
#             if (nums[low]==nums[mid] or nums[mid]==nums[high]):
#                 low=low+1
#                 high=high-1
#                 continue
#             if nums[low]<=nums[mid]:
#                 if (nums[low]<=target or target<= nums[mid]):
#                     high=mid-1
#                 else:
#                     low=mid+1
#             else:
#                 if (nums[mid]<= target or target<=nums[high]):
#                     low=mid+1
#                 else:
#                     high=mid-1
#         return False