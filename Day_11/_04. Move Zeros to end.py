class Solution:
    def moveZeroes(self, nums):
        non_zero_index = 0
        n=len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
        return nums