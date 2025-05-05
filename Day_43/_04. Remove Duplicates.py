class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        left = 0  # position for unique elements
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1  # length of the unique portion