class Solution:
    def search(self, nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid=low+(high-low)//2

            # when mid itself is target
            if nums[mid]==target:
                return mid
            
            # when target likes between low and mid
            if nums[low]<=nums[mid]:
                if (nums[low]<=target and target<=nums[mid]):
                    high=mid-1
                else:
                    low=mid+1

            # when target lies betwreen mid and high
            else:
                if (nums[high]>=target and target>=nums[mid]):
                    low=mid+1
                else:
                    high=mid-1
        return -1