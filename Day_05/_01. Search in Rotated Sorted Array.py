class Solution:
    def search(self, nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target | target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if (nums[mid]<=target | target<=nums[high]):
                    low=mid+1
                else:
                    high=mid-1
        return -1